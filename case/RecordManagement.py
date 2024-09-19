import random
import unittest

from common.common_api import clear_excel_contents
from common.get_data_excel import *
from common.ApiTest import *
from common.log import setup_logging
from common.transfer_gmt_time import *
import time


class TestRecordManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次
        cls.logger = setup_logging()
        # 获取Cookie

        default_dict = read_section_key_value_dict("../config/config.ini", "default")
        cls.Cookie = default_dict["cookie"]
        cls.headers = {"Cookie": default_dict["cookie"]}
        cls.section_dict = read_section_key_value_dict(
            "../config/config.ini", "data_path"
        )

    def test_message_index_combination(self):
        # 获取预期响应数据
        data = get_test_data(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "message_index_combination",
        )
        expect_res = json.loads(data["expect_res"])
        # 发起请求
        actual_res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "message_index_combination",
            headers=self.headers,
        )
        # 断言结果
        self.assertEqual(actual_res, expect_res)

    def test_call_index_combination(self):
        # 获取预期响应数据
        data = get_test_data(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "call_index_combination",
        )
        expect_res = json.loads(data["expect_res"])
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "call_index_combination",
            headers=self.headers,
        )
        # 断言结果
        self.assertEqual(response.json(), expect_res)

    def test_call_index_by_HandOutBound(self):
        # 获取预期响应数据
        data = get_test_data(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "call_index_by_HandOutBound",
        )
        expect_res = json.loads(data["expect_res"])
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "call_index_by_HandOutBound",
            headers=self.headers,
        )
        # 断言结果
        self.assertEqual(response.json(), expect_res)

    def test_call_index_by_AutoOutBound(self):
        # 获取预期响应数据
        data = get_test_data(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "call_index_by_AutoOutBound",
        )
        expect_res = json.loads(data["expect_res"])
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "call_index_by_AutoOutBound",
            headers=self.headers,
        )
        # 断言结果
        self.assertEqual(response.json(), expect_res)

    def test_review_index_combination(self):
        # 获取预期响应数据
        data = get_test_data(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "review_index_combination",
        )
        expect_res = json.loads(data["expect_res"])
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "review_index_combination",
            headers=self.headers,
        )
        print("\n", type(response.json()), "\n")
        print(type(expect_res))
        # 断言结果
        self.assertEqual(response.json(), expect_res)

    def test_testdata_index_combination(self):
        # 获取预期响应数据
        data = get_test_data(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "testdata_index_combination",
        )
        expect_res = json.loads(data["expect_res"])
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "testdata_index_combination",
            headers=self.headers,
        )
        # 断言结果
        self.assertEqual(response.json(), expect_res)

    def test_index_by_project_closed(self):
        # 获取预期响应数据
        data = get_test_data(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_by_project_closed",
        )
        expect_res = json.loads(data["expect_res"])
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_by_project_closed",
            headers=self.headers,
        )
        # 断言结果
        self.assertEqual(response.json(), expect_res)

    def test_index_by_project_deleted(self):
        # 获取预期响应数据
        data = get_test_data(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_by_project_deleted",
        )
        expect_res = json.loads(data["expect_res"])
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_by_project_deleted",
            headers=self.headers,
        )
        # 断言结果
        self.assertEqual(response.json(), expect_res)

    def test_index_no_result_by_keyword(self):
        # 获取预期响应数据
        data = get_test_data(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_by_id",
        )
        expect_res = json.loads(data["expect_res"])
        # 发起请求
        response_by_id = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_by_id",
            headers=self.headers,
        )
        # 特殊符号
        response_by_symbol01 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_01",
            headers=self.headers,
        )
        response_by_symbol02 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_02",
            headers=self.headers,
        )
        response_by_symbol03 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_03",
            headers=self.headers,
        )
        response_by_symbol04 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_04",
            headers=self.headers,
        )
        response_by_symbol05 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_05",
            headers=self.headers,
        )
        response_by_symbol06 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_06",
            headers=self.headers,
        )
        response_by_symbol07 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_07",
            headers=self.headers,
        )
        response_by_symbol08 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_08",
            headers=self.headers,
        )
        response_by_symbol09 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_09",
            headers=self.headers,
        )
        response_by_symbol10 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_10",
            headers=self.headers,
        )
        response_by_symbol11 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_11",
            headers=self.headers,
        )
        response_by_symbol12 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_12",
            headers=self.headers,
        )
        response_by_symbol13 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_13",
            headers=self.headers,
        )
        response_by_symbol14 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_14",
            headers=self.headers,
        )
        response_by_symbol15 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_15",
            headers=self.headers,
        )
        response_by_symbol16 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_16",
            headers=self.headers,
        )
        response_by_symbol17 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_17",
            headers=self.headers,
        )
        response_by_symbol18 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_18",
            headers=self.headers,
        )
        response_by_symbol19 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_19",
            headers=self.headers,
        )
        response_by_symbol20 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_20",
            headers=self.headers,
        )
        response_by_symbol21 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_21",
            headers=self.headers,
        )
        response_by_symbol22 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_22",
            headers=self.headers,
        )
        response_by_symbol23 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_23",
            headers=self.headers,
        )
        response_by_symbol24 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_24",
            headers=self.headers,
        )
        response_by_symbol25 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_25",
            headers=self.headers,
        )
        response_by_symbol26 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_26",
            headers=self.headers,
        )
        response_by_symbol27 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_27",
            headers=self.headers,
        )
        response_by_symbol28 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_28",
            headers=self.headers,
        )
        response_by_symbol29 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_29",
            headers=self.headers,
        )
        response_by_symbol30 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_30",
            headers=self.headers,
        )
        response_by_symbol31 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_31",
            headers=self.headers,
        )
        response_by_symbol32 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_32",
            headers=self.headers,
        )
        response_by_symbol33 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_33",
            headers=self.headers,
        )
        response_by_symbol34 = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_no_result_34",
            headers=self.headers,
        )

        # 断言结果
        self.assertEqual(response_by_id.json(), expect_res)
        self.assertEqual(response_by_symbol01.json(), expect_res)
        self.assertEqual(response_by_symbol02.json(), expect_res)
        self.assertEqual(response_by_symbol03.json(), expect_res)
        self.assertEqual(response_by_symbol04.json(), expect_res)
        self.assertEqual(response_by_symbol05.json(), expect_res)
        self.assertEqual(response_by_symbol06.json(), expect_res)
        self.assertEqual(response_by_symbol07.json(), expect_res)
        self.assertEqual(response_by_symbol08.json(), expect_res)
        self.assertEqual(response_by_symbol09.json(), expect_res)
        self.assertEqual(response_by_symbol10.json(), expect_res)
        self.assertEqual(response_by_symbol11.json(), expect_res)
        self.assertEqual(response_by_symbol12.json(), expect_res)
        self.assertEqual(response_by_symbol13.json(), expect_res)
        self.assertEqual(response_by_symbol14.json(), expect_res)
        self.assertEqual(response_by_symbol15.json(), expect_res)
        self.assertEqual(response_by_symbol16.json(), expect_res)
        self.assertEqual(response_by_symbol17.json(), expect_res)
        self.assertEqual(response_by_symbol18.json(), expect_res)
        self.assertEqual(response_by_symbol19.json(), expect_res)
        self.assertEqual(response_by_symbol20.json(), expect_res)
        self.assertEqual(response_by_symbol21.json(), expect_res)
        self.assertEqual(response_by_symbol22.json(), expect_res)
        self.assertEqual(response_by_symbol23.json(), expect_res)
        self.assertEqual(response_by_symbol24.json(), expect_res)
        self.assertEqual(response_by_symbol25.json(), expect_res)
        self.assertEqual(response_by_symbol26.json(), expect_res)
        self.assertEqual(response_by_symbol27.json(), expect_res)
        self.assertEqual(response_by_symbol28.json(), expect_res)
        self.assertEqual(response_by_symbol29.json(), expect_res)
        self.assertEqual(response_by_symbol30.json(), expect_res)
        self.assertEqual(response_by_symbol31.json(), expect_res)
        self.assertEqual(response_by_symbol32.json(), expect_res)
        self.assertEqual(response_by_symbol33.json(), expect_res)
        self.assertEqual(response_by_symbol34.json(), expect_res)

    def test_index_year(self):
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "index_year",
            headers=self.headers,
        )

        # 断言结果
        jsonData = response.json()  # 将响应结果转换成json格式
        self.assertEqual(response.status_code, 200)
        self.assertEqual(jsonData["code"], 0)
        self.assertEqual(jsonData["msg"], "success")
        self.assertEqual(jsonData["data"]["total"], 12019)  # 断言data中total数量

    def test_MessageProjectList(self):
        # 获取预期响应数据
        data = get_test_data(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "message-project-list",
        )
        expect_res = data["expect_res"]
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "message-project-list",
            headers=self.headers,
        )

        # 断言结果
        jsonData = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(jsonData["code"], 0)
        self.assertEqual("success", jsonData["msg"])
        self.assertIn(expect_res, response.text)

    def test_TelephoneProjectList(self):
        # 获取预期响应数据
        data = get_test_data(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "telephone-project-list",
        )
        expect_res = data["expect_res"]
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "telephone-project-list",
            headers=self.headers,
        )

        # 断言结果
        jsonData = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(jsonData["code"], 0)
        self.assertEqual("success", jsonData["msg"])
        self.assertIn(expect_res, response.text)

    def test_export_record(self):
        download_result_data = get_test_data(
            section_dict["data_file"], section_dict["sheet_name2"], "download-result"
        )
        # 发起请求
        # 创建压缩包
        create_package_response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "create-package",
            headers=self.headers,
        )
        # open_status = None
        # while not open_status:
        #     progress_res = my_get(
        #         section_dict["data_file"],
        #         section_dict["sheet_name2"],
        #         "export-progress",
        #         headers=self.headers,
        #     )
        #     # 日志
        #     self.logger.info(f"test_export_words\t{progress_res.text}")
        #     progress_res_json = progress_res.json()
        #     open_status = progress_res_json["data"]["open_status"]
        #     time.sleep(5)
        # # 导出列表
        # export_list_response = my_get(
        #     section_dict["data_file"],
        #     section_dict["sheet_name2"],
        #     "export-list",
        #     headers=self.headers,
        # )
        #
        # jsonData = export_list_response.json()  # 将响应结果转换成json格式
        # file_id = jsonData["data"][0]["id"]  # 获取文件下载接口所需的参数id
        # data = {"id": file_id}
        # url = download_result_data["url"]
        # # 下载压缩包
        # result_res = requests.post(url=url, data=data, headers=self.headers)
        # 将导出文件的数据写入excel文件
        # filepath = '../data/record-down-result.xlsx'
        # with open(filepath, "wb") as file:
        #     file.write(result_res.content)
        # # 读取文件内容
        # actual_res = excel_to_list(filepath, 'sheet1')
        # print(actual_res)
        # 获取预期结果
        # expect_res = get_expect_res_text(section_dict['data_file'], section_dict['sheet_name7'], 'down_result')
        # 清除文件内容
        # clear_excel_contents(filepath)
        # 断言
        # self.assertEqual(expect_res, str(actual_res))

    def test_CalloutTaskList(self):
        # 获取预期响应数据
        data = get_test_data(
            section_dict["data_file"], section_dict["sheet_name2"], "callout-task-list"
        )
        expect_res = data["expect_res"]
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "callout-task-list",
            headers=self.headers,
        )
        print("\n", expect_res)
        print(response.text)
        # 断言结果
        jsonData = response.json()  # 将响应结果转换成json格式
        self.assertEqual(response.status_code, 200)
        self.assertEqual(jsonData["code"], 0)
        self.assertEqual(jsonData["msg"], "success")
        self.assertIn(expect_res, response.text)

    def test_OutboundTaskList(self):
        # 获取预期响应数据
        data = get_test_data(
            section_dict["data_file"], section_dict["sheet_name2"], "outbound-task-list"
        )
        expect_res = data["expect_res"]
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "outbound-task-list",
            headers=self.headers,
        )
        # 断言结果
        jsonData = response.json()  # 将响应结果转换成json格式
        self.assertEqual(response.status_code, 200)
        self.assertEqual(jsonData["code"], 0)
        self.assertEqual(jsonData["msg"], "success")
        self.assertIn(expect_res, response.text)

    def test_update_data(self):
        # 请求数据
        get_data = get_test_data(
            section_dict["data_file"], section_dict["sheet_name2"], "update_data"
        )  # 获取用例update的数据
        data = json.loads(get_data["data"])  # 获取请求参数
        url = get_data["url"]
        expect_res = get_data["expect_res"]

        # 设置tags为随机数
        random_tags = random.randint(1, 10000)  # 生成随机数来作为tags的值
        tags = [f"{random_tags}"]
        data["tags"] = tags
        data_json = json.dumps(data)

        # 发起请求

        # 修改数据接口：/v2/call/call-log/{id}
        response_update = requests.patch(
            url=url,
            data=data_json,
            headers={"Cookie": self.Cookie, "Content-Type": "application/json"},
        )

        # 通过id检索被修改的消息记录
        response_update_for_check_tags = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "update-for_check_tags",
            headers=self.headers,
        )

        response_update_for_check_tags_jsonData = response_update_for_check_tags.json()
        # 断言结果
        actual_tags = response_update_for_check_tags_jsonData["data"]["data"][0]["tags"]
        expect_tags = tags
        assert_equal(response_update, 200, expect_res)
        self.assertEqual(actual_tags, expect_tags)  # 断言标签

    def test_TableHeader(self):
        # 获取预期响应数据
        data = get_test_data(
            section_dict["data_file"], section_dict["sheet_name2"], "table-header"
        )
        expect_res = data["expect_res"]
        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name2"],
            "table-header",
            headers=self.headers,
        )

        # 断言结果
        self.assertIn(expect_res, response.text)
