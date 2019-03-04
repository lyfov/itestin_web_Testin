from openpyxl import load_workbook

class ParseExcel(object):

        def __init__(self,filename,sheetname):
                self.book = load_workbook(filename)
                self.sheet = self.book.get_sheet_by_name(sheetname)
                # self.maxRowNum = self.sheet.max_row


        def getDataFromSheet(self):
                datalist=[]

                for line in self.sheet:
                        app = {}
                        locallist = []
                        # print(line[0].value)
                        # print(line[1].value)
                        app['username'] = line[0].value
                        app['password'] = line[1].value
                        locallist.append(line[0].value)
                        locallist.append(line[1].value)
                        # datalist.append(locallist)
                        # print(datalist)
                        datalist.append(app)

                        # tmplist = []
                        # tmplist.append(line[1].value)
                        # tmplist.append(line[2].value)
                        # datalist.append(tmplist)
                return datalist


if __name__ == '__main__':
        filename ="C:\\Users\\HP\\Desktop\\1.xlsx"
        sheetname = "Sheet1"
        pe =ParseExcel(filename,sheetname)
        print(pe.getDataFromSheet())