import configparser

class configRead():

    def read_url(self):

        cf= configparser.ConfigParser()
        # 读取配置文件
        cf.read(r'C:\Users\HP\PycharmProjects\itestin_web_tencent\common\config.ini',encoding='utf-8')
        # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，每个section由[]包裹，即[section])，并以列表的形式返回
        section = cf.sections()
        print(section)
        # 获取某个section名为test所对应的键
        op=cf.options("test")
        print(op)
        # 获取莫格section名为test的键值对
        it=cf.items("test")
        print(it)
        url =cf.get("test","url")
        print(url)
        print(type(url))
        return url
    def read_driver(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(r'C:\Users\HP\PycharmProjects\itestin_web_tencent\common\config.ini', encoding='utf-8')
        print(self.cf.get("test","driver"))
        return self.cf.get("test","driver")

    def read_username(self):
        self.cf=configparser.ConfigParser()
        self.cf.read(r'C:\Users\HP\PycharmProjects\itestin_web_tencent\common\config.ini', encoding='utf-8')
        return self.cf.get("email", "uesrname")

    def read_pwd(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(r'C:\Users\HP\PycharmProjects\itestin_web_tencent\common\config.ini', encoding='utf-8')
        return self.cf.get("email", "pwd")

if __name__=="__main__":
    configRead().read_driver()
    configRead().read_url()
    configRead().read_username()
    configRead().read_pwd()