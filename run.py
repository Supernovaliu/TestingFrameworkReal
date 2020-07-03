#coding=utf-8

import unittest
import HTMLTestRunnerNew
import time
from config import globalparam


def run():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')

    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    reportname = globalparam.report_path + '\\' + 'TestResult' + now + '.html'
    with open(reportname,'wb') as f:
        runner = HTMLTestRunnerNew.HTMLTestRunner(
            stream=f,
            title='testing report',
            description='Test the import testcase'
        )
        runner.run(suite)

if __name__=='__main__':
    run()