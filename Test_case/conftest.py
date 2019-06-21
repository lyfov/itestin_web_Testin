from selenium import webdriver
import pytest
import os
import sys
import allure
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
@pytest.fixture(scope="function")
def driver():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        print("========================================")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        yield driver
        # driver.save_screenshot("../picture.png")
        # file = open('../test.png', 'rb').read()
        # allure.attach('test_img', file, allure.attach_type.PNG)
        driver.close()
        return driver
