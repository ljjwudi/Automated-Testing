import json

import xlrd
from config.get_config import *

section_dict = read_section_key_value_dict('../config/config.ini', 'data_path')


def excel_to_list(data_file, sheet_name):
    """
    :param data_file:excel文件路径
    :param sheet_name:excel文件表名
    :return：sheet_name表所有数据
    """
    data_list = []  # 新建个空列表，来乘装所有的数据
    wb = xlrd.open_workbook(data_file)  # 打开excel
    sh = wb.sheet_by_name(sheet_name)  # 获取工作簿
    header = sh.row_values(0)  # 获取标题行数据
    for i in range(1, sh.nrows):  # 跳过标题行，从第二行开始取数据
        d = dict(zip(header, sh.row_values(i)))  # 将标题和每行数据组装成字典
        data_list.append(d)
    return data_list  # 列表嵌套字典格式，每个元素是一个字典


def get_test_data(data_file, sheet_name, case_name):
    """
    :param data_file: excel文件路径
    :param sheet_name: excel文件表名
    :param case_name: 用例名称
    :return:对应case_name的所有数据
    """
    # 获取测试用例数据
    data_list = excel_to_list(data_file, sheet_name)
    for case_data in data_list:
        if case_name == case_data['case_name']:  # 如果字典数据中case_name与参数一致
            return case_data


def get_url(data_file, sheet_name, case_name):
    # 使用该方法获取url
    data = get_test_data(data_file, sheet_name, case_name)
    url = data['url']
    return url


def get_expect_res(data_file, sheet_name, case_name):
    # 使用该方法获取预期结果
    data = get_test_data(data_file, sheet_name, case_name)
    expect_res = data['expect_res']
    return json.loads(expect_res)


def get_expect_res_text(data_file, sheet_name, case_name):
    # 使用该方法获取预期结果(文本)
    data = get_test_data(data_file, sheet_name, case_name)
    expect_res = data['expect_res']
    return expect_res


def get_request_data(data_file, sheet_name, case_name):
    # 使用该方法获取请求数据
    data = get_test_data(data_file, sheet_name, case_name)
    request_data = json.loads(data['data'])
    return request_data


def get_request_data_text(data_file, sheet_name, case_name):
    # 使用该方法获取请求数据
    data = get_test_data(data_file, sheet_name, case_name)
    request_data = json.loads(data['data'])
    return request_data

# def extract_data_by_keyword(data_file, sheet_name, case_name, keyword):
#     """
#     :param data_file: excel文件路径
#     :param sheet_name: excel文件表名
#     :param case_name: 用例名称
#     :param keyword: 关键词，如：url，data，expect_res
#     :return:
#     """
#     # 根据关键词获取测试用例数据中的相关数据如:url,data等
#     case_data = get_test_data(data_file, sheet_name, case_name)
#     result = {}
#     for key, value in case_data.items():
#         if keyword in str(key):
#             result = value
#     return result


# if __name__ == '__main__':
#     url = get_url(section_dict['data_file'], section_dict['sheet_name5'], 'export_qa')
#     data = get_request_data(section_dict['data_file'], section_dict['sheet_name5'], 'export_qa')
#     res = expect_res = get_expect_res(section_dict['data_file'], section_dict['sheet_name5'], 'export_qa')
#     print(type(data))
#     print(url)
#     print(res)
