from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import XLutils
path = 'AllTestCases.xlsx'
##-------------------------------TEST CASE----------------------
##1. Checking that the note is visible or not (send by the manager)

##2. Checking that the Fund is transferring to another account or not!

driver = webdriver.Chrome()
driver.get('http://localhost/bank/')
driver.set_window_size(1420, 780)
##----------------TEST CASE 1
time.sleep(5)
driver.find_element_by_xpath("//*[@id='headingOne']/h5/a/button").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseOne"]/div/form/input[1]').send_keys("a@a.com")
#time.sleep(1)
driver.find_element_by_xpath('//*[@id="collapseOne"]/div/form/input[2]').send_keys("1234")
time.sleep(5)
driver.find_element_by_xpath('//*[@id="collapseOne"]/div/form/button').click()
time.sleep(5)

if driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/p').text == 'Latest Notification: Hii this is Manager!!':
    XLutils.writeData(path,'Sheet1',7,2,'pass')

##-------------------TEST CASE 2-------------------
time.sleep(3)
driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[4]/a').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/input').send_keys(1637857226)
time.sleep(5)
driver.find_element_by_name('get').click()
time.sleep(3)
driver.find_element_by_name('amount').send_keys(1000)
time.sleep(5)
driver.find_element_by_name('transferSelf').click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/form/a[5]').click()
time.sleep(5)

driver.find_element_by_xpath("//*[@id='headingOne']/h5/a/button").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseOne"]/div/form/input[1]').send_keys("r@r.com")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseOne"]/div/form/input[2]').send_keys("1234")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseOne"]/div/form/button').click()
time.sleep(8)
XLutils.writeData(path,'Sheet1',8,2,'pass')
driver.close()
