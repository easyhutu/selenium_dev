"""
CREAt: 2017/3/22
AUTHOR: Hehahutu
"""
from framework.HTMLTestRunner import HTMLTestRunner
from datetime import datetime
import time
import unittest
from config.settings import TIME_TAG, TEST_REPORT_PATH, TEST_SUITES_PATH
import os
from tools.emails import send_email

if __name__ == '__main__':
    cases = unittest.defaultTestLoader.discover(start_dir=TEST_SUITES_PATH, pattern='*_test.py')
    file_path = os.path.join(TEST_REPORT_PATH, '{}_test_case.html'.format(TIME_TAG))
    report_file = open(file_path, 'w', encoding='utf8')
    runner = HTMLTestRunner(stream=report_file, title='测试报告', description='万店掌WEB系统测试报告-详细信息请查看附件')
    runner.run(cases)
    report_file.close()

    send_email(file_path)
