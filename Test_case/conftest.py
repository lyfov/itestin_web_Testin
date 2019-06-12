from selenium import webdriver
import pytest
import os
import sys
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
@pytest.fixture(scope="module")
def driver():
        print("========================================")
        driver = webdriver.Chrome()
        yield driver
        driver.close()
        return driver