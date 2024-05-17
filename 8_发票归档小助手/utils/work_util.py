from datetime import datetime

from excel_util import output_excel_file
from xml_util import get_xml_file, get_xml_content, create_dir, copy_file_to_target, str_to_date_and_get_month


def sendReq(file_dir_path, file_target_path, company_name):
    start_time = datetime.now()

    # 1、获取所有xml文件
    xml_file_array = get_xml_file(file_dir_path)
    # 2、创建目录结构
    create_dir(file_target_path)
    # 3、解析所有xml文件
    xml_data_array = []
    for xml_file in xml_file_array:
        data = get_xml_content(xml_file)
        xml_data_array.append(data)
    # 4、文件copy到指定目录

    for xml_data in xml_data_array:
        index = str_to_date_and_get_month(xml_data[0])
        file_id = xml_data[1]
        seller = xml_data[2]
        buyer = xml_data[3]
        invoice_type = -1
        if buyer == company_name:
            invoice_type = 0
        elif seller == company_name:
            invoice_type = 1
        copy_file_to_target(file_dir_path, file_target_path, file_id, index, invoice_type, buyer, xml_data[0], xml_data[6], seller)
    # 5、生成全年进项销项统计数据表及明细表
    output_excel_file(xml_data_array, company_name, file_target_path)

    end_time = datetime.now()
    print("运行时间：", end_time - start_time)
