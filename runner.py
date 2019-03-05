import unittest
import HTMLTestRunner
import os
from Testcase.testcase import testlogin

import time

suite1 = unittest.TestLoader().loadTestsFromTestCase(testlogin)
suite = unittest.TestSuite([suite1])
filename1 = os.getcwd()+"\\"+"Reports\\"
# print(filename1)
filename = filename1+ time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
# print(filename)
fp =open(filename+"Report.html","wb")
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="report", description="fuck")
# runner.run(suite)
report_path = os.path.join(os.getcwd(), r"testOutput\html\report.html")
print(report_path)
# fp = open(report_path, "wb+")
runner = HTMLTestRunner.HTMLTestReportCN(
        stream=fp,
        title=u'自动化测试报告',
        description='详细测试用例结果',  # 不传默认为空
        tester=u"tester")
runner.run(suite)
fp.close()



