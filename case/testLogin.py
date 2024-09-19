import unittest

from requests import post

from common.ApiTest import *
from common.get_data_excel import *


class TestLogin(unittest.TestCase):
    case_data = {}
    data_list = {}

    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次

        # 获取测试用例数据
        cls.url = extract_data_by_keyword(section_dict['data_file'], section_dict['sheet_name'],
                                          'testcase_login', 'url')
        cls.data = extract_data_by_keyword(section_dict['data_file'], section_dict['sheet_name'],
                                           'testcase_login', 'data')
        cls.expect_res = extract_data_by_keyword(section_dict['data_file'], section_dict['sheet_name'],
                                                 'testcase_login', 'expect_res')

    def test_testLogin(self):
        # 发送POST请求，并断言响应状态码和响应数据
        response = post(url=self.url, data=json.loads(self.data))
        assert_equal(response, 200, self.expect_res)


if __name__ == '__main__':
    unittest.main(verbosity=2)
