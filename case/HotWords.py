import time
import unittest

from common.common_api import delete_words_qa, clear_excel_contents
from common.log import setup_logging
from common.get_data_excel import *
from common.ApiTest import *


class TestHotWords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次
        cls.logger = setup_logging()
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

    # 通过词集内容查询
    def test_search_hotWords_by_words(self):
        # 请求查询接口
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "search_hotWords_by_words",
            headers=self.headers,
        )
        # 获取实际结果
        actual_res = res.json()
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "search_hotWords_by_words",
        )
        # 日志
        self.logger.info(f"search_hotWords_by_words\t{res.text}")
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 通过词集名称查询
    def test_search_hotWords_by_name(self):
        # 请求查询接口
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "search_hotWords_by_name",
            headers=self.headers,
        )
        # 获取实际结果
        actual_res = res.json()
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "search_hotWords_by_name",
        )
        # 日志
        self.logger.info(f"search_hotWords_by_name\t{res.text}")
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 通过话术流程查询
    def test_search_hotWords_by_project(self):
        # 请求查询接口
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "search_hotWords_by_project",
            headers=self.headers,
        )
        actual_res = res.json()  # 获取实际结果
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "search_hotWords_by_project",
        )
        # 日志
        self.logger.info(f"search_hotWords_by_project\t{res.text}")
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 查询范围为热词
    def test_search_combination_hotWords(self):
        # 请求查询接口
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "search_combination_hotWords",
            headers=self.headers,
        )
        actual_res = res.json()  # 获取实际结果
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "search_combination_hotWords",
        )
        # 日志
        self.logger.info(f"search_combination_hotWords\t{res.text}")
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 查询范围为替换词
    def test_search_combination_replaceWords(self):
        # 请求查询接口
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "search_combination_replaceWords",
            headers=self.headers,
        )
        actual_res = res.json()  # 获取实际结果
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "search_combination_replaceWords",
        )
        # 日志
        self.logger.info(f"search_combination_replaceWords\t{res.text}")
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 筛选出包含替换词的热词
    def test_search_by_have_replaceWords(self):
        # 请求查询接口
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "search_by_have_replaceWords",
            headers=self.headers,
        )
        actual_res = res.json()  # 获取实际结果
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "search_by_have_replaceWords",
        )
        # 日志
        self.logger.info(f"search_by_have_replaceWords\t{res.text}")
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 筛选出不包含替换词的热词
    def test_search_by_without_replaceWords(self):
        # 请求查询接口
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "search_by_without_replaceWords",
            headers=self.headers,
        )
        actual_res = res.json()  # 获取实际结果
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "search_by_without_replaceWords",
        )
        # 日志
        self.logger.info(f"search_by_without_replaceWords\t{res.text}")
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 新建热词
    def test_new_hotWords(self):
        # 请求新建接口
        res_new = my_post(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "new_hotWords",
            headers=self.headers,
        )
        # 日志
        self.logger.info(f"test_new_hotWords\t{res_new.text}")
        time.sleep(1)
        # 查询新建的热词
        res_search = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "验证新建热词",
            headers=self.headers,
        )
        # 日志
        self.logger.info(f"new_hotWords\t{res_search.text}")
        # 实际结果
        jsonData = res_search.json()
        actual_res = jsonData["data"]["paginate"]["data"][0]["name"]
        # 删除热词
        ids = jsonData["data"]["paginate"]["data"][0]["id"]  # 获取id
        data = {"ids": [ids]}
        url = get_url(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "mul_delete_hotWords",
        )
        requests.post(url=url, data=json.dumps(data), headers=self.headers)
        # 获取预期结果
        expect_res = get_expect_res_text(
            section_dict["data_file"], section_dict["sheet_name8"], "new_hotWords"
        )
        # 断言
        self.assertEqual(expect_res, str(actual_res))

    # 删除热词
    def test_delete_hotWords(self):
        # 新建一个热词
        my_post(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "new_hotWords",
            headers=self.headers,
        )
        time.sleep(1)
        # 查询新建的热词
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "验证新建热词",
            headers=self.headers,
        )
        jsonData = res.json()
        self.logger.info(f"delete_hotWords\t{res.text}")
        # 删除热词
        word_id = str(jsonData["data"]["paginate"]["data"][0]["id"])  # 获取id
        part_url = get_url(
            section_dict["data_file"], section_dict["sheet_name8"], "delete_hotWords"
        )
        url = part_url + word_id
        requests.delete(url=url, headers=self.headers)  # 请求删除接口
        # 删除后查询词集
        del_res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "验证新建热词",
            headers=self.headers,
        )
        actual_res = del_res.json()
        self.logger.info(f"delete_hotWords\t{del_res.text}")
        # 断言
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name8"], "delete_hotWords"
        )
        self.assertEqual(expect_res, actual_res)

    # 批量删除热词
    def test_mul_delete_hotWords(self):
        # 新建一个热词
        my_post(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "new_hotWords",
            headers=self.headers,
        )
        time.sleep(1)
        # 查询新建的热词
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "验证新建热词",
            headers=self.headers,
        )
        jsonData = res.json()
        self.logger.info(f"mul_delete_hotWords\t{res.text}")
        # 删除热词
        ids = str(jsonData["data"]["paginate"]["data"][0]["id"])  # 获取id
        url = get_url(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "mul_delete_hotWords",
        )
        data = {"ids": [ids]}
        mul_delete_res = requests.post(
            url=url, data=json.dumps(data), headers=self.headers
        )  # 请求批量删除接口
        self.logger.info(f"mul_delete_hotWords\t{mul_delete_res.text}")
        # 删除后查询词集
        del_res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "验证新建热词",
            headers=self.headers,
        )
        actual_res = del_res.json()
        self.logger.info(f"mul_delete_hotWords\t{del_res.text}")
        # 断言
        expect_res = get_expect_res(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "mul_delete_hotWords",
        )
        self.assertEqual(expect_res, actual_res)

    # 检查同名词集
    def test_check_hotWords_dict_name(self):
        res = my_post(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "check_hotWords_dict_name",
            headers=self.headers,
        )
        # 日志
        self.logger.info(f"check_hotWords_dict_name\t{res.text}")
        # 实际结果
        actual_res = res.json()
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "check_hotWords_dict_name",
        )
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 获取id列表
    def test_hotWords_query_ids(self):
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "hotWords_query_ids",
            headers=self.headers,
        )
        # 日志
        self.logger.info(f"test_hotWords_query_ids\t{res.text}")
        actual_res = res.json()
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name8"], "hotWords_query_ids"
        )
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 复制热词
    def test_copy_hotWords(self):
        # 请求接口
        res_copy = my_post(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "copy_hotWords",
            headers=self.headers,
        )
        # 日志
        self.logger.info(f"test_copy_hotWords\t{res_copy.text}")
        time.sleep(0.5)
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name8"], "copy_hotWords"
        )
        # 查询复制的词集
        res_search = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "验证复制热词",
            headers=self.headers,
        )
        # 日志
        self.logger.info(f"test_copy_hotWords\t{res_search.text}")
        # 将词集名称放入列表中作为断言的实际结果
        jsonData = res_search.json()
        words_name = jsonData["data"]["paginate"]["data"][0]["name"]
        project_id = jsonData["data"]["paginate"]["data"][0]["project_id"]
        actual_res = [words_name, project_id]
        # 删除所复制的热词
        delete_words_qa(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "获取复制词集的id",
            "mul_delete_hotWords",
        )
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 编辑热词
    def test_edit_hotWords(self):
        # 请求新建接口
        res_new = my_post(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "new_hotWords",
            headers=self.headers,
        )
        # 日志
        self.logger.info(f"test_edit_hotWords\t{res_new.text}")
        time.sleep(1)
        # 查询新建的热词
        res_search_new = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "验证新建热词",
            headers=self.headers,
        )
        res_search_new_json = res_search_new.json()
        new_id = res_search_new_json["data"]["paginate"]["data"][0]["id"]
        # 获取请求参数
        data = get_request_data(
            section_dict["data_file"], section_dict["sheet_name8"], "edit_hotWords"
        )
        data["id"] = new_id
        url = get_url(
            section_dict["data_file"], section_dict["sheet_name8"], "edit_hotWords"
        )
        # 请求编辑接口
        requests.post(url=url, data=json.dumps(data), headers=self.headers)
        # 预期结果
        res_search_edit = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "验证编辑热词",
            headers=self.headers,
        )
        self.logger.info(f"test_edit_hotWords\t{res_search_edit.text}")
        res_search_edit_json = res_search_edit.json()
        edit_id = res_search_edit_json["data"]["paginate"]["data"][0]["id"]
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name8"], "edit_hotWords"
        )
        expect_res["data"]["paginate"]["data"][0]["id"] = edit_id
        # 实际结果
        actual_res = res_search_edit_json
        # 删除编辑后词集
        url_del = get_url(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "mul_delete_hotWords",
        )
        data_del = {"ids": [edit_id]}
        requests.post(url=url_del, data=json.dumps(data_del), headers=self.headers)
        # 断言
        self.assertEqual(actual_res, expect_res)

    # 导出热词
    def test_export_hotWords(self):
        res = my_post(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "export_hotWords",
            headers=self.headers,
        )
        # 日志
        self.logger.info(f"test_export_hotWords\t{res.content}")
        # 将导出文件的数据写入excel文件
        filepath = "../data/export_hotWords.xlsx"
        with open(filepath, "wb") as file:
            file.write(res.content)
        # 读取文件内容
        actual_res = excel_to_list(filepath, "Worksheet")
        # 获取预期结果
        expect_res = get_expect_res_text(
            section_dict["data_file"], section_dict["sheet_name8"], "export_hotWords"
        )
        # 清除文件内容
        clear_excel_contents(filepath)
        # 断言
        self.assertEqual(expect_res, str(actual_res))

    # 导入热词
    def test_import_hotWords(self):
        # 导入热词
        url_import = get_url(
            section_dict["data_file"], section_dict["sheet_name8"], "import_hotWords"
        )
        file_path = "../data/import_hotWords.xlsx"
        files = {"file": (open(file_path, "rb"))}
        requests.post(
            url=url_import, files=files, headers={"Cookie": self.Cookie}
        )  # 请求导入接口
        # 查询是否导入成功
        res_search = my_get(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "热词导入验证",
            headers=self.headers,
        )  # 请求查询接口
        self.logger.info(f"test_import_hotWords\t{res_search.text}")
        # 实际结果
        jsonData_search = res_search.json()
        name = str(jsonData_search["data"]["paginate"]["data"][8]["name"])
        total = jsonData_search["data"]["paginate"]["total"]
        actual_res = {"name": name, "total": total}
        # 预期结果
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name8"], "import_hotWords"
        )
        # 删除导入的词集
        delete_words_qa(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "删除导入的词集",
            "mul_delete_hotWords",
        )
        self.assertEqual(expect_res, actual_res)

    # 下载导入热词结果报告
    def test_down_result_hotWords(self):
        # 导入热词
        url_import = get_url(
            section_dict["data_file"], section_dict["sheet_name8"], "import_hotWords"
        )
        file_path = "../data/import_hotWords.xlsx"
        files = {"file": (open(file_path, "rb"))}
        res = requests.post(
            url=url_import, files=files, headers={"Cookie": self.Cookie}
        )
        # 获取结果文件名
        res_json = res.json()
        file_name = res_json["data"]["name"]
        # 下载结果报告
        data = {"filename": file_name}
        url = get_url(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "down_result_hotWords",
        )
        res_down_result = requests.get(
            url=url, data=json.dumps(data), headers=self.headers
        )
        # 将导出文件的数据写入excel文件
        filepath = "../data/down_result_hotWords.xlsx"
        with open(filepath, "wb") as file:
            file.write(res_down_result.content)
        # 预期结果
        actual_res = excel_to_list(filepath, "sheet1")
        # 实际结果
        expect_res = get_expect_res_text(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "down_result_hotWords",
        )
        # 删除导入的词集
        delete_words_qa(
            section_dict["data_file"],
            section_dict["sheet_name8"],
            "删除导入的词集",
            "mul_delete_hotWords",
        )
        self.assertEqual(expect_res, str(actual_res))

