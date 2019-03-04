import ddt
import unittest
from common.ExcelUtil import ParseExcel
from ddt import ddt,data,unpack
@ddt
class test1(unittest.TestCase):
    excel = ParseExcel("C:\\Users\\HP\\Desktop\\1.xlsx", "Sheet1")
    print(excel.getDataFromSheet())
    @data(*excel.getDataFromSheet())
    # @unpack
    def testda(self,data):

        print(data['username'],data['password'])

if __name__ == "__main__":
    unittest.main()