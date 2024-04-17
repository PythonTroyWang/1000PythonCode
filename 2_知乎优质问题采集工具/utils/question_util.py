import requests
import pandas as pd
import json
import pandas.io.formats.excel

# noinspection PyPropertyAccess
pandas.io.formats.excel.ExcelFormatter.header_style = None


def get_question(keyword, cookie):
    # 整理参数
    target_url = 'https://tools.zhihu.com/api/v2/content/tool/question/list'
    headers = {
        'accept': "application/json, text/javascript, */*; q=0.01",
        'x-requested-with': "XMLHttpRequest",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.114 Safari/537.36",
        'content-type': "application/json",
        'accept-language': "zh-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        'cookie': cookie
    }
    request_json = '{"domains": [],"marketings": [],"search": {"type": "topic","content": "' + keyword + '"},' \
                                                                                                         '"interval": "30d","commercial_answer": "","limitation": {},"smart_switch": true,"gender": [],' \
                                                                                                         '"page": 1,"page_size": 1000, "ordering": "","sorting": ""} '
    request_json = request_json.encode('utf-8')
    # 发送请求
    response = requests.post(target_url, headers=headers, data=request_json)
    # 处理返回值
    data = json.loads(response.text)
    print(response.text)
    if 'code' in data and data['code'] == 401:
        return 'Unauthorized'
    elif data['data']['total'] == 0:
        return None
    else:
        source_df = pd.DataFrame(data['data']['search_list'])
        target_df = source_df[
            ["question_title", "question_token", "answer_vote_ups", "answer_num_total", "pv_total", "click_rate",
             "question_created"]]
        target_df.loc[:, "question_token"] = "https://www.zhihu.com/question/" + target_df["question_token"]
        target_df = target_df.rename(columns={'question_title': '标题',
                                              'question_token': '链接',
                                              'answer_vote_ups': '阅读量增量',
                                              'answer_num_total': '回答人数',
                                              'pv_total': '总浏览量',
                                              'click_rate': '点击率',
                                              'question_created': '创建时间'})
        target_df.index = target_df.index + 1
        filename = f"output/{keyword}.xlsx"
        target_df.to_excel(filename, index=True, header=True)
        return 'OK'
