# Test 1 -- Validating login credentials by entering valid input data
from selenium import webdriver
import time
import pyautogui

from selenium.webdriver.common.keys import Keys 
driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe"); #Path given for the installed Chrome driver as I am using Google chrome
driver.maximize_window()
driver.get("https://platformrc.wyscout.com/app/")
time.sleep(2)

# Test 1 -- Validating login credentials by entering valid data

driver.find_element_by_xpath('//*[@id="login_username"]').send_keys("shantanursy@gmail.com")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login_password"]').send_keys("pw_IndiaTest!")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login_button"]').click()
time.sleep(10)
assert driver.find_element_by_xpath('//*[@id="account_button"]/a').is_displayed()==True
print("Login successful")
screenshot = pyautogui.screenshot()
screenshot.save('image1.png')              #Additional verification as a screenshot of login page
driver.close()




