from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get(r'http://test.pro.testin.cn/account/login.htm')
sleep(3)
driver.find_element_by_id('email').send_keys("chenhaodong@testin.cn")
sleep(3)
driver.find_element_by_id('pwd').send_keys("chd650320")
sleep(3)
driver.find_element_by_id('submitBtn').click()
driver.find_element_by_xpath('//*[@id="page-menu"]/div/nav/div/ul/li[6]/a/span').click()
sleep(3)
driver.find_element_by_xpath('//*[@id="page-menu"]/div/nav/div/ul/li[6]/ul/li[2]/a').click()
sleep(3)
driver.find_element_by_xpath('//*[@id="itestin-project-main"]/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/button[2]/span').click()
sleep(3)
driver.find_element_by_xpath('//*[@id="create-tabs-wrap"]/div[1]/button/span').click()
from selenium.webdriver import ActionChains
def addAtt(driver,element,att,value):
    driver.execute_script("arguments[0].%s=arguments[1]"%att,element,value)

if __name__=="__main__":
    element = driver.find_element_by_class_name("cn_left")
    sleep(3)
    #element.click()
    driver.find_element_by_xpath('//*[@id="create_step"]/div[1]/div[1]/div[2]/div[3]/table/tbody/tr[3]/td[1]/div').click()
    for i in range(10):
        #river.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        ActionChains(driver).key_down(Keys.DOWN).perform()
        sleep(5)
    # js='var action=document.documentElement.scrollTop=10000'
    # sleep(3)
    # driver.execute_script(js)





