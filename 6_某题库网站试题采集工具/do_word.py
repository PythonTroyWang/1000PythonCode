from utils import requests_util
from utils import converts_util
from datetime import datetime


def sendReq(url, cookie):
    try:
        start_time = datetime.now()
        # 采集数据
        content = requests_util.HTRequest(url, cookie)
        end_time = datetime.now()
        print("采集单篇运行时间：", end_time - start_time)

        start_time = datetime.now()
        # 解析数据并生成word
        converts_util.parse(content, url)
        end_time = datetime.now()
        print("解析并生成word运行时间：", end_time - start_time)
    except Exception:
        return 'error'
