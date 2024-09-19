import pandas as pd
import common.log
from common.ApiTest import *
from common.get_data_excel import *
from config.get_config import read_section_key_value_dict
from common.log import setup_logging


def clear_excel_contents(file_path):
    # 读取Excel文件
    df = pd.read_excel(file_path)
    # 将DataFrame中的数据清空
    df.iloc[:, :] = ""
    # 保存Excel文件
    df.to_excel(file_path, index=False)


# 批量删除词集、问答
def delete_words_qa(data_file, sheet_name, case_name1, case_name2):
    default_dict = read_section_key_value_dict('../config/config.ini',
                                               'default')
    Cookie = default_dict['cookie']
    headers = {
        'Content-Type': 'application/json',
        'Cookie': Cookie
    }
    res = my_get(data_file, sheet_name, case_name1, headers=headers)
    res_json = res.json()
    ids = res_json['data']
    url = get_url(data_file, sheet_name, case_name2)
    data = json.dumps(ids)
    res_del = requests.post(url=url, data=data, headers=headers)
    return res_del.text


# 将导出内容写入excel文件
def export(filepath, content, sheet_name):
    # 将导出文件的数据写入excel文件
    filepath = filepath
    with open(filepath, "wb") as file:
        file.write(content)
    data = excel_to_list(filepath, sheet_name)  # 导出文件数据
    return data


# 删除流程树
def delete_project(data_file, sheet_name, case_search, case_del, project_name):
    default_dict = read_section_key_value_dict('../config/config.ini',
                                               'default')
    Cookie = default_dict['cookie']
    headers = {
        'Content-Type': 'application/json',
        'Cookie': Cookie
    }
    # 获取目标流程树的id
    url = get_url(data_file, sheet_name, case_search)
    url_search = url + project_name
    res_search = requests.get(url=url_search, headers=headers)
    res_search_json = res_search.json()
    project_id = res_search_json['data']['paginate']['data'][0]['id']
    # 拼接删除接口地址
    url = get_url(data_file, sheet_name, case_del)
    url_del = url + str(project_id)
    data = get_request_data(data_file, sheet_name, case_del)
    # 删除流程树
    requests.delete(url=url_del, data=json.dumps(data), headers=headers)


# 通过流程树名称查询流程树
def search_project(data_file, sheet_name, case_name, project_name):
    default_dict = read_section_key_value_dict('../config/config.ini',
                                               'default')
    Cookie = default_dict['cookie']
    headers = {
        'Content-Type': 'application/json',
        'Cookie': Cookie
    }
    url = get_url(data_file, sheet_name, case_name)
    url_search = url + project_name
    res = requests.get(url=url_search, headers=headers)
    return res.json()


# 日志
def log_case_info(case_name, expect_res, res_text):
    logger = setup_logging()
    logger.info("测试用例：{}".format(case_name))
    logger.info("期望结果：{}".format(expect_res))
    logger.info("实际结果：{}".format(res_text))


if __name__ == '__main__':
    case_name1 = "测试用例"
    expect_res1 = "成功"
    res_text1 = "成功"
    log_case_info(case_name1, expect_res1, res_text1)
