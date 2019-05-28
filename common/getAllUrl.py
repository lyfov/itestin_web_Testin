import urllib.request
import re
class Get_curr_alllink():
    def __init__(self,driver):
        self.driver = driver
    def PrintLink(self):

        headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        urllib.request.install_opener(opener)
        #赋值当前页面的url
        file = urllib.request.urlopen(self.driver.current_url).read()
        file = file.decode('utf-8')
        pattern = '(http?://[^\s)";]+(\.(\w|/)*))'
        link = re.compile(pattern).findall(file)
        #去重
        #link = list(set(link))
        for link in link:
                print(link[0])



# url = "http://blog.csdn.net/"
# linklist = get_curr_alllink.getlink(url)
# for link in linklist:
#     print(link[0])
# print(len(linklist))

