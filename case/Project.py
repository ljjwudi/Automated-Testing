import time
import unittest
from common.common_api import delete_project, search_project, log_case_info
from common.get_data_excel import *
from common.ApiTest import *


class TestProject(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次
        # cls.logger = setup_logging()
        # 获取Cookie
        default_dict = read_section_key_value_dict("../config/config.ini", "default")
        cls.Cookie = default_dict["cookie"]
        cls.headers = {"Cookie": default_dict["cookie"], "Content-Type": "application/json"}
        cls.section_dict = read_section_key_value_dict("../config/config.ini", "data_path")

    # 通过名称查询流程树
    def test_search_project_byName(self):
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "search_project_byName",
            headers=self.headers,
        )
        # 实际结果
        actual_res = res.json()
        # 预期结果
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name9"], "search_project_byName"
        )
        # 日志
        log_case_info("test_search_project_byName", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 通过Id查询流程树
    def test_search_project_byId(self):
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "search_project_byId",
            headers=self.headers,
        )
        # 实际结果
        actual_res = res.json()
        # 预期结果
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name9"], "search_project_byId"
        )
        # 日志
        log_case_info("test_search_project_byId", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 通过归属人查询流程树
    def test_search_project_byBelongers(self):
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "search_project_byBelongers",
            headers=self.headers,
        )
        # 实际结果
        actual_res = res.json()
        # 预期结果
        expect_res = get_expect_res(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "search_project_byBelongers",
        )
        # 日志
        log_case_info("test_search_project_byBelongers", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 查询开启和关闭的流程树
    def test_search_project_byOpenStatus_all(self):
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "search_project_byOpenStatus_all",
            headers=self.headers,
        )
        # 实际结果
        actual_res = res.json()
        # 预期结果
        expect_res = get_expect_res(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "search_project_byOpenStatus_all",
        )
        # 日志
        log_case_info("test_search_project_byOpenStatus_all", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 查询开启状态的流程树
    def test_search_project_byOpenStatus_open(self):
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "search_project_byOpenStatus_open",
            headers=self.headers,
        )
        # 实际结果
        actual_res = res.json()
        # 预期结果
        expect_res = get_expect_res(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "search_project_byOpenStatus_open",
        )
        # 日志
        log_case_info("test_search_project_byOpenStatus_open", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 查询关闭状态的流程树
    def test_search_project_byOpenStatus_close(self):
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "search_project_byOpenStatus_close",
            headers=self.headers,
        )
        # 实际结果
        actual_res = res.json()
        # 预期结果
        expect_res = get_expect_res(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "search_project_byOpenStatus_close",
        )
        # 日志
        log_case_info("test_search_project_byOpenStatus_close", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 通过知识分类查询
    def test_search_project_byKnowledge(self):
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "search_project_byKnowledge",
            headers=self.headers,
        )
        # 实际结果
        actual_res = res.json()
        # 预期结果
        expect_res = get_expect_res(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "search_project_byKnowledge",
        )
        # 日志
        log_case_info("test_search_project_byKnowledge", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 检测流程树名称是否存在
    def test_check_project_name(self):
        res = my_get(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "check_project_name",
            headers=self.headers,
        )
        # 实际结果
        actual_res = res.json()
        # 预期结果
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name9"], "check_project_name"
        )
        # 日志
        log_case_info("test_search_project_byKnowledge", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 新建流程树
    def test_new_project(self):
        # 新建
        my_post(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "new_project",
            headers=self.headers,
        )
        # 预期结果
        res_search = my_get(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "验证新建流程树",
            headers=self.headers,
        )
        res_search_json = res_search.json()
        project_id = res_search_json["data"]["paginate"]["data"][0]["id"]
        phone_number = res_search_json["data"]["paginate"]["data"][0]["phone_number"]
        update_time = res_search_json["data"]["paginate"]["data"][0]["update_time"]
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name9"], "new_project"
        )
        # 将id覆盖至预期结果
        expect_res["data"]["paginate"]["data"][0]["id"] = project_id
        # 将话术流程号码覆盖至预期结果
        expect_res["data"]["paginate"]["data"][0]["phone_number"] = phone_number
        # 将更新时间覆盖至预期结果
        expect_res["data"]["paginate"]["data"][0]["update_time"] = update_time
        # 实际结果
        actual_res = res_search.json()
        # # 删除话术流程
        delete_project(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "查询流程树",
            "delete_project_1",
            "自动化新建流程树",
        )
        # 日志
        log_case_info("test_new_project", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 复制流程树
    def test_copy_project(self):
        # 复制
        my_post(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "copy_project",
            headers=self.headers,
        )
        # 预期结果
        res_search = my_get(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "验证复制流程树",
            headers=self.headers,
        )
        res_search_json = res_search.json()
        project_id = res_search_json["data"]["paginate"]["data"][0]["id"]
        phone_number = res_search_json["data"]["paginate"]["data"][0]["phone_number"]
        update_time = res_search_json["data"]["paginate"]["data"][0]["update_time"]
        expect_res = get_expect_res(
            section_dict["data_file"], section_dict["sheet_name9"], "copy_project"
        )
        # 将id覆盖至预期结果
        expect_res["data"]["paginate"]["data"][0]["id"] = project_id
        # 将话术流程号码覆盖至预期结果
        expect_res["data"]["paginate"]["data"][0]["phone_number"] = phone_number
        # 将更新时间覆盖至预期结果
        expect_res["data"]["paginate"]["data"][0]["update_time"] = update_time
        # 实际结果
        actual_res = res_search.json()
        # 删除话术流程
        delete_project(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "查询流程树",
            "delete_project_1",
            "【勿删】自动化测试复制流程树副本",
        )
        # 日志
        log_case_info("test_copy_project", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 复制流程树的同义词
    def test_copy_project_synonymWords(self):
        # 复制流程树
        my_post(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "copy_project",
            headers=self.headers,
        )
        time.sleep(2)
        # 实际结果
        res_synonymWords = my_get(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "copy_project_synonymWords",
            headers=self.headers,
        )
        res_synonymWords_json = res_synonymWords.json()
        project_name = res_synonymWords_json["data"]["paginate"]["data"][0]["project_name"]
        word_name = res_synonymWords_json["data"]["paginate"]["data"][0]["name"]
        actual_res = [word_name, project_name]
        # 预期结果
        expect_res = get_expect_res_text(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "copy_project_synonymWords",
        )
        # 删除话术流程
        delete_project(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "查询流程树",
            "delete_project_1",
            "【勿删】自动化测试复制流程树副本",
        )
        # 日志
        log_case_info("test_copy_project_synonymWords", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, str(actual_res))

    # 复制流程树的同类词
    def test_copy_project_similarWords(self):
        # 复制流程树
        my_post(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "copy_project",
            headers=self.headers,
        )
        time.sleep(2)
        # 实际结果
        res_synonymWords = my_get(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "copy_project_similarWords",
            headers=self.headers,
        )
        res_synonymWords_json = res_synonymWords.json()
        project_name = res_synonymWords_json["data"]["paginate"]["data"][0]["project_name"]
        word_name = res_synonymWords_json["data"]["paginate"]["data"][0]["name"]
        actual_res = [word_name, project_name]
        # 预期结果
        expect_res = get_expect_res_text(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "copy_project_similarWords",
        )
        # 删除话术流程
        delete_project(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "查询流程树",
            "delete_project_1",
            "【勿删】自动化测试复制流程树副本",
        )
        # 日志
        log_case_info("test_copy_project_similarWords", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, str(actual_res))

    # 复制流程树的热词
    def test_copy_project_hotWords(self):
        # 复制流程树
        my_post(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "copy_project",
            headers=self.headers,
        )
        time.sleep(2)
        # 实际结果
        res_synonymWords = my_get(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "copy_project_hotWords",
            headers=self.headers,
        )
        res_synonymWords_json = res_synonymWords.json()
        project_name = res_synonymWords_json["data"]["paginate"]["data"][0]["project_name"]
        hot_word = res_synonymWords_json["data"]["paginate"]["data"][0]["name"]
        replace_word = res_synonymWords_json["data"]["paginate"]["data"][0]["replace"][0][
            "replace_content"
        ]
        actual_res = [hot_word, replace_word, project_name]
        # 预期结果
        expect_res = get_expect_res_text(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "copy_project_hotWords"
        )
        # 删除话术流程
        delete_project(
            section_dict["data_file"],
            section_dict["sheet_name9"],
            "查询流程树",
            "delete_project_1",
            "【勿删】自动化测试复制流程树副本",
        )
        # 日志
        log_case_info("test_copy_project_hotWords", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, str(actual_res))

    # 删除流程并删除对应词集
    def test_del_project_and_words(self):
        # 复制流程树
        my_post(section_dict['data_file'],
                section_dict['sheet_name9'],
                'copy_project',
                headers=self.headers)

        time.sleep(2)
        # 删除流程树和对应词集
        delete_project(section_dict['data_file'],
                       section_dict['sheet_name9'],
                       '查询流程树',
                       'delete_project_1',
                       '【勿删】自动化测试复制流程树副本')
        # 实际结果
        res_project = search_project(section_dict['data_file'],
                                     section_dict['sheet_name9'], 'def_search',
                                     '【勿删】自动化测试复制流程树副本')
        res_synonymWords = my_get(section_dict['data_file'],
                                  section_dict['sheet_name9'],
                                  'copy_project_synonymWords',
                                  headers=self.headers)

        res_synonymWords_json = res_synonymWords.json()
        project_name = res_synonymWords_json['data']['paginate']['data'][0]['project_name']
        actual_res_project = res_project
        actual_res_words = project_name
        # 预期结果
        expect_res_project = get_expect_res(section_dict['data_file'],
                                            section_dict['sheet_name9'],
                                            'del_project')
        expect_res_words = get_expect_res_text(section_dict['data_file'],
                                               section_dict['sheet_name9'],
                                               'delete_project_1')
        # 日志
        log_case_info("test_del_project_and_words", expect_res_project, actual_res_project)
        log_case_info("test_del_project_and_words", expect_res_words, actual_res_words)
        # 断言
        self.assertEqual(expect_res_project, actual_res_project)
        self.assertEqual(expect_res_words, actual_res_words)

    # 仅删除话术流程
    def test_del_project(self):
        # 复制流程树
        my_post(section_dict['data_file'],
                section_dict['sheet_name9'],
                'copy_project',
                headers=self.headers)
        time.sleep(1)
        res_project = search_project(section_dict['data_file'],
                                     section_dict['sheet_name9'],
                                     'def_search',
                                     '【勿删】自动化测试复制流程树副本')
        time.sleep(1)
        # 删除流程树
        delete_project(section_dict['data_file'],
                       section_dict['sheet_name9'],
                       '查询流程树',
                       'delete_project_0',
                       '【勿删】自动化测试复制流程树副本')
        time.sleep(1)
        # 实际结果
        res_project_del = search_project(section_dict['data_file'],
                                         section_dict['sheet_name9'],
                                         'def_search',
                                         '【勿删】自动化测试复制流程树副本')

        res_synonymWords = my_get(section_dict['data_file'],
                                  section_dict['sheet_name9'],
                                  '查询流程树已被删除的词集',
                                  headers=self.headers)
        res_synonymWords_json = res_synonymWords.json()
        actual_project_id = res_synonymWords_json['data']['paginate']['data'][0]['project_id']
        actual_res_project = res_project_del
        # 预期结果
        expect_project_id = res_project['data']['paginate']['data'][0]['id']
        expect_res_project = get_expect_res(section_dict['data_file'],
                                            section_dict['sheet_name9'],
                                            'del_project')
        # 日志
        log_case_info("test_del_project", expect_res_project, actual_res_project)
        log_case_info("test_del_project", expect_project_id, actual_project_id)
        # 断言
        self.assertEqual(expect_res_project, actual_res_project)
        self.assertEqual(expect_project_id, actual_project_id)

    # 获取流程树全局配置
    def test_get_global_config(self):
        # 实际结果
        res = my_get(section_dict['data_file'],
                     section_dict['sheet_name9'],
                     'get_global_config',
                     headers=self.headers)
        actual_res = res.json()
        # 预期结果
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'get_global_config')
        # 日志
        log_case_info("test_get_global_config", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 配置重复话术
    def test_edit_repeatWords(self):
        # 新建
        my_post(section_dict['data_file'],
                section_dict['sheet_name9'],
                'new_project',
                headers=self.headers)
        # 预期结果
        res_search = my_get(section_dict['data_file'],
                            section_dict['sheet_name9'],
                            '验证新建流程树',
                            headers=self.headers)
        res_search_json = res_search.json()
        project_id = res_search_json['data']['paginate']['data'][0]['id']
        expect_res = get_expect_res_text(section_dict['data_file'],
                                         section_dict['sheet_name9'],
                                         'edit_repeatWords')
        # 配置重复话术
        data = get_request_data(section_dict['data_file'],
                                section_dict['sheet_name9'],
                                'edit_repeatWords')
        data['id'] = project_id
        url_edit = get_url(section_dict['data_file'],
                           section_dict['sheet_name9'],
                           'edit_repeatWords')
        requests.post(url=url_edit, data=json.dumps(data), headers=self.headers)
        # 实际结果
        url_get = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          '验证事件配置')
        url_get = url_get + str(project_id)
        res_edit = requests.get(url=url_get, headers=self.headers)
        res_edit_json = res_edit.json()
        repeat_words = res_edit_json['data']['built_in']['repeat_words'][0]
        actual_res = repeat_words
        # 删除话术流程
        delete_project(section_dict['data_file'],
                       section_dict['sheet_name9'],
                       '查询流程树',
                       'delete_project_1',
                       '自动化新建流程树')
        # 日志
        log_case_info("test_edit_repeatWords", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 配置敏感词
    def test_edit_stopWords(self):
        # 新建
        my_post(section_dict['data_file'],
                section_dict['sheet_name9'],
                'new_project',
                headers=self.headers)
        # 预期结果
        res_search = my_get(section_dict['data_file'],
                            section_dict['sheet_name9'],
                            '验证新建流程树',
                            headers=self.headers)
        res_search_json = res_search.json()
        project_id = res_search_json['data']['paginate']['data'][0]['id']
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'edit_stopWords')
        # 配置敏感词
        data = get_request_data(section_dict['data_file'],
                                section_dict['sheet_name9'],
                                'edit_stopWords')
        data['id'] = project_id
        url_edit = get_url(section_dict['data_file'], section_dict['sheet_name9'],
                           'edit_stopWords')
        requests.post(url=url_edit, data=json.dumps(data), headers=self.headers)
        # 实际结果
        url_get = get_url(section_dict['data_file'], section_dict['sheet_name9'],
                          '验证事件配置')
        url_get = url_get + str(project_id)
        res_edit = requests.get(url=url_get, headers=self.headers)
        res_edit_json = res_edit.json()
        actual_res = res_edit_json['data']['built_in']['stop_words'][0]
        # 删除话术流程
        delete_project(section_dict['data_file'],
                       section_dict['sheet_name9'],
                       '查询流程树',
                       'delete_project_1',
                       '自动化新建流程树')
        # 日志
        log_case_info("test_edit_stopWords", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 配置短信
    def test_edit_sms(self):
        # 新建流程树
        my_post(section_dict['data_file'],
                section_dict['sheet_name9'],
                'new_project',
                headers=self.headers)
        # 预期结果
        res_search = my_get(section_dict['data_file'],
                            section_dict['sheet_name9'],
                            '验证新建流程树',
                            headers=self.headers)
        res_search_json = res_search.json()
        project_id = res_search_json['data']['paginate']['data'][0]['id']
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'edit_sms')
        # 配置短信
        data = get_request_data(section_dict['data_file'],
                                section_dict['sheet_name9'],
                                'edit_sms')
        data['id'] = project_id
        url_edit = get_url(section_dict['data_file'],
                           section_dict['sheet_name9'],
                           'edit_sms')
        requests.post(url=url_edit,
                      data=json.dumps(data),
                      headers=self.headers)
        # 实际结果
        url_get = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          '验证事件配置')
        url_get = url_get + str(project_id)
        res_edit = requests.get(url=url_get, headers=self.headers)
        res_edit_json = res_edit.json()
        actual_res = res_edit_json['data']['sms_templates']
        # 删除话术流程
        delete_project(section_dict['data_file'],
                       section_dict['sheet_name9'],
                       '查询流程树',
                       'delete_project_1',
                       '自动化新建流程树')
        # 日志
        log_case_info("test_edit_sms", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 配置等待超时
    def test_edit_waiting(self):
        # 新建流程树
        my_post(section_dict['data_file'],
                section_dict['sheet_name9'],
                'new_project',
                headers=self.headers)
        # 预期结果
        res_search = my_get(section_dict['data_file'],
                            section_dict['sheet_name9'],
                            '验证新建流程树',
                            headers=self.headers)
        res_search_json = res_search.json()
        project_id = res_search_json['data']['paginate']['data'][0]['id']
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'edit_waiting')
        # 配置等待超时
        data = get_request_data(section_dict['data_file'],
                                section_dict['sheet_name9'],
                                'edit_waiting')
        data['id'] = project_id
        url_edit = get_url(section_dict['data_file'],
                           section_dict['sheet_name9'],
                           'edit_waiting')
        requests.post(url=url_edit,
                      data=json.dumps(data),
                      headers=self.headers)
        # 实际结果
        url_get = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          '验证事件配置')
        url_get = url_get + str(project_id)
        res_edit = requests.get(url=url_get, headers=self.headers)
        res_edit_json = res_edit.json()
        actual_res = res_edit_json['data']['built_in']['waiting_timeout']
        # 删除话术流程
        delete_project(section_dict['data_file'],
                       section_dict['sheet_name9'],
                       '查询流程树',
                       'delete_project_1',
                       '自动化新建流程树')
        # 日志
        log_case_info("test_edit_waiting", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 配置结束对话内容
    def test_edit_endSession(self):
        # 新建流程树
        my_post(section_dict['data_file'],
                section_dict['sheet_name9'],
                'new_project',
                headers=self.headers)
        # 预期结果
        res_search = my_get(section_dict['data_file'],
                            section_dict['sheet_name9'],
                            '验证新建流程树',
                            headers=self.headers)
        res_search_json = res_search.json()
        project_id = res_search_json['data']['paginate']['data'][0]['id']
        expect_res = get_expect_res_text(section_dict['data_file'],
                                         section_dict['sheet_name9'],
                                         'edit_endSession')
        # 配置结束对话内容
        data = get_request_data(section_dict['data_file'],
                                section_dict['sheet_name9'],
                                'edit_endSession')
        data['id'] = project_id
        url_edit = get_url(section_dict['data_file'],
                           section_dict['sheet_name9'],
                           'edit_endSession')
        requests.post(url=url_edit, data=json.dumps(data), headers=self.headers)
        # 实际结果
        url_get = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          '验证事件配置')
        url_get = url_get + str(project_id)
        res_edit = requests.get(url=url_get, headers=self.headers)
        res_edit_json = res_edit.json()
        actual_res = res_edit_json['data']['operations']['end_session']
        # 删除话术流程
        delete_project(section_dict['data_file'],
                       section_dict['sheet_name9'],
                       '查询流程树',
                       'delete_project_1',
                       '自动化新建流程树')
        # 日志
        log_case_info("test_edit_endSession", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, str(actual_res))

    # 配置挖槽询问
    def test_edit_slot(self):
        # 新建
        my_post(section_dict['data_file'],
                section_dict['sheet_name9'],
                'new_project',
                headers=self.headers)
        # 预期结果
        res_search = my_get(section_dict['data_file'],
                            section_dict['sheet_name9'],
                            '验证新建流程树',
                            headers=self.headers)
        res_search_json = res_search.json()
        project_id = res_search_json['data']['paginate']['data'][0]['id']
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'edit_slot')
        # 配置敏感词
        data = get_request_data(section_dict['data_file'],
                                section_dict['sheet_name9'],
                                'edit_slot')
        data['id'] = project_id
        url_edit = get_url(section_dict['data_file'],
                           section_dict['sheet_name9'],
                           'edit_slot')
        requests.post(url=url_edit,
                      data=json.dumps(data),
                      headers=self.headers)
        # 实际结果
        url_get = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          '验证事件配置')
        url_get = url_get + str(project_id)
        res_edit = requests.get(url=url_get, headers=self.headers)
        res_edit_json = res_edit.json()
        actual_res = res_edit_json['data']['operations']['slots_query']
        # 删除话术流程
        delete_project(section_dict['data_file'],
                       section_dict['sheet_name9'],
                       '查询流程树',
                       'delete_project_1',
                       '自动化新建流程树')
        # 日志
        log_case_info("test_edit_slot", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 配置异常处理-跳转节点
    def test_edit_timeHandle_jumpNode(self):
        # 新建流程
        my_post(section_dict['data_file'],
                section_dict['sheet_name9'],
                'new_project',
                headers=self.headers)
        # 预期结果
        res_search = my_get(section_dict['data_file'],
                            section_dict['sheet_name9'],
                            '验证新建流程树',
                            headers=self.headers)
        res_search_json = res_search.json()
        project_id = res_search_json['data']['paginate']['data'][0]['id']
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'edit_timeHandle_jumpNode')
        # 配置异常处理-跳转节点
        data = get_request_data(section_dict['data_file'],
                                section_dict['sheet_name9'],
                                'edit_timeHandle_jumpNode')
        data['id'] = project_id
        url_edit = get_url(section_dict['data_file'],
                           section_dict['sheet_name9'],
                           'edit_timeHandle_jumpNode')
        requests.post(url=url_edit,
                      data=json.dumps(data),
                      headers=self.headers)
        # 实际结果
        url_get = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          '验证事件配置')
        url_get = url_get + str(project_id)
        res_edit = requests.get(url=url_get, headers=self.headers)
        res_edit_json = res_edit.json()
        actual_res = res_edit_json['data']['operations']['timeout_handle']
        # # 删除话术流程
        # delete_project(section_dict['data_file'],
        #                section_dict['sheet_name9'],
        #                '查询流程树',
        #                'delete_project_1',
        #                '自动化新建流程树')
        # 日志
        log_case_info("test_edit_timeHandle_jumpNode", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 配置异常处理-结束对话
    def test_edit_timeHandle_hangUp(self):
        # 新建流程树
        my_post(section_dict['data_file'],
                section_dict['sheet_name9'],
                'new_project',
                headers=self.headers)
        # 预期结果
        res_search = my_get(section_dict['data_file'],
                            section_dict['sheet_name9'],
                            '验证新建流程树',
                            headers=self.headers)
        res_search_json = res_search.json()
        project_id = res_search_json['data']['paginate']['data'][0]['id']
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'edit_timeHandle_hangUp')
        # 配置异常处理-结束对话
        data = get_request_data(section_dict['data_file'],
                                section_dict['sheet_name9'],
                                'edit_timeHandle_hangUp')
        data['id'] = project_id
        url_edit = get_url(section_dict['data_file'],
                           section_dict['sheet_name9'],
                           'edit_timeHandle_hangUp')
        requests.post(url=url_edit, data=json.dumps(data), headers=self.headers)
        # 实际结果
        url_get = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          '验证事件配置')
        url_get = url_get + str(project_id)
        res_edit = requests.get(url=url_get, headers=self.headers)
        res_edit_json = res_edit.json()
        actual_res = res_edit_json['data']['operations']['timeout_handle']
        # 删除话术流程
        delete_project(section_dict['data_file'],
                       section_dict['sheet_name9'],
                       '查询流程树',
                       'delete_project_1',
                       '自动化新建流程树')
        # 日志
        log_case_info("test_edit_timeHandle_hangUp", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 配置接入超并发时转人工
    def test_edit_overConcurrency_transferHuman(self):
        # 新建流程树
        my_post(section_dict['data_file'],
                section_dict['sheet_name9'],
                'new_project',
                headers=self.headers)
        # 预期结果
        res_search = my_get(section_dict['data_file'],
                            section_dict['sheet_name9'],
                            '验证新建流程树',
                            headers=self.headers)
        res_search_json = res_search.json()
        project_id = res_search_json['data']['paginate']['data'][0]['id']
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'edit_overConcurrency_transferHuman')
        # 配置接入超并发时转人工
        data = get_request_data(section_dict['data_file'],
                                section_dict['sheet_name9'],
                                'edit_overConcurrency_transferHuman')
        data['id'] = project_id
        url_edit = get_url(section_dict['data_file'],
                           section_dict['sheet_name9'],
                           'edit_overConcurrency_transferHuman')
        requests.post(url=url_edit,
                      data=json.dumps(data),
                      headers=self.headers)
        # 实际结果
        url_get = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          '验证事件配置')
        url_get = url_get + str(project_id)
        res_edit = requests.get(url=url_get, headers=self.headers)
        res_edit_json = res_edit.json()
        actual_res = res_edit_json['data']['built_in']['call_in_hyper_concurrency']
        # 删除话术流程
        delete_project(section_dict['data_file'],
                       section_dict['sheet_name9'],
                       '查询流程树',
                       'delete_project_1',
                       '自动化新建流程树')
        # 日志
        log_case_info("test_edit_overConcurrency_transferHuman", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 配置接入超并发时挂断
    def test_edit_overConcurrency_hangUp(self):
        # 新建流程树
        my_post(section_dict['data_file'],
                section_dict['sheet_name9'],
                'new_project',
                headers=self.headers)
        # 预期结果
        res_search = my_get(section_dict['data_file'],
                            section_dict['sheet_name9'],
                            '验证新建流程树',
                            headers=self.headers)
        res_search_json = res_search.json()
        project_id = res_search_json['data']['paginate']['data'][0]['id']
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'edit_overConcurrency_hangUp')
        # 配置超并发时挂断
        data = get_request_data(section_dict['data_file'],
                                section_dict['sheet_name9'],
                                'edit_overConcurrency_hangUp')
        data['id'] = project_id
        url_edit = get_url(section_dict['data_file'],
                           section_dict['sheet_name9'],
                           'edit_overConcurrency_hangUp')
        requests.post(url=url_edit,
                      data=json.dumps(data),
                      headers=self.headers)
        # 实际结果
        url_get = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          '验证事件配置')
        url_get = url_get + str(project_id)
        res_edit = requests.get(url=url_get, headers=self.headers)
        res_edit_json = res_edit.json()
        actual_res = res_edit_json['data']['built_in']['call_in_hyper_concurrency']
        # 删除话术流程
        delete_project(section_dict['data_file'],
                       section_dict['sheet_name9'],
                       '查询流程树',
                       'delete_project_1',
                       '自动化新建流程树')
        # 日志
        log_case_info("test_edit_overConcurrency_hangUp", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 获取服务导航配置
    def test_get_navigation(self):
        # 实际结果
        res = my_get(section_dict['data_file'],
                     section_dict['sheet_name9'],
                     'get_navigation',
                     headers=self.headers)
        actual_res = res.json()
        # 预期结果
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'get_navigation')
        # 日志
        log_case_info("test_get_navigation", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 新建服务导航
    def test_set_navigation(self):
        # 新建流程树
        my_post(section_dict['data_file'],
                section_dict['sheet_name9'],
                'new_project',
                headers=self.headers)
        # 预期结果
        res_search = my_get(section_dict['data_file'],
                            section_dict['sheet_name9'],
                            '验证新建流程树',
                            headers=self.headers)
        res_search_json = res_search.json()
        project_id = res_search_json['data']['paginate']['data'][0]['id']
        expect_res = get_expect_res_text(section_dict['data_file'],
                                         section_dict['sheet_name9'],
                                         'set_navigation')
        # 配置服务导航
        data = get_request_data(section_dict['data_file'],
                                section_dict['sheet_name9'],
                                'set_navigation')
        data['project_id'] = project_id
        url_edit = get_url(section_dict['data_file'],
                           section_dict['sheet_name9'],
                           'set_navigation')
        requests.post(url=url_edit,
                      data=json.dumps(data),
                      headers=self.headers)
        # 实际结果
        url_get = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          '验证服务导航配置')
        url_get = url_get + str(project_id)
        res_edit = requests.get(url=url_get, headers=self.headers)
        res_edit_json = res_edit.json()
        navigation_name = res_edit_json['data']['data'][0]['name']
        navigation_message = res_edit_json['data']['data'][0]['message']
        navigation_icon = res_edit_json['data']['data'][0]['icon']
        actual_res = [navigation_name, navigation_message]
        # 删除话术流程
        delete_project(section_dict['data_file'],
                       section_dict['sheet_name9'],
                       '查询流程树',
                       'delete_project_1',
                       '自动化新建流程树')
        # 日志
        log_case_info("test_set_navigation", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, str(actual_res))
        self.assertIsNotNone(navigation_icon)

    # 删除服务导航
    def test_del_navigation(self):
        # 新建流程树
        my_post(section_dict['data_file'],
                section_dict['sheet_name9'],
                'new_project',
                headers=self.headers)
        # 预期结果
        res_search = my_get(section_dict['data_file'],
                            section_dict['sheet_name9'],
                            '验证新建流程树',
                            headers=self.headers)
        res_search_json = res_search.json()
        project_id = res_search_json['data']['paginate']['data'][0]['id']
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'del_navigation')
        # 新建服务导航
        data_new = get_request_data(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'set_navigation')
        data_new['project_id'] = project_id
        url_new = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          'set_navigation')
        requests.post(url=url_new, data=json.dumps(data_new), headers=self.headers)
        # 删除服务导航
        url_get_navigation = get_url(section_dict['data_file'],
                                     section_dict['sheet_name9'],
                                     '验证服务导航配置')
        url_get_navigation = url_get_navigation + str(project_id)
        res_get_navigation = requests.get(url=url_get_navigation, headers=self.headers)
        res_get_navigation_json = res_get_navigation.json()
        navigation_id = res_get_navigation_json['data']['data'][0]['id']
        url_del = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          'del_navigation')
        url_del = url_del + str(navigation_id)
        requests.delete(url=url_del, headers=self.headers)
        # 实际结果
        res_after_del = requests.get(url=url_get_navigation, headers=self.headers)
        actual_res = res_after_del.json()
        # 删除话术流程
        delete_project(section_dict['data_file'],
                       section_dict['sheet_name9'],
                       '查询流程树',
                       'delete_project_1',
                       '自动化新建流程树')
        # 日志
        log_case_info("test_del_navigation", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 获取tts可选配置
    def test_get_tts(self):
        # 预期结果
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'get_tts')
        # 实际结果
        res = my_get(section_dict['data_file'],
                     section_dict['sheet_name9'],
                     'get_tts',
                     headers=self.headers)
        actual_res = res.json()
        # 日志
        log_case_info("test_get_tts", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 获取流程树基本配置信息
    def test_get_project_config(self):
        # 实际结果
        res = my_post(section_dict['data_file'],
                      section_dict['sheet_name9'],
                      'get_project_config',
                      headers=self.headers)
        actual_res = res.json()
        img_url = actual_res['data']['project_virtualavatar']['img_url']
        interactive_url = actual_res['data']['project_virtualavatar']['interactive_url']
        rest_url = actual_res['data']['project_virtualavatar']['rest_url']
        # 预期结果
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'get_project_config')
        expect_res['data']['project_virtualavatar']['img_url'] = img_url
        expect_res['data']['project_virtualavatar']['interactive_url'] = interactive_url
        expect_res['data']['project_virtualavatar']['rest_url'] = rest_url
        # 日志
        log_case_info("test_get_project_config", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 获取短信渠道列表
    def test_get_smsService(self):
        # 预期结果
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'get_smsService')
        # 实际结果
        res = my_get(section_dict['data_file'],
                     section_dict['sheet_name9'],
                     'get_smsService',
                     headers=self.headers)
        actual_res = res.json()
        # 日志
        log_case_info("test_get_smsService", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 获取转人工工作时间配置
    def test_get_WorkingTime(self):
        # 预期结果
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'get_WorkingTime')
        # 实际结果
        res = my_get(section_dict['data_file'],
                     section_dict['sheet_name9'],
                     'get_WorkingTime',
                     headers=self.headers)
        actual_res = res.json()
        # 日志
        log_case_info("test_get_WorkingTime", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 获取转人工非工作时间配置
    def test_get_nonWorkingTime(self):
        # 预期结果
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'get_nonWorkingTime')
        # 实际结果
        res = my_get(section_dict['data_file'],
                     section_dict['sheet_name9'],
                     'get_nonWorkingTime',
                     headers=self.headers)
        actual_res = res.json()
        # 日志
        log_case_info("test_get_nonWorkingTime", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 新增转人工工作时间配置
    def test_new_WorkingTime(self):
        # 新增转人工新建转人工工作时间配置
        res_new = my_post(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          'new_WorkingTime',
                          headers=self.headers)
        res_new_json = res_new.json()
        config_id = res_new_json['data']['id']
        # 预期结果
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'new_WorkingTime')
        expect_res['data']['data'][0]['id'] = config_id
        # 实际结果
        res_get_config = my_get(section_dict['data_file'],
                                section_dict['sheet_name9'],
                                '验证新建转人工工作时间配置',
                                headers=self.headers)
        actual_res = res_get_config.json()
        # 删除新增的人工时间配置
        del_url = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          'del_transferHuman_config')
        del_url = del_url + str(config_id)
        requests.delete(url=del_url, headers=self.headers)
        # 日志
        log_case_info("test_new_WorkingTime", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 新增转人工非工作时间配置-挂断
    def test_new_nonWorkingTime_hangUp(self):
        # 新增转人工非工作时间配置-挂断
        res_new = my_post(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          'new_nonWorkingTime_hangUp',
                          headers=self.headers)
        res_new_json = res_new.json()
        config_id = res_new_json['data']['id']
        # 预期结果
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'new_nonWorkingTime_hangUp')
        expect_res['data']['data'][1]['id'] = config_id
        # 实际结果
        res_get_config = my_get(section_dict['data_file'],
                                section_dict['sheet_name9'],
                                '验证新建转人工非工作时间配置',
                                headers=self.headers)
        actual_res = res_get_config.json()
        # 删除新增的非人工工作时间配置
        del_url = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          'del_transferHuman_config')
        del_url = del_url + str(config_id)
        requests.delete(url=del_url, headers=self.headers)
        # 日志
        log_case_info("test_new_nonWorkingTime_hangUp", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 新增转人工非工作时间配置-挂断
    def test_new_nonWorkingTime_jumpNode(self):
        # 新增转人工非工作时间配置-挂断
        res_new = my_post(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          'new_nonWorkingTime_jumpNode',
                          headers=self.headers)
        res_new_json = res_new.json()
        config_id = res_new_json['data']['id']
        # 预期结果
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'new_nonWorkingTime_jumpNode')
        expect_res['data']['data'][1]['id'] = config_id
        # 实际结果
        res_get_config = my_get(section_dict['data_file'],
                                section_dict['sheet_name9'],
                                '验证新建转人工非工作时间配置',
                                headers=self.headers)
        actual_res = res_get_config.json()
        # 删除新增的非人工工作时间配置
        del_url = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          'del_transferHuman_config')
        del_url = del_url + str(config_id)
        requests.delete(url=del_url, headers=self.headers)
        # 日志
        log_case_info("test_new_nonWorkingTime_jumpNode", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 删除流程转人工配置
    def test_del_transferHuman_config(self):
        # 新增转人工新建转人工工作时间配置
        res_new = my_post(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          'new_WorkingTime',
                          headers=self.headers)
        res_new_json = res_new.json()
        config_id = res_new_json['data']['id']
        # 删除新增的人工时间配置
        del_url = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          'del_transferHuman_config')
        del_url = del_url + str(config_id)
        requests.delete(url=del_url, headers=self.headers)
        # 预期结果
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'del_transferHuman_config')
        # 实际结果
        res_get_config = my_get(section_dict['data_file'],
                                section_dict['sheet_name9'],
                                '验证新建转人工工作时间配置',
                                headers=self.headers)
        actual_res = res_get_config.json()
        # 日志
        log_case_info("test_del_transferHuman_config", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)

    # 新增转人工工作时间配置
    def test_edit_transfer_human_config(self):
        # 新增转人工新建转人工工作时间配置
        res_new = my_post(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          'new_WorkingTime',
                          headers=self.headers)
        res_new_json = res_new.json()
        config_id = res_new_json['data']['id']
        # 预期结果
        expect_res = get_expect_res(section_dict['data_file'],
                                    section_dict['sheet_name9'],
                                    'new_WorkingTime')
        expect_res['data']['data'][0]['id'] = config_id
        # 实际结果
        res_get_config = my_get(section_dict['data_file'],
                                section_dict['sheet_name9'],
                                '验证新建转人工工作时间配置',
                                headers=self.headers)
        actual_res = res_get_config.json()
        # 删除新增的人工时间配置
        del_url = get_url(section_dict['data_file'],
                          section_dict['sheet_name9'],
                          'del_transferHuman_config')
        del_url = del_url + str(config_id)
        requests.delete(url=del_url, headers=self.headers)
        # 日志
        log_case_info("test_edit_transfer_human_config", expect_res, actual_res)
        # 断言
        self.assertEqual(expect_res, actual_res)
