from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import XLutils
##-------------------------------TEST CASE----------------------
## 1. Login to Manager Section

## 2. Adding new account and checking if it is visible in view panal or not

##3. Sending a Note to user

path='AllTestCases.xlsx'

driver = webdriver.Chrome()
driver.get('http://localhost/bank/')
driver.set_window_size(1420, 780)
##-------------------Logging as a manager--------------------
time.sleep(5)
driver.find_element_by_xpath('//*[@id="headingTwo"]/h5/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseTwo"]/div/form/input[1]').send_keys("manager@manager.com")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseTwo"]/div/form/input[2]').send_keys('manager')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="collapseTwo"]/div/form/button').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[3]/a').click()
time.sleep(2)
XLutils.writeData(path,'Sheet1',4,2,'pass')
##----------------Filling account Details-------------------- TESTCASE 2------------
time.sleep(15)
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/table/tbody/tr[1]/td[1]/input').send_keys('nikhil')
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/input').send_keys(123456)
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/table/tbody/tr[3]/td[1]/input').send_keys('Pune')
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/table/tbody/tr[3]/td[2]/input').send_keys('dy patil college')
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/table/tbody/tr[4]/td[1]/input').send_keys('nikhil@n.com')
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/table/tbody/tr[4]/td[2]/input').send_keys('1234')
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/table/tbody/tr[5]/td[1]/input').send_keys(52000)
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/table/tbody/tr[5]/td[2]/input').send_keys('Job')
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/table/tbody/tr[6]/td[1]/input').send_keys(1234567890)
select = Select(driver.find_element_by_name('branch'))
time.sleep(2)
driver.find_element_by_name('branch').click()
time.sleep(1)
select.select_by_value('1')
driver.find_element_by_name('branch').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/table/tbody/tr[7]/td/button[1]').click()

if driver.find_element_by_xpath('/html/body/div[1]').text == 'Account added Successfully':
    XLutils.writeData(path,'Sheet1',5,2,'pass')

##------Now going to the View panel to see whether the user is visible or not-------
time.sleep(5)
driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[1]/a').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr[5]/td[7]/a[2]').click()
time.sleep(8)
driver.find_element_by_name('notice').send_keys('Hii this is Manager!!')
time.sleep(2)
driver.find_element_by_name('send').click()
time.sleep(2)
if driver.find_element_by_xpath('/html/body/div/div/div[2]/div').text == 'Successfully send':
    XLutils.writeData(path,'Sheet1',6,2,'pass')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/form/a').click()
time.sleep(2)
driver.close()