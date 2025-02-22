#!/usr/bin/env python
# code:UTF-8
# @Author  : SUN FEIFEI
import HTMLTestRunner
import re
import time
import os

# from BeautifulReport import BeautifulReport
from conf.base_config import GetVariable as gv


class RunCases:
    def __init__(self, device, port):
        self.device = device
        self.port = port

        if not os.path.exists(gv.REPORT_ROOT):
            os.makedirs(gv.REPORT_ROOT)

        date_time = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
        # 过滤掉deviceName中的':'（因为文件夹名称不能包含':'）
        device_name = re.sub('[:]', '-', '%s' % self.device['deviceName'])
        self.test_report_path = gv.REPORT_ROOT + '/' + device_name + '/' + date_time

        if not os.path.exists(self.test_report_path):
            os.makedirs(self.test_report_path)
        # self.file_name = 'TestReport_' + date_time + '.html'  # 这个filename是生成的自动化测试报告的文件名

        self.file_name = self.test_report_path + '/TestReport_' + date_time + '.html'  # 这个filename是生成的自动化测试报告的文件名

    def get_path(self):
        return self.test_report_path

    def get_device(self):
        return self.device

    def get_port(self):
        return self.port

    def run(self, cases):
        desc = '用例执行情况统计：'
        report_title = '测试用例执行报告'

        fp = open(self.file_name, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title=report_title,
                description=desc)
        runner.run(cases)
        fp.close()

        # desc = '用例执行情况：'
        # result = BeautifulReport(cases)
        # result.report(filename=self.file_name,
        #               description=desc,
        #               log_path=self.test_report_path)
