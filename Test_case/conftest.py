import os
import sys

import pytest
from selenium import webdriver

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
@pytest.fixture(scope="function")
def driver():

        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        print("========================================")
        driver = webdriver.Chrome(chrome_options=chrome_options)

        # driver =webdriver.Remote(
        # command_executor="http://10.32.25.59:5555/wd/hub",
        # desired_capabilities={"browserName": "chrome"}
        # )
        yield driver
        # driver.save_screenshot("../picture.png")
        # file = open('../test.png', 'rb').read()
        # allure.attach('test_img', file, allure.attach_type.PNG)
        driver.close()
        return driver
