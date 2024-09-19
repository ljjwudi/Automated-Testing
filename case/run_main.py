import os
import unittest
import HTMLTestRunner

from case.HomePage import TestHomePage
from case.HotWords import TestHotWords
from case.Project import TestProject
from case.Qa import TestQA
from case.RecordManagement import TestRecordManagement
from case.Login import TestUserLogin
from case.SimilarWords import TestSimilarWords
from case.SynonymWords import TestSynonymWords

if __name__ == "__main__":
    suite = unittest.TestSuite()
    test_case_QA = [
        TestQA("test_search_qa_combination"),
        TestQA("test_search_qa_by_question"),
        TestQA("test_search_qa_by_answer"),
        TestQA("test_new_qa"),
        TestQA("test_export_qa"),
        TestQA("test_check_relation"),
        TestQA("test_edit_qa"),
        TestQA("test_mul_qa_close"),
        TestQA("test_mul_qa_open"),
        TestQA("test_mul_qa_range"),
        TestQA("test_mul_qa_label"),
        TestQA("test_mul_check"),
        TestQA("test_close_qa"),
        TestQA("test_open_qa"),
        TestQA("test_delete_qa"),
        TestQA("test_search_qa_id"),
        TestQA("test_import_qa"),
        TestQA("test_ext_import_qa"),
        TestQA("test_custom_import_type1"),
        TestQA("test_custom_import_type2"),
        TestQA("test_down_result"),
        TestQA("test_search_qa_by_pagesize"),
    ]
    suite.addTests(test_case_QA)
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestHomePage))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestRecordManagement))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestUserLogin))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSynonymWords))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSimilarWords))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestHotWords))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestProject))
    report_path = os.path.abspath("../report/test0528.html")
    report = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=report,
        title="My Test Report",
        description="This demonstrates " "the " "report output by " "HTMLTestRunner.",
    )
    runner.run(suite)

