import xml.etree.ElementTree as ET
from datetime import datetime
import os
import shutil


# 获取文件夹中的所有XML文件
def get_xml_file(file_dir_path):
    xml_file_array = []
    for root, dirs, files in os.walk(file_dir_path):
        for f in files:
            if os.path.splitext(f)[1] == '.xml':
                xml_file_path = os.path.join(root, f)
                xml_file_array.append(xml_file_path)
    return xml_file_array


def get_xml_content(xml_file_path):
    # 加载XML文件
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    date_str = ''
    file_id = ''
    seller = ''
    buyer = ''
    amount = ''
    tax_amount = ''
    total_amount = ''

    invoice_status = root.find('./Header/InherentLabel/InIssuType/LabelCode')
    invoice_type = root.find('./Header/InherentLabel/GeneralOrSpecialVAT/LabelName')

    # 获取节点数据
    for element in root.iter():
        if element.tag == 'IssueTime':
            date_str = element.text
            if len(date_str) == 19:
                date_str = date_str[0:10]
        if element.tag == 'EIid':
            file_id = element.text
        if element.tag == 'SellerName':
            seller = element.text
        if element.tag == 'BuyerName':
            buyer = element.text
        if element.tag == 'TotalTax-includedAmount':
            total_amount = element.text
        if element.tag == 'TotalTaxAm':
            tax_amount = element.text
        if element.tag == 'TotalAmWithoutTax':
            amount = element.text

    return date_str, file_id, seller, buyer, amount, tax_amount, total_amount, invoice_status.text, invoice_type.text


def copy_file_to_target(file_dir_path, file_target_path, file_id, index, invoice_type, buyer_name, date, total_amount, seller_name):
    for root, dirs, files in os.walk(file_dir_path):
        for f in files:
            other_file_path = os.path.join(root, f)
            if file_id in os.path.splitext(f)[0] and os.path.splitext(f)[1] != '.xlsx':
                if invoice_type == 0:
                    new_name_path = file_id + "_" + seller_name + "_" + date.replace('-', '') + "_" + total_amount + \
                                    os.path.splitext(f)[1]
                    file_target_path_input = file_target_path + "/" + str(index) + "月" + "/进项发票/"
                    if os.path.splitext(f)[1] == '.pdf':
                        copy_file(other_file_path, file_target_path_input + "pdf")
                        if not os.path.exists(os.path.join(file_target_path_input + "pdf", new_name_path)):
                            os.rename(os.path.join(file_target_path_input + "pdf", f),
                                      os.path.join(file_target_path_input + "pdf", new_name_path))
                        else:
                            os.remove(os.path.join(file_target_path_input + "pdf", f))
                    if os.path.splitext(f)[1] == '.ofd':
                        copy_file(other_file_path, file_target_path_input + "ofd")
                        if not os.path.exists(os.path.join(file_target_path_input + "ofd", new_name_path)):
                            os.rename(os.path.join(file_target_path_input + "ofd", f),
                                      os.path.join(file_target_path_input + "ofd", new_name_path))
                        else:
                            os.remove(os.path.join(file_target_path_input + "ofd", f))
                    if os.path.splitext(f)[1] == '.xml':
                        copy_file(other_file_path, file_target_path_input + "xml")
                        if not os.path.exists(os.path.join(file_target_path_input + "xml", new_name_path)):
                            os.rename(os.path.join(file_target_path_input + "xml", f),
                                      os.path.join(file_target_path_input + "xml", new_name_path))
                        else:
                            os.remove(os.path.join(file_target_path_input + "xml", f))
                elif invoice_type == 1:
                    new_name_path = file_id + "_" + buyer_name + "_" + date.replace('-', '') + "_" + total_amount + \
                                    os.path.splitext(f)[1]
                    file_target_path_output = file_target_path + "/" + str(index) + "月" + "/销项发票/"
                    if os.path.splitext(f)[1] == '.pdf':
                        copy_file(other_file_path, file_target_path_output + "pdf")
                        if not os.path.exists(os.path.join(file_target_path_output + "pdf", new_name_path)):
                            os.rename(os.path.join(file_target_path_output + "pdf", f),
                                      os.path.join(file_target_path_output + "pdf", new_name_path))
                        else:
                            os.remove(os.path.join(file_target_path_output + "pdf", f))
                    if os.path.splitext(f)[1] == '.ofd':
                        copy_file(other_file_path, file_target_path_output + "ofd")
                        if not os.path.exists(os.path.join(file_target_path_output + "ofd", new_name_path)):
                            os.rename(os.path.join(file_target_path_output + "ofd", f),
                                      os.path.join(file_target_path_output + "ofd", new_name_path))
                        else:
                            os.remove(os.path.join(file_target_path_output + "ofd", f))
                    if os.path.splitext(f)[1] == '.xml':
                        copy_file(other_file_path, file_target_path_output + "xml")
                        if not os.path.exists(os.path.join(file_target_path_output + "xml", new_name_path)):
                            os.rename(os.path.join(file_target_path_output + "xml", f),
                                      os.path.join(file_target_path_output + "xml", new_name_path))
                        else:
                            os.remove(os.path.join(file_target_path_output + "xml", f))
                else:
                    print('错误的发票类型')


def create_dir(file_target_path):
    for i in range(1, 13):
        path_month_type11 = file_target_path + "/" + str(i) + "月" + "/进项发票/pdf"
        path_month_type12 = file_target_path + "/" + str(i) + "月" + "/进项发票/ofd"
        path_month_type13 = file_target_path + "/" + str(i) + "月" + "/进项发票/xml"
        path_month_type21 = file_target_path + "/" + str(i) + "月" + "/销项发票/pdf"
        path_month_type22 = file_target_path + "/" + str(i) + "月" + "/销项发票/ofd"
        path_month_type23 = file_target_path + "/" + str(i) + "月" + "/销项发票/xml"
        os.makedirs(path_month_type11, exist_ok=True)
        os.makedirs(path_month_type12, exist_ok=True)
        os.makedirs(path_month_type13, exist_ok=True)
        os.makedirs(path_month_type21, exist_ok=True)
        os.makedirs(path_month_type22, exist_ok=True)
        os.makedirs(path_month_type23, exist_ok=True)


def copy_file(source_path, destination_path):
    shutil.copy2(source_path, destination_path)


def str_to_date_and_get_month(date_str):
    try:
        if len(date_str) == 10:
            # 如果时间字符串长度为10，说明只包含年月日
            date = datetime.strptime(date_str, "%Y-%m-%d")
        elif len(date_str) == 19:
            # 如果时间字符串长度为19，说明包含年月日时分秒
            date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        else:
            # 其他情况，可以根据实际需求进行处理
            date = None
        return date.month
    except ValueError as e:
        print("无法将字符串转换为日期！错误信息：", e)
