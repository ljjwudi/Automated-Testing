import unittest
from common.get_data_excel import *
from config.get_config import *
from common.ApiTest import *


class TestHandOutbound(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次

        dict_default = read_section_key_value_dict('../config/config.ini',
                                                   'default')
        cls.Cookie = dict_default['cookie']
        cls.section_dict = read_section_key_value_dict('../config/config.ini',
                                                       'data_path')

    def testNewHandTask(self):
        # 获取测试用例数据
        data_NewHandTask = get_test_data(section_dict['data_file'],
                                         section_dict['sheet_name3'],
                                         'new_hand_task')
        url = data_NewHandTask['url']
        data = json.loads(data_NewHandTask['data'])
        expect_res = data_NewHandTask['expect_res']
        file_path = '../data/phone_number.csv'
        phone_number = open(file_path, 'rb')
        # 发起请求

        headers = {'Cookie': self.Cookie, 'Content-Type': 'multipart/form-data; boundary=<calculated when request is '
                                                          'sent>'}

        response = requests.post(url=url, data=data, headers=headers)
        # 断言结果
        print(data)
        print(phone_number)
        print(response.text)
        assert_equal(response, 200, expect_res)

    def testPermissions(self):
        # 发起请求
        response = my_get(section_dict['data_file'], section_dict['sheet_name1'], 'permissions',
                          headers={'Cookie': self.Cookie})
        jsonData = response.json()
        # 断言结果
        self.assertEqual(response.status_code, 200)  # 断言状态码
        self.assertIsNotNone(jsonData['data']['permissions'])  # 断言data中permissions数据不为空
        self.assertIn('success', jsonData['msg'])  # 断言msg
        self.assertEqual(jsonData['code'], 0)
