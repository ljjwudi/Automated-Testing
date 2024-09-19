import unittest

from common.ApiTest import my_post, assert_equal, my_get
from common.get_data_excel import *


class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次

        cls.section_dict = read_section_key_value_dict('../config/config.ini',
                                                       'data_path')
        cls.header = {"Content-Type": "application/json"}

    def testLogin(self):
        # 获取测试用例数据
        data_Login = get_test_data(section_dict['data_file'], section_dict['sheet_name4'], 'login')
        expect_res = data_Login['expect_res']
        # 发起请求
        response = my_post(section_dict['data_file'], section_dict['sheet_name4'], 'login', headers=self.header)
        # 断言状态码，响应数据
        assert_equal(response, 200, expect_res)

    def testLoginOut(self):
        # 获取Cookie
        response = my_post(section_dict['data_file'], section_dict['sheet_name4'], 'login', headers=self.header)
        Cookie = response.headers['Set-Cookie']

        # 获取测试用例数据
        data_Logout = get_test_data(section_dict['data_file'], section_dict['sheet_name4'], 'logout')
        expect_res_Logout = data_Logout['expect_res']

        data_IsLogged = get_test_data(section_dict['data_file'], section_dict['sheet_name4'], 'is-logged')
        expect_res_IsLogged = data_IsLogged['expect_res']
        # 发起请求
        response_logout = my_get(section_dict['data_file'], section_dict['sheet_name4'], 'logout',
                                 headers={'Cookie': Cookie})  # logout接口
        response_IsLogged = my_get(section_dict['data_file'], section_dict['sheet_name4'], 'is-logged',
                                   headers={'Cookie': Cookie})  # is-logged接口
        # 断言状态码，响应数据
        assert_equal(response_logout, 200, expect_res_Logout)  # 断言登出返回数据
        assert_equal(response_IsLogged, 200, expect_res_IsLogged)  # 通过is-logged接口判断是否成功登出


if __name__ == '__main__':  # 非必要，用于测试码
    unittest.main(verbosity=2)
