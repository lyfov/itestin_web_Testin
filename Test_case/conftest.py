import os
import sys

import pytest
from selenium import webdriver

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))


@pytest.fixture(scope="class")
def driver():
        global i
        i = 1
        chrome_options=webdriver.ChromeOptions()
        # 增加linux环境下启动浏览器的权限
        # chrome_options.add_argument('--no-sandbox')
        ##不需要可视化启动浏览器，进行后台运行
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1366,768')
        print("========================================")
        driver = webdriver.Chrome(options=chrome_options)
        yield driver
        # driver.save_screenshot("../picture"+i+".png")
        # i=i+1
        # file = open('../test.png', 'rb').read()
        # allure.attach('test_img', file, allure.attach_type.PNG)
        # print(i)
        # print(driver.save_screenshot)
        driver.close()
        return driver
