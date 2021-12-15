from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import XLutils
##-------------------------------TEST CASE----------------------
##1. Checking whether a help notice is working or not
##2. Checking wheter that note is visible to the manager or not
path = 'AllTestCases.xlsx'
driver = webdriver.Chrome()
driver.get('http://localhost/bank/')
driver.set_window_size(1420, 780)

##--------------------Help Notice sending----------------------
time.sleep(5)
driver.find_element_by_xpath("//*[@id='headingOne']/h5/a/button").click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="collapseOne"]/div/form/input[1]').send_keys("a@a.com")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseOne"]/div/form/input[2]').send_keys("1234")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseOne"]/div/form/button').click()
time.sleep(4)
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[2]/div/div/a').click()
time.sleep(5)
driver.find_element_by_name('msg').send_keys('I want to close my account')
time.sleep(4)
driver.find_element_by_name('send').click()
time.sleep(4)
XLutils.writeData(path,'Sheet1',12,2,'pass')
driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/form/a[5]').click()

#---------------Ckecking that the help notice written by the user is visible to manager or not-------------
driver.find_element_by_xpath('//*[@id="headingTwo"]/h5/a').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="collapseTwo"]/div/form/input[1]').send_keys("manager@manager.com")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseTwo"]/div/form/input[2]').send_keys('manager')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseTwo"]/div/form/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[4]/a').click()
time.sleep(6)
XLutils.writeData(path,'Sheet1',13,2,'pass')
driver.close()