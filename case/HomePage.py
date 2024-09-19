import unittest
from common.get_data_excel import *
from config.get_config import *
from common.ApiTest import *


class TestHomePage(unittest.TestCase):
    """
    测试模块：首页
    包含接口：

    """

    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次

        dict_default = read_section_key_value_dict("../config/config.ini", "default")
        cls.Cookie = dict_default["cookie"]
        cls.headers = {
            "Cookie": dict_default["cookie"],
            "Content-Type": "application/json",
        }
        cls.section_dict = read_section_key_value_dict(
            "../config/config.ini", "data_path"
        )

    # def testLogin(self):
    #     # 获取测试用例数据
    #     data_Login = get_test_data(section_dict['data_file'], section_dict['sheet_name1'], 'login')
    #     expect_res = data_Login['expect_res']
    #     # 发起请求
    #     response = my_post(section_dict['data_file'], section_dict['sheet_name1'], 'login')
    #     # 断言状态码，响应数据
    #     if response.text != expect_res:
    #         print('\n', response.text, '\n', expect_res)
    #     assert_equal(response, 200, expect_res)

    def test_IsLogged(self):
        # 获取测试用例数据
        data_IsLogged = get_test_data(
            section_dict["data_file"], section_dict["sheet_name1"], "is-logged"
        )
        expect_res = data_IsLogged["expect_res"]
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name1"],
            "is-logged",
            headers=self.headers,
        )
        # 断言状态码，响应数据
        assert_equal(response, 200, expect_res)

    def test_BasicInfo(self):
        # 获取测试用例数据
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name1"], "basic-info"
        )
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name1"],
            "basic-info",
            headers=self.headers,
        )
        # 断言结果

        self.assertEqual(expect_res, response.json())

    def test_Permissions(self):
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name1"],
            "permissions",
            headers=self.headers,
        )
        jsonData = response.json()
        # 断言结果
        self.assertEqual(response.status_code, 200)  # 断言状态码
        self.assertIsNotNone(jsonData["data"]["permissions"])  # 断言data中permissions数据不为空
        self.assertIn("success", jsonData["msg"])  # 断言msg
        self.assertEqual(jsonData["code"], 0)

    def test_Config(self):
        # 发起请求
        response = my_post(
            section_dict["data_file"],
            section_dict["sheet_name1"],
            "config",
            headers=self.headers,
        )
        # 预期结果
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name1"], "config"
        )
        # 实际结果
        actual_res = response.json()
        # 断言结果
        if response.text != expect_res:
            print("\n", response.text, "\n", expect_res)
        self.assertEqual(expect_res, actual_res)

    def test_Corner(self):
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name1"],
            "corner",
            headers=self.headers,
        )
        jsonData = response.json()
        # print(jsonData['data'])
        # print(response.text)
        # 断言结果
        self.assertEqual(response.status_code, 200)  # 断言状态码
        self.assertIsNotNone(jsonData["data"])  # 断言data中数据不为空
        self.assertIn("success", jsonData["msg"])  # 断言msg
        self.assertEqual(jsonData["code"], 0)

    def test_AllProjects(self):
        # 获取测试用例数据
        data_AllProjects = get_test_data(
            section_dict["data_file"], section_dict["sheet_name1"], "all-projects"
        )
        expect_res = json.loads(data_AllProjects["expect_res"])
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name1"],
            "all-projects",
            headers=self.headers,
        )
        jsonData = response.json()
        # print(jsonData['data'])
        # print(response.text)
        # 断言结果
        self.assertEqual(response.status_code, 200)  # 断言状态码
        self.assertIn(expect_res, jsonData["data"])  # 断言data包含expect_res
        self.assertEqual("success", jsonData["msg"])  # 断言msg
        self.assertEqual(jsonData["code"], 0)

    def test_PhoneLine(self):
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name1"],
            "phone-line",
            headers=self.headers,
        )
        jsonData = response.json()
        # 断言结果
        self.assertEqual(response.status_code, 200)  # 断言状态码
        self.assertIsNotNone(jsonData["data"]["phone_line"])  # 断言data中的phone_line数据不为空
        self.assertEqual("success", jsonData["msg"])  # 断言msg
        self.assertEqual(jsonData["code"], 0)

    def test_Count(self):
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name1"],
            "count",
            headers=self.headers,
        )
        jsonData = response.json()
        # print(jsonData['data'])
        # print(response.text)
        # 断言结果
        self.assertEqual(response.status_code, 200)  # 断言状态码
        self.assertIsNotNone(jsonData["data"])  # 断言data中的phone_line数据不为空
        self.assertEqual("success", jsonData["msg"])  # 断言msg
        self.assertEqual(jsonData["code"], 0)