from selenium import webdriver
import pytest
import os
import sys
import allure
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
@pytest.fixture(scope="function")
def driver():
        print("========================================")
        driver = webdriver.Chrome()
        yield driver
        # driver.save_screenshot("../picture.png")
        # file = open('../test.png', 'rb').read()
        # allure.attach('test_img', file, allure.attach_type.PNG)
        driver.close()
        return driver
