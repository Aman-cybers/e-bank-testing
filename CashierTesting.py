from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import XLutils
##-------------------------------TEST CASE----------------------
##1. Enter Valid username and password in Cashier Login
##2. Checking that miney is withdrawing or not
##3. Checking that money is adding or not
path = 'AllTestCases.xlsx'
driver = webdriver.Chrome()
driver.get('http://localhost/bank/')
driver.set_window_size(1420, 780)
##----------------------------------Logging in as a cashier-----------------
time.sleep(5)
driver.find_element_by_xpath('//*[@id="headingThree"]/h5/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseThree"]/div/form/input[1]').send_keys("cashier@cashier.com")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseThree"]/div/form/input[2]').send_keys("cashier")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseThree"]/div/form/button').click()
time.sleep(5)
driver.find_element_by_name('otherNo').send_keys(1637857226)
time.sleep(3)
driver.find_element_by_name('get').click()
time.sleep(2)
XLutils.writeData(path,'Sheet1',9,2,'pass')
#-----------------Withdrawing Money-----------------------
driver.find_element_by_name('checkno').send_keys(1234)
time.sleep(4)
driver.find_element_by_name('amount').send_keys(5000)
time.sleep(3)
driver.find_element_by_name('withdraw').click()
time.sleep(2)
XLutils.writeData(path,'Sheet1',10,2,'pass')
#-----------------------Adding money-------------------------
driver.find_element_by_name('otherNo').send_keys(1637857226)
time.sleep(3)
driver.find_element_by_name('get').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/form[2]/input[3]').send_keys(1234)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/form[2]/input[4]').send_keys(5000)
time.sleep(3)
driver.find_element_by_name('deposit').click()
time.sleep(2)
XLutils.writeData(path,'Sheet1',11,2,'pass')
time.sleep(5)
driver.close()
