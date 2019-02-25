import unittest
import HTMLTestRunner
import os
from Testcase.testcase import testlogin
import time

suite1 = unittest.TestLoader().loadTestsFromTestCase(testlogin)
suite = unittest.TestSuite([suite1])
filename1 = os.getcwd()+"\\"+"Reports\\"
print(filename1)
filename = filename1+ time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
print(filename)
fp =open(filename+"Report.html","wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="report", description="fuck")
runner.run(suite)


