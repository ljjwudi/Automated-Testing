import time
import unittest
from common.common_api import delete_words_qa, clear_excel_contents, log_case_info
from common.get_data_excel import *
from common.ApiTest import *


class TestSynonymWords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次
        # cls.logger = setup_logging()
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
    def test_search_by_word(self):
        # 请求查询接口
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "search_by_word",
            headers=self.headers,
        )
        actual_res = res.json()  # 获取实际结果
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name6"], "search_by_word"
        )
        # 日志
        log_case_info("test_search_by_word", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 通过词集名称查询
    def test_search_by_name(self):
        # 请求查询接口
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "search_by_word",
            headers=self.headers,
        )
        actual_res = res.json()  # 获取实际结果
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name6"], "search_by_name"
        )
        # 日志
        log_case_info("test_search_by_name", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 通过话术查询
    def test_search_by_project(self):
        # 请求查询接口
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "search_by_project",
            headers=self.headers,
        )
        actual_res = res.json()  # 获取实际结果
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name6"], "search_by_project"
        )
        # 日志
        log_case_info("test_search_by_project", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 新建同义词
    def test_new_synonym_words(self):
        # 请求新建接口
        my_post(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "new_synonym_words",
            headers=self.headers,
        )
        time.sleep(1)
        # 查询新建的同义词
        res_search = my_get(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "验证新建同义词",
            headers=self.headers,
        )
        jsonData = res_search.json()
        actual_res = jsonData["data"]["paginate"]["data"][0]["dict_content"]

        # 删除同义词
        ids = jsonData["data"]["paginate"]["data"][0]["id"]  # 获取id
        data = {"ids": [ids]}
        url = get_url(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "mul_delete_synonym_words",
        )
        requests.post(url=url, data=json.dumps(data), headers=self.headers)
        # 获取预期结果
        expect_res = get_expect_res_text(
            section_dict["data_file"], section_dict["sheet_name6"], "new_synonym_words"
        )
        # 日志
        log_case_info("test_new_synonym_words", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, str(actual_res))

    # 删除同义词
    def test_delete_synonym_words(self):
        # 新建一个同义词
        my_post(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "new_synonym_words",
            headers=self.headers,
        )
        time.sleep(1)
        # 查询新建的同义词
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "验证新建同义词",
            headers=self.headers,
        )
        jsonData = res.json()
        # 删除同义词
        word_id = str(jsonData["data"]["paginate"]["data"][0]["id"])  # 获取id
        part_url = get_url(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "delete_synonym_words",
        )
        url = part_url + word_id
        requests.delete(url=url, headers=self.headers)  # 请求删除接口
        # 删除后查询词集
        del_res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "验证新建同义词",
            headers=self.headers,
        )
        # 实际结果
        actual_res = del_res.json()
        # 预期结果
        expect_res = get_expect_res(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "delete_synonym_words",
        )
        # 日志
        log_case_info("test_delete_synonym_words", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 导入同义词
    def test_import_synonym_words(self):
        url_import = get_url(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "import_synonym_words",
        )
        file_path = "../data/synonym-similar.xlsx"
        files = {"file": (open(file_path, "rb"))}
        res_import = requests.post(
            url=url_import, files=files, headers={"Cookie": self.Cookie}
        )  # 请求导入接口
        jsonData_import = res_import.json()

        task_id = jsonData_import["data"]
        url_status = get_url(
            section_dict["data_file"], section_dict["sheet_name6"], "import_status"
        )
        status = 0
        while status != 3:
            res = requests.get(
                url=url_status, data=json.dumps(task_id), headers=self.headers
            )
            res_status = res.json()
            status = res_status["data"]["status"]
            time.sleep(5)
        # 查询是否导入成功
        res_search = my_get(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "同义词导入验证",
            headers=self.headers,
        )  # 请求查询接口
        jsonData_search = res_search.json()

        actual_res_name = str(jsonData_search["data"]["paginate"]["data"][9]["name"])
        actual_res_total = jsonData_search["data"]["paginate"]["total"]

        expect_res = get_expect_res_text(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "import_synonym_words",
        )
        # 删除导入的词集
        delete_words_qa(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "获取id列表",
            "mul_delete_synonym_words",
        )
        # 日志
        log_case_info("test_import_synonym_words", expect_res, actual_res_name)
        log_case_info("test_delete_synonym_words", 10, actual_res_total)
        # 断言
        self.assertEqual(10, actual_res_total)  # 使用total字段值断言
        self.assertEqual(expect_res, actual_res_name)  # 使用查询到的所有问答中的最后一个问答的问题进行断言

    # 查询同义词导入状态
    def test_import_status(self):
        # 导入同义词
        url_import = get_url(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "import_synonym_words",
        )
        file_path = "../data/synonym-similar-error.xlsx"
        files = {"file": (open(file_path, "rb"))}
        res_import = requests.post(
            url=url_import, files=files, headers={"Cookie": self.Cookie}
        )  # 请求导入接口
        jsonData_import = res_import.json()

        data = jsonData_import["data"]
        task_id = jsonData_import["data"]["task_id"]
        url_status = get_url(
            section_dict["data_file"], section_dict["sheet_name6"], "import_status"
        )
        status = 0
        while status != 3:
            res = requests.get(
                url=url_status, data=json.dumps(data), headers=self.headers
            )
            res_status = res.json()
            status = res_status["data"]["status"]
            time.sleep(5)
        expect_res_taskId = res_status["data"]["task_id"]
        expect_res_total = res_status["data"]["total"]
        expect_res_error = res_status["data"]["error"]
        # 日志
        log_case_info("test_import_status", 10, expect_res_total)
        log_case_info("test_import_status", 10, expect_res_error)
        # 断言
        self.assertEqual(
            task_id, expect_res_taskId
        )  # 通过task_id字段断言，判断状态查询接口返回的任务id是否正确
        self.assertEqual(10, expect_res_total)  # 通过导入总数断言
        self.assertEqual(10, expect_res_error)  # 通过导入失败数断言

    # 下载导入报告
    def test_down_result(self):
        # 导入同义词
        url_import = get_url(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "import_synonym_words",
        )
        file_path = "../data/synonym-similar-error.xlsx"
        files = {"file": (open(file_path, "rb"))}
        res_import = requests.post(
            url=url_import, files=files, headers={"Cookie": self.Cookie}
        )  # 请求导入接口
        jsonData_import = res_import.json()
        data = jsonData_import["data"]
        task_id = jsonData_import["data"]["task_id"]
        url_status = get_url(
            section_dict["data_file"], section_dict["sheet_name6"], "import_status"
        )
        status = 0
        while status != 3:
            res = requests.get(
                url=url_status, data=json.dumps(data), headers=self.headers
            )
            res_status = res.json()
            status = res_status["data"]["status"]
            time.sleep(5)
        url_down_result = (
                get_url(
                    section_dict["data_file"], section_dict["sheet_name6"], "down_result"
                )
                + task_id
        )
        res_down_result = requests.get(url=url_down_result, headers=self.headers)
        # 将导出文件的数据写入excel文件
        filepath = "../data/synonym-words-down-result.xlsx"
        with open(filepath, "wb") as file:
            file.write(res_down_result.content)
        # 读取文件内容
        actual_res = excel_to_list("../data/synonym-words-down-result.xlsx", "sheet1")
        # 获取预期结果
        expect_res = get_expect_res_text(
            section_dict["data_file"], section_dict["sheet_name6"], "down_result"
        )
        # 清除文件内容
        clear_excel_contents("../data/synonym-words-down-result.xlsx")
        # 日志
        log_case_info("test_down_result", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, str(actual_res))

    # 获取id列表
    def test_get_query_ids(self):
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "get_query_ids",
            headers=self.headers,
        )
        # 实际结果
        actual_res = res.json()
        # 预期结果
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name6"], "get_query_ids"
        )
        # 日志
        log_case_info("test_get_query_ids", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 导出同义词
    def test_export_words(self):
        res = my_post(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "export_words",
            headers=self.headers,
        )
        # 将导出文件的数据写入excel文件
        filepath = "../data/export-SynonymWords.xlsx"
        with open(filepath, "wb") as file:
            file.write(res.content)
        # 读取文件内容
        actual_res = excel_to_list("../data/export-SynonymWords.xlsx", "Worksheet")
        # 获取预期结果
        expect_res = get_expect_res_text(
            section_dict["data_file"], section_dict["sheet_name6"], "export_words"
        )
        # 清除文件内容
        clear_excel_contents(filepath)
        # 日志
        log_case_info("test_export_words", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, str(actual_res))

    # 检查同名词集
    def test_check_dict_name(self):
        res = my_post(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "check_dict_name",
            headers=self.headers,
        )

        # 实际结果
        actual_res = res.json()
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name6"], "check_dict_name"
        )
        # 日志
        log_case_info("test_check_dict_name", expect_res, actual_res)
        # 断言
        self.assertEqual(actual_res, expect_res)

    # 批量词集名称检测
    def test_mul_check_name(self):
        res = my_post(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "multi_check_name",
            headers=self.headers,
        )
        # 实际结果
        actual_res = res.json()
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name6"], "multi_check_name"
        )
        # 日志
        log_case_info("test_mul_check_name", expect_res, actual_res)
        # 断言
        self.assertEqual(actual_res, expect_res)

    # 同义词筛选视图
    def test_screening_view(self):
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "screening_view",
            headers=self.headers,
        )
        # 实际结果
        actual_res = res.json()
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name6"], "screening_view"
        )
        # 日志
        log_case_info("test_screening_view", expect_res, actual_res)
        # 断言
        self.assertEqual(actual_res, expect_res)

    # 导出筛选视图词集
    def test_screening_view_export(self):
        res = my_post(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "screening_view_export",
            headers=self.headers,
        )
        # 将导出数据从二进制转换成中文
        content = res.content.decode("utf-8-sig")
        expect_res = get_expect_res_text(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "screening_view_export",
        )
        # 日志
        log_case_info("test_screening_view_export", expect_res, content)
        # 断言
        self.assertEqual(expect_res, content)

    # 检查所选词集是否重名
    def test_check_same_name(self):
        # 请求接口
        res = my_post(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "check_same_name",
            headers=self.headers,
        )
        actual_res = res.json()
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name6"], "check_same_name"
        )
        # 日志
        log_case_info("test_check_same_name", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 获取词集关联流程树
    def test_get_dictionary_projects(self):
        # 请求接口
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "get_dictionary_projects",
            headers=self.headers,
        )
        actual_res = res.text
        # 获取预期结果
        expect_res = get_expect_res_text(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "get_dictionary_projects",
        )
        # 日志
        log_case_info("test_get_dictionary_projects", expect_res, actual_res)
        # 断言
        self.assertIn(expect_res, actual_res)

    # 获取名称数组同名数量
    def test_words_count(self):
        # 请求接口
        res = my_post(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "words_count",
            headers=self.headers,
        )
        actual_res = res.json()
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name6"], "words_count"
        )
        # 日志
        log_case_info("test_words_count", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 批量复制同义词
    def test_mul_copy(self):
        # 请求接口
        my_post(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "mul_copy",
            headers=self.headers,
        )
        # 获取预期结果
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name6"], "mul_copy"
        )
        # 查询复制的词集
        res_search = my_get(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "查询验证批量复制",
            headers=self.headers,
        )
        # 将词集名称放入列表中作为断言的实际结果
        jsonData = res_search.json()
        words_name_1 = jsonData["data"]["paginate"]["data"][0]["name"]
        words_name_2 = jsonData["data"]["paginate"]["data"][1]["name"]
        words_name_3 = jsonData["data"]["paginate"]["data"][2]["name"]
        actual_res = [words_name_1, words_name_2, words_name_3]
        # 删除所复制的同义词
        delete_words_qa(
            section_dict["data_file"],
            section_dict["sheet_name6"],
            "获取复制词集的id列表",
            "mul_delete_synonym_words",
        )
        # 日志
        log_case_info("test_mul_copy", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 该功能已停用
    # 创建迁移-移动至通用
    # def test_duplicate_move_task_1(self):
    #     # 创建同义词
    #     my_post(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "新建同义词-创建迁移-移动至通用",
    #         headers=self.headers,
    #     )
    #     time.sleep(1)
    #
    #     # 查询新建的同义词
    #     res_search = my_get(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "验证新建同义词",
    #         headers=self.headers,
    #     )
    #     jsonData = res_search.json()
    #     # 迁移至通用
    #     url_move = get_url(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "duplicate_move_task_1",
    #     )
    #     ids_move = jsonData["data"]["paginate"]["data"][0]["id"]  # 获取id
    #     data_move = {"type": "1", "ids": [ids_move]}
    #     res_move = requests.post(
    #         url=url_move, data=json.dumps(data_move), headers=self.headers
    #     )
    #     jsonData_move = res_move.json()
    #     task_id = jsonData_move["data"]
    #     data = {"task_id": task_id}
    #     status = 0
    #     url_state = get_url(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "duplicate_move_task_state",
    #     )
    #
    #     # 检查创建迁移状态，status为2时即迁移成功，才继续往下执行接口
    #     try:
    #         while status != 2:
    #             res_state = requests.get(
    #                 url=url_state, data=json.dumps(data), headers=self.headers
    #             )
    #             jsonData_state = res_state.json()
    #             status = jsonData_state["data"]["status"]
    #             time.sleep(5)
    #     except Exception as e:
    #         self.logger.info(f"test_duplicate_move_task_1\t迁移异常:{e}")
    #         # 若迁移失败，删除未迁移的同义词
    #         data_del = {"ids": [ids_move]}
    #         url = get_url(
    #             section_dict["data_file"],
    #             section_dict["sheet_name6"],
    #             "mul_delete_synonym_words",
    #         )
    #         requests.post(url=url, data=json.dumps(data_del), headers=self.headers)
    #     # 迁移后查询
    #     res_move_search = my_get(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "验证新建同义词",
    #         headers=self.headers,
    #     )
    #     # 实际结果
    #     jsonData_move_search = res_move_search.json()
    #     actual_res = jsonData_move_search["data"]["paginate"]["data"][0]["project_id"]
    #     # 预期结果
    #     expect_res = 0  # 通用词集的id为0
    #     # 删除迁移后同义词
    #     ids_del = jsonData_move_search["data"]["paginate"]["data"][0]["id"]  # 获取id
    #     data_del = {"ids": [ids_del]}
    #     url = get_url(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "mul_delete_synonym_words",
    #     )
    #     requests.post(url=url, data=json.dumps(data_del), headers=self.headers)
    #     # 日志
    #     log_case_info("test_duplicate_move_task_1", expect_res, actual_res)
    #     # 断言
    #     self.assertEqual(expect_res, actual_res)

    # 该功能已停用
    # 创建迁移-同步至其他流程
    # def test_duplicate_move_task_2(self):
    #     # 创建同义词
    #     my_post(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "新建同义词-创建迁移-同步至其他流程",
    #         headers=self.headers,
    #     )
    #     time.sleep(1)
    #
    #     # 查询新建的同义词
    #     res_search = my_get(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "验证新建同义词",
    #         headers=self.headers,
    #     )
    #     jsonData = res_search.json()
    #     # 同步至其他流程树
    #     url_move = get_url(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "duplicate_move_task_2",
    #     )
    #     ids_move = jsonData["data"]["paginate"]["data"][0]["id"]  # 获取id
    #     data_move = {
    #         "type": "2",
    #         "ids": [ids_move],
    #         "project_id": "901014",
    #         "duplicate_name_deal": "2",
    #     }
    #     res_move = requests.post(
    #         url=url_move, data=json.dumps(data_move), headers=self.headers
    #     )
    #     jsonData_move = res_move.json()
    #     task_id = jsonData_move["data"]
    #     data = {"task_id": task_id}
    #     status = 0
    #     url_state = get_url(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "duplicate_move_task_state",
    #     )
    #
    #     # 检查创建迁移状态，status为2时即迁移成功，才继续往下执行接口
    #     try:
    #         while status != 2:
    #             res_state = requests.get(
    #                 url=url_state, data=json.dumps(data), headers=self.headers
    #             )
    #             jsonData_state = res_state.json()
    #             status = jsonData_state["data"]["status"]
    #             time.sleep(5)
    #     except Exception as e:
    #         self.logger.info(f"test_duplicate_move_task_2\t迁移异常:{e}")
    #         # 删除未迁移的同义词
    #         data_del = {"ids": [ids_move]}
    #         url = get_url(
    #             section_dict["data_file"],
    #             section_dict["sheet_name6"],
    #             "mul_delete_synonym_words",
    #         )
    #         requests.post(url=url, data=json.dumps(data_del), headers=self.headers)
    #     # 迁移后查询
    #     res_move_search = my_get(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "验证新建同义词",
    #         headers=self.headers,
    #     )
    #     # 实际结果
    #     jsonData_move_search = res_move_search.json()
    #     project_name_move = jsonData_move_search["data"]["paginate"]["data"][0][
    #         "project_name"
    #     ]
    #     project_name_new = jsonData_move_search["data"]["paginate"]["data"][1][
    #         "project_name"
    #     ]
    #     actual_res = [project_name_move, project_name_new]
    #     # 预期结果
    #     expect_res = get_expect_res(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "duplicate_move_task_2",
    #     )
    #     # 删除迁移后同义词
    #     ids_del_0 = jsonData_move_search["data"]["paginate"]["data"][0]["id"]  # 获取id
    #     ids_del_1 = jsonData_move_search["data"]["paginate"]["data"][1]["id"]  # 获取id
    #     data_del = {"ids": [ids_del_0, ids_del_1]}
    #     url = get_url(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "mul_delete_synonym_words",
    #     )
    #     requests.post(url=url, data=json.dumps(data_del), headers=self.headers)
    #     # 日志
    #     log_case_info("test_duplicate_move_task_2", expect_res, actual_res)
    #     # 断言
    #     self.assertEqual(expect_res, actual_res)

    # 该功能已停用
    # 下载创建迁移报告
    # def test_duplicate_move_task_report(self):
    #     # 创建同义词
    #     my_post(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "新建同义词-创建迁移-同步至其他流程",
    #         headers=self.headers,
    #     )
    #     time.sleep(1)
    #
    #     # 查询新建的同义词
    #     res_search = my_get(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "验证新建同义词",
    #         headers=self.headers,
    #     )
    #     jsonData = res_search.json()
    #     # 迁移至通用
    #     url_move = get_url(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "duplicate_move_task_1",
    #     )
    #     ids_move = jsonData["data"]["paginate"]["data"][0]["id"]  # 获取id
    #     data_move = {"type": "1", "ids": [ids_move]}
    #     res_move = requests.post(
    #         url=url_move, data=json.dumps(data_move), headers=self.headers
    #     )
    #     jsonData_move = res_move.json()
    #     task_id = jsonData_move["data"]
    #     data = {"task_id": task_id}
    #     status = 0
    #     url_state = get_url(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "duplicate_move_task_state",
    #     )
    #     report_path = None
    #     # 检查创建迁移状态，status为2时即迁移成功，才继续往下执行接口
    #     try:
    #         while status != 2:
    #             res_state = requests.get(
    #                 url=url_state, data=json.dumps(data), headers=self.headers
    #             )
    #             jsonData_state = res_state.json()
    #             status = jsonData_state["data"]["status"]
    #             report_path = jsonData_state["data"]["report_path"]
    #             time.sleep(5)
    #     except Exception as e:
    #         self.logger.info(f"test_duplicate_move_task_report\t迁移异常:{e}")
    #         # 删除未迁移的同义词
    #         data_del = {"ids": [ids_move]}
    #         url = get_url(
    #             section_dict["data_file"],
    #             section_dict["sheet_name6"],
    #             "mul_delete_synonym_words",
    #         )
    #         requests.post(url=url, data=json.dumps(data_del), headers=self.headers)
    #     # 下载报告请求参数,url
    #     url_download = get_url(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "duplicate_move_task_report",
    #     )
    #     data_download = {"report_path": report_path}
    #     print(data_download)
    #     # 下载报告
    #     res_download = requests.get(
    #         url=url_download, data=json.dumps(data_download), headers=self.headers
    #     )
    #     actual_res = res_download.content.decode("gbk", errors="ignore")
    #     # 预期结果
    #     expect_res = get_expect_res_text(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "duplicate_move_task_report",
    #     )
    #     # 删除迁移后同义词
    #     res_move_search = my_get(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "验证新建同义词",
    #         headers=self.headers,
    #     )
    #     jsonData_move_search = res_move_search.json()
    #     ids_del = jsonData_move_search["data"]["paginate"]["data"][0]["id"]  # 获取id
    #     data_del = {"ids": [ids_del]}
    #     url = get_url(
    #         section_dict["data_file"],
    #         section_dict["sheet_name6"],
    #         "mul_delete_synonym_words",
    #     )
    #     requests.post(url=url, data=json.dumps(data_del), headers=self.headers)
    #     # 日志
    #     log_case_info("test_duplicate_move_task_report", expect_res, actual_res)
    #     # 断言
    #     self.assertEqual(expect_res, str(actual_res))
