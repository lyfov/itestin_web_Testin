import os
import sys

import pytest
from selenium import webdriver

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
@pytest.fixture(scope="function")
def driver():

        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        print("========================================")
        driver = webdriver.Chrome(options=chrome_options)


        yield driver
        # driver.save_screenshot("../picture.png")
        # file = open('../test.png', 'rb').read()
        # allure.attach('test_img', file, allure.attach_type.PNG)
        driver.close()
        return driver
