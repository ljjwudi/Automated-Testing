import time
import unittest

from common.common_api import clear_excel_contents, delete_words_qa
from common.get_data_excel import *
from common.ApiTest import *

qa_id = ''  # 设置全局变量qa_id


class TestQA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次

        # 获取Cookie
        default_dict = read_section_key_value_dict("../config/config.ini", "default")
        cls.Cookie = default_dict["cookie"]
        cls.headers = {
            "Cookie": default_dict["cookie"],
            "Content-Type": "application/json",
        }
        cls.section_dict = read_section_key_value_dict(
            "../config/config.ini", "data_path"
        )

    def test_search_qa_combination(self):
        # 获取测试用例数据
        data = get_test_data(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "search_qa_combination",
        )
        expect_res = data["expect_res"]

        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "search_qa_combination",
            headers=self.headers,
        )

        # 断言结果
        self.assertEqual(response.status_code, 200)  # 断言状态码
        self.assertIn(expect_res, response.text)  # 断言data包含expect_res

    def test_search_qa_by_question(self):
        # 获取测试用例数据
        expect_res = get_expect_res_text(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "search_qa_by_question",
        )

        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "search_qa_by_question",
            headers=self.headers,
        )
        # 断言结果
        self.assertIn(expect_res, response.text)  # 断言data包含expect_res

    def test_search_qa_by_answer(self):
        # 获取测试用例数据
        data = get_test_data(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "search_qa_by_answer",
        )
        expect_res = data["expect_res"]

        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "search_qa_by_answer",
            headers=self.headers,
        )
        # 断言结果
        self.assertIn(expect_res, response.text)  # 断言data包含expect_res

    def test_search_qa_by_pagesize(self):
        # 获取测试用例数据
        expect_res = get_expect_res_text(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "search_qa_by_pagesize",
        )

        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "search_qa_by_pagesize",
            headers=self.headers,
        )
        # 断言结果
        jsonData = response.json()
        actual_res = jsonData["data"]["paginate"]["per_page"]
        self.assertEqual(expect_res, actual_res)

    def test_new_qa(self):
        # 获取测试用例数据
        data = get_test_data(
            section_dict["data_file"], section_dict["sheet_name5"], "new_qa"
        )
        expect_res = data["expect_res"]
        url = data["url"]
        data1 = {
            "group_name": "自动化测试分组",
            "category_id": "node-1-1606902493661",
            "question": [
                "测试一下你好",
                "测试一下你好测试一下你好测试一下你好测试一下你好",
                "测试1",
                "测试2",
                "测试3",
                "test1",
                "test2",
                "test3",
            ],
            "answer": ["测试成功谢谢谢谢再见谢谢谢谢test"],
            "tts_mark_answer": ["测试成功谢谢谢谢再见谢谢谢谢<LR>test"],
            "answer_type": 1,
            "active_time_option": 1,
            "active_start_time": "",
            "active_end_time": "",
            "enable_recommend": 1,
            "enable_prompt": 1,
        }
        # 新建问答
        response = requests.post(
            url=url,
            data=json.dumps(data1),
            headers={"Cookie": self.Cookie, "Content-Type": "application/json"},
        )
        # 获取要查询的目标问答库id
        response_get_qa_id = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "get_qa_id_from_new_qa",
            headers=self.headers,
        )
        jsonData = response_get_qa_id.json()
        global qa_id
        qa_id = str(jsonData["data"]["paginate"]["data"][0]["id"])
        # 断言结果
        assert_equal(response, 200, expect_res)

    def test_edit_qa(self):
        # 编辑问答
        url = (
            "http://ai-service-frontend-test1.aiad-internal.aiadtech.cn/v2/qa/" + qa_id
        )
        request_data = get_request_data(
            section_dict["data_file"], section_dict["sheet_name5"], "edit_qa"
        )
        res = requests.patch(
            url=url, data=json.dumps(request_data), headers=self.headers
        )
        # 查询编辑后问答数据
        url = (
            "http://ai-service-frontend-test1.aiad-internal.aiadtech.cn/v2/qa?page=1&page_size=10&is_open=0"
            "&knowledge_cid=&option=1&search=%E6%B5%8B%E8%AF%95%E4%B8%80%E4%B8%8B%E4%BD%A0%E5%A5%BD "
        )
        response = requests.get(url=url, headers=self.headers)
        actual_res = response.text
        # 断言
        expect_res = get_expect_res_text(
            section_dict["data_file"], section_dict["sheet_name5"], "edit_qa"
        )
        self.assertIn(expect_res, actual_res)

    def test_check_relation(self):
        # 检查流程中的引用
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "check-relation",
            headers=self.headers,
        )
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name5"], "check-relation"
        )

        # 断言结果
        self.assertEqual(response.json(), expect_res)

    def test_delete_qa(self):
        # 获取测试用例数据
        data = get_test_data(
            section_dict["data_file"], section_dict["sheet_name5"], "delete_qa"
        )
        expect_res = data["expect_res"]

        # 删除目标问答

        url = (
            "http://ai-service-frontend-test1.aiad-internal.aiadtech.cn/v2/qa/" + qa_id
        )  # 删除问答库请求url

        response_delete_qa = requests.delete(url=url, headers=self.headers)

        # 断言结果
        assert_equal(response_delete_qa, 200, expect_res)

    def test_search_qa_id(self):
        # 获取测试用例数据
        data = get_test_data(
            section_dict["data_file"], section_dict["sheet_name5"], "search_qa_id"
        )
        expect_res = json.loads(data["expect_res"])

        # 发起请求
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "search_qa_id",
            headers=self.headers,
        )
        # 断言结果
        self.assertEqual(expect_res, response.json())

    def test_mul_qa_close(self):
        # 批量编辑问答开关状态
        request_body = {"ids": [qa_id], "operation": 1, "operation_value": 2}
        data_mul_qa_status = get_test_data(
            section_dict["data_file"], section_dict["sheet_name5"], "mul_qa"
        )
        url = data_mul_qa_status["url"]  # 获取url
        requests.post(
            url=url, data=json.dumps(request_body), headers=self.headers
        )  # 请求批量编辑接口,关闭问答
        # 通过查询接口，验证问答状态
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "search_for_status",
            headers=self.headers,
        )  # 查询问答
        jsonData = response.json()
        actual_res = jsonData["data"]["paginate"]["data"][0]["is_open"]  # 获取问答的开关状态
        # 断言结果
        self.assertEqual(bool(0), actual_res)

    def test_mul_qa_open(self):
        # 批量编辑问答开关状态
        request_body = {"ids": [qa_id], "operation": 1, "operation_value": 1}
        data_mul_qa_status = get_test_data(
            section_dict["data_file"], section_dict["sheet_name5"], "mul_qa"
        )
        url = data_mul_qa_status["url"]  # 获取url
        requests.post(
            url=url, data=json.dumps(request_body), headers=self.headers
        )  # 请求批量编辑接口,关闭问答
        # 通过查询接口，验证问答状态
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "search_for_status",
            headers=self.headers,
        )  # 查询问答
        jsonData = response.json()
        actual_res = jsonData["data"]["paginate"]["data"][0]["is_open"]  # 获取问答的开关状态
        # 断言结果
        self.assertEqual(bool(1), actual_res)

    def test_mul_qa_range(self):
        # 批量编辑问答应用范围
        request_body = {
            "ids": [qa_id],
            "operation": 3,
            "enable_recommend": 2,
            "enable_prompt": 2,
        }
        data_mul_qa_range = get_test_data(
            section_dict["data_file"], section_dict["sheet_name5"], "mul_qa"
        )
        url = data_mul_qa_range["url"]  # 获取url
        requests.post(
            url=url, data=json.dumps(request_body), headers=self.headers
        )  # 请求批量编辑接口,修改应用范围
        # 通过查询接口，验证问答状态
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "search_for_status",
            headers=self.headers,
        )  # 查询问答
        jsonData = response.json()
        enable_prompt = jsonData["data"]["paginate"]["data"][0][
            "enable_prompt"
        ]  # 获取问答应用范围推荐问状态
        enable_recommend = jsonData["data"]["paginate"]["data"][0][
            "enable_prompt"
        ]  # 获取问答应用范围输入联想状态

        # 断言结果
        self.assertEqual(enable_prompt, 2)
        self.assertEqual(enable_recommend, 2)

    def test_mul_qa_label(self):
        # 批量清空发音标注
        request_body = {"ids": [qa_id], "operation": 2}
        data_mul_qa_label = get_test_data(
            section_dict["data_file"], section_dict["sheet_name5"], "mul_qa"
        )
        url = data_mul_qa_label["url"]  # 获取url
        requests.post(
            url=url, data=json.dumps(request_body), headers=self.headers
        )  # 请求批量编辑接口,清空发音标注
        # 通过查询接口，验证发音标注是否被清空
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "search_for_status",
            headers=self.headers,
        )  # 查询问答
        jsonData = response.json()
        tts_mark_answer = jsonData["data"]["paginate"]["data"][0][
            "tts_mark_answer"
        ]  # 获取发音标注，结果为空
        expect_res = []  # 预期结果为空
        # 断言结果
        self.assertEqual(tts_mark_answer, expect_res)

    def test_mul_delete_qa(self):
        # 新建问答
        data = get_test_data(
            section_dict["data_file"], section_dict["sheet_name5"], "new_qa"
        )
        url_new_qa = data["url"]
        data_new_qa = {
            "group_name": "自动化测试",
            "category_id": "node-1-1606902493661",
            "question": ["自动化你好"],
            "answer": ["你好你好"],
            "tts_mark_answer": [""],
            "answer_type": 1,
            "active_time_option": 1,
            "active_start_time": "",
            "active_end_time": "",
            "enable_recommend": 1,
            "enable_prompt": 1,
        }
        requests.post(
            url=url_new_qa, data=json.dumps(data_new_qa), headers=self.headers
        )
        time.sleep(1)
        # 批量删除问答
        response_get_qa_id = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "search_qa",
            headers=self.headers,
        )
        jsonData = response_get_qa_id.json()
        del_id = str(jsonData["data"]["paginate"]["data"][0]["id"])  # 获取目标id
        data_mul_del_qa = {"ids": [del_id]}
        url_mul_del = get_url(
            section_dict["data_file"], section_dict["sheet_name5"], "mul_delete_qa"
        )  # 获取批量删除接口url
        time.sleep(1)
        requests.post(
            url=url_mul_del, data=json.dumps(data_mul_del_qa), headers=self.headers
        )  # 发起请求

        # 通过被删除问答的id查询
        url_search_qa = get_url(
            section_dict["data_file"], section_dict["sheet_name5"], "search_qa_for14"
        )  # 获取查询问答接口url
        time.sleep(1)
        response = requests.get(
            url=url_search_qa, data=json.dumps(data_mul_del_qa), headers=self.headers
        )  # 发起请求
        data = response.json()
        actual_res = data["data"]["paginate"]["total"]  # 获取响应数据
        # 断言
        self.assertEqual(0, actual_res)

    def test_mul_check(self):
        # 批量检查流程中的引用
        response = my_post(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "mul_check",
            headers=self.headers,
        )  # 调用批量检查流程引用接口
        # 断言
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name5"], "mul_check"
        )  # 获取预期结果
        actual_res = response.json()  # 获取实际结果
        self.assertEqual(expect_res, actual_res)

    def test_close_qa(self):
        # 开启问答
        request_body = {"id": qa_id, "open": 0}
        data_close_qa = get_test_data(
            section_dict["data_file"], section_dict["sheet_name5"], "open_qa"
        )
        url = data_close_qa["url"]  # 获取url
        requests.post(
            url=url, data=json.dumps(request_body), headers=self.headers
        )  # 请求接口,开启问答

        # 通过查询接口，验证问答是否被关闭
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "search_for_status",
            headers=self.headers,
        )  # 查询问答
        jsonData = response.json()
        expect_res = jsonData["data"]["paginate"]["data"][0]["is_open"]  # 获取问答开启状态

        # 断言结果
        self.assertEqual(bool(0), expect_res)

    def test_open_qa(self):
        # 开启问答
        request_body = {"id": qa_id, "open": 1}
        data_close_qa = get_test_data(
            section_dict["data_file"], section_dict["sheet_name5"], "open_qa"
        )
        url = data_close_qa["url"]  # 获取url
        requests.post(
            url=url, data=json.dumps(request_body), headers=self.headers
        )  # 请求接口,关闭问答

        # 通过查询接口，验证问答是否被关闭
        response = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "search_for_status",
            headers=self.headers,
        )  # 查询问答
        jsonData = response.json()
        expect_res = jsonData["data"]["paginate"]["data"][0]["is_open"]  # 获取问答开启状态

        # 断言结果
        self.assertEqual(bool(1), expect_res)

    def test_export_qa(self):
        # 导出问答
        response = my_post(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "export_qa",
            headers=self.headers,
        )  # 发起请求
        # 将导出文件的数据写入excel文件
        filepath = "../data/exportData.xlsx"
        with open(filepath, "wb") as file:
            file.write(response.content)
        actual_res = excel_to_list("../data/exportData.xlsx", "Worksheet")  # 导出文件数据
        # 断言
        expect_res = get_expect_res_text(
            section_dict["data_file"], section_dict["sheet_name5"], "export_qa"
        )  # 获取预期结果
        self.assertEqual(expect_res, str(actual_res))

        clear_excel_contents(filepath)  # 清空exportData.xls文件

    def test_import_qa(self):
        # 全量导入问答
        url = get_url(
            section_dict["data_file"], section_dict["sheet_name5"], "import_qa"
        )
        file_path = "../data/import_qa.xlsx"
        files = {"file": (open(file_path, "rb"))}
        response_import = requests.post(
            url=url, files=files, headers={"Cookie": self.Cookie}
        )  # 请求全量导入接口
        # 断言
        jsonData_1 = response_import.json()
        actual_res_1 = jsonData_1["data"]["total"]
        response_search = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "查询导入问答",
            headers=self.headers,
        )  # 请求查询接口
        jsonData_2 = response_search.json()
        actual_res_2 = str(jsonData_2["data"]["paginate"]["data"][1]["question"])
        expect_res = get_expect_res_text(
            section_dict["data_file"], section_dict["sheet_name5"], "import_qa"
        )
        self.assertEqual(9, actual_res_1)  # 使用导入接口返回数据中的total字段值断言
        self.assertEqual(expect_res, actual_res_2)  # 使用查询到的所有问答中的最后一个问答的问题进行断言

    def test_ext_import_qa(self):
        # 导入拓展问
        url = get_url(
            section_dict["data_file"], section_dict["sheet_name5"], "ext-import_qa"
        )
        file_path = "../data/ext-import.xlsx"
        files = {"file": (open(file_path, "rb"))}
        requests.post(
            url=url, files=files, headers={"Cookie": self.Cookie}
        )  # 请求拓展问导入接口
        # 断言
        response_search = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "查询导入问答",
            headers=self.headers,
        )  # 请求查询接口
        jsonData = response_search.json()
        actual_res = str(jsonData["data"]["paginate"]["data"][0]["question"])
        expect_res = get_expect_res_text(
            section_dict["data_file"], section_dict["sheet_name5"], "ext-import_qa"
        )
        self.assertEqual(expect_res, actual_res)

    def test_custom_import_type1(self):
        # 自定义导入，覆盖问答
        url = get_url(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "custom_import_type1",
        )
        data = get_request_data(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "custom_import_type1",
        )
        file_path = "../data/custom-import_1.xlsx"
        files = {"file": (open(file_path, "rb"))}
        requests.post(
            url=url, data=data, files=files, headers={"Cookie": self.Cookie}
        )  # 请求自定义导入接口
        # 断言
        response_search = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "查询导入问答",
            headers=self.headers,
        )  # 请求查询接口
        jsonData = response_search.json()
        actual_res = str(jsonData["data"]["paginate"]["data"][0]["answer"])
        expect_res = get_expect_res_text(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "custom_import_type1",
        )
        self.assertEqual(expect_res, actual_res)

    # 自定义导入，追加问答
    def test_custom_import_type2(self):
        url = get_url(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "custom_import_type1",
        )
        data = get_request_data(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "custom_import_type2",
        )
        file_path = "../data/custom-import_2.xlsx"
        files = {"file": (open(file_path, "rb"))}
        requests.post(
            url=url, data=data, files=files, headers={"Cookie": self.Cookie}
        )  # 请求自定义导入接口
        # 断言
        response_search = my_get(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "查询导入问答",
            headers=self.headers,
        )  # 请求查询接口
        jsonData = response_search.json()
        actual_res = str(jsonData["data"]["paginate"]["data"][8]["answer"])
        expect_res = get_expect_res_text(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "custom_import_type2",
        )
        # 删除问答
        delete_words_qa(
            section_dict["data_file"],
            section_dict["sheet_name5"],
            "批量删除-获取ids",
            "mul_delete_qa",
        )
        self.assertEqual(expect_res, actual_res)

    def test_down_result(self):
        # 全量导入问答
        url_import = get_url(
            section_dict["data_file"], section_dict["sheet_name5"], "import_qa"
        )
        file_path = "../data/import_qa.xlsx"
        files = {"file": (open(file_path, "rb"))}
        response_import = requests.post(
            url=url_import, files=files, headers={"Cookie": self.Cookie}
        )  # 请求全量导入接口
        jsonData = response_import.json()
        file_name = jsonData["data"]["name"]  # 获取导入结果文件名

        # 下载导入结果文件
        url = get_url(
            section_dict["data_file"], section_dict["sheet_name5"], "down_result"
        )
        url_down_result = url + file_name  # 拼接url
        response_down_result = requests.get(url=url_down_result, headers=self.headers)

        # 将文件的数据写入excel文件
        filepath = "../data/down_result.xlsx"
        with open(filepath, "wb") as file:
            file.write(response_down_result.content)
        actual_res = excel_to_list("../data/down_result.xlsx", "sheet1")  # 导出文件数据

        # 断言
        expect_res = get_expect_res_text(
            section_dict["data_file"], section_dict["sheet_name5"], "down_result"
        )
        self.assertEqual(expect_res, str(actual_res))
        # 清空文件
        clear_excel_contents(filepath)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestQA('test_new_qa'))
    suite.addTest(TestQA('test_export_qa'))
    suite.addTest(TestQA('test_edit_qa'))
    suite.addTest(TestQA('test_check_relation'))
    suite.addTest(TestQA('test_mul_qa_close'))
    suite.addTest(TestQA('test_mul_qa_open'))
    suite.addTest(TestQA('test_mul_qa_range'))
    suite.addTest(TestQA('test_mul_qa_label'))
    suite.addTest(TestQA('test_mul_check'))
    suite.addTest(TestQA('test_close_qa'))
    suite.addTest(TestQA('test_open_qa'))
    suite.addTest(TestQA('test_delete_qa'))
    suite.addTest(TestQA('test_import_qa'))
    suite.addTest(TestQA('test_ext_import_qa'))
    suite.addTest(TestQA('test_custom_import_type1'))
    suite.addTest(TestQA('test_custom_import_type2'))
    suite.addTest(TestQA('test_down_result'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
