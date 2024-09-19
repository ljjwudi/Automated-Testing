import requests
import json

from common.get_data_excel import get_test_data


def my_get(data_file, sheet_name, case_name, headers=None):
    case_data = get_test_data(data_file, sheet_name, case_name)
    url = case_data['url']
    response = requests.get(url=url, params=None, headers=headers)
    return response


def my_post(data_file, sheet_name, case_name, headers=None):
    case_data = get_test_data(data_file, sheet_name, case_name)
    url = case_data['url']
    data = json.loads(case_data['data'])
    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    return response


def assert_equal(response, expected_status_code, expected_response_data):
    # 断言响应内容
    assert response.text == expected_response_data
    # 断言状态码
    assert response.status_code == expected_status_code

# if __name__ == '__main__':
#     section_dict = read_section_key_value_dict('../config/config.ini', 'data_path')
#     default_dict = read_section_key_value_dict('../config/config.ini',
#                                                'default')
#     Cookie = default_dict['cookie']
#     res = my_get(section_dict['data_file'], section_dict['sheet_name1'], 'islogged', headers={'Cookie': Cookie})
#     print(res.text)
