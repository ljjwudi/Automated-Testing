import requests
import json  # 用来转化excel中的json字符串为字典

from common.ApiTest import my_post
from common.get_data_excel import *

section_dict = read_section_key_value_dict('../config/config.ini',
                                           'data_path')
try:
    # 从excel中的get_cookie获取登录信息
    response = my_post(section_dict['data_file'], section_dict['sheet_name1'], 'get_cookie')
    print(response.text)
    Cookie = response.headers['Set-Cookie']  # 获取Cookie
    print(Cookie)
    # 读取config.ini
    config = configparser.ConfigParser()
    config.read("../config/config.ini")
    # 将获得的Cookie值传入config.ini
    config['default']['Cookie'] = Cookie
    with open('../config/config.ini', 'w') as configfile:
        config.write(configfile)
except requests.exceptions.RequestException as e:
    print("请求发生异常:", e)
    # 处理异常情况
