from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

##-------------------------------TEST CASE----------------------
##1. Enter Valid username and password
##2. Enter InValid username and password
import XLutils

driver = webdriver.Chrome()
driver.get('http://localhost/bank/')
driver.set_window_size(1420, 780)
path = 'AllTestCases.xlsx'

time.sleep(5)
driver.find_element_by_xpath("//*[@id='headingOne']/h5/a/button").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseOne"]/div/form/input[1]').send_keys("a@a.com")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseOne"]/div/form/input[2]').send_keys("1234")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseOne"]/div/form/button').click()
time.sleep(2)
XLutils.writeData(path,'Sheet1',2,2,'pass')
#---------------------------Ibavlid username sections-----------
driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/form/a[5]').click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='headingOne']/h5/a/button").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseOne"]/div/form/input[1]').send_keys("something@a.com")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseOne"]/div/form/input[2]').send_keys("12f34")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseOne"]/div/form/button').click()
time.sleep(2)
if (driver.find_element_by_xpath('/html/body/div[1]').text) == 'Username or password wrong try again!':
    XLutils.writeData(path,'Sheet1',3,2,'Fail')
driver.close()

