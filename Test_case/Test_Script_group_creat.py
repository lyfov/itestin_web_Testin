from Pages.LoginPage import *
from Pages.HomePage import *
from common.BasePage import *
import allure
import pytest
import pysnooper
from common.configRead import configRead
from Pages.ScriptManagerPage import ScriptManagerPage
class Test_Script_group_creat():
    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        self.driver = driver
        yield self.driver
        self.driver.close()
        return self.driver
    @pysnooper.snoop(r'C:\Users\HP\Desktop\1.log')
    @allure.step("创建脚本组选择清除数据")
    def test_creat_group(self, driver):

        LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
        # 主页选择项目组
        HomePage_one(driver).choise_project()
        sleep(3)
        #点击脚本管理
        HomePage_one(driver).click_auto_script()

        sleep(3)
        # 点击脚本组tab
        ScriptManagerPage(driver).click_scrpt_group_tab()
        sleep(3)
        #点击创建脚本组
        ScriptManagerPage(driver).click_creat_scrpt_group()
        sleep(3)
        #输入脚本组名称
        ScriptManagerPage(driver).input_description_value("asdadasdasd")
        sleep(3)
        #添加两个脚本
        ScriptManagerPage(driver).add_button_twice()
        sleep(3)
        #点击已添加
        ScriptManagerPage(driver).click_added()
        sleep(3)
        ScriptManagerPage(driver).click_ALL_clear()
        sleep(3)

        #点击创建
        ScriptManagerPage(driver).click_success_creat()
        assert ScriptManagerPage(driver).Get_Alert_message() == "操作成功"
    #修改脚本组
    def test_updata_group(self, driver):
        ScriptManagerPage(driver).click_first_updata()
        sleep(3)
        # 输入脚本组名称
        ScriptManagerPage(driver).input_description_value("修改的脚本组")
        sleep(3)
        # 添加两个脚本
        ScriptManagerPage(driver).add_button_twice()
        sleep(3)
        # 点击已添加
        ScriptManagerPage(driver).click_added()
        sleep(3)
        # 点击创建
        ScriptManagerPage(driver).click_upadata_success()
        assert ScriptManagerPage(driver).Get_Alert_message() == "操作成功"
        # 删除脚本组

    def test_Remove_Group(self, driver):
        ScriptManagerPage(driver).click_Delete_Forst()
        sleep(3)
        # 输入脚本组名称
        ScriptManagerPage(driver).click_Remove_Confirm()
        assert ScriptManagerPage(driver).Get_Alert_message()=="删除成功"