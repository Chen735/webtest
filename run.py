#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import time
import unittest
import sys
sys.path.append('../')

from report.HTMLTestRunner3 import HTMLTestRunner

test_dir = './test/testcase'


def create_suite():
    print(test_dir)
    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='test*.py',
        # pattern='test_01_login.py',

        # top_level_dir=None
    )

    TestSuite = unittest.TestSuite()  # 测试集
    # TestSuite.addTest(discover)
    TestSuite.addTest(discover)
    # print('discover')
    # print(discover)
    # for test_case in discover:
    #     print('Testcase----------------------------------------')
    #     # TestSuite.addTests(test_case)
    #     print(test_case)
    return TestSuite


def report():
    if len(sys.argv) > 1:
        report_name = os.path.dirname(os.getcwd()) + '\\report\\' + sys.argv[1] + '_result.html'
        print(report_name)
    else:
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        # 需要查看每段时间的测试报告，可以这样写：
        # report_name = os.getcwd() + '\\report\\'+now+'result.html'
        report_name = './report/result.html'
        print(report_name)
    return report_name


if __name__ == '__main__':
    suite = create_suite()
    print('-----------------Testsuite', suite)
    fp = open(report(), 'wb')
    Runner = HTMLTestRunner(
        stream=fp,
        title='测试报告',
        description='测试用例执行情况'
    )
    Runner.run(suite)
    fp.close()
