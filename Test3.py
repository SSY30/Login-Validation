# Test 3 -- Validating login when Login username is incorrect / invalid but password is correct
from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.common.keys import Keys 
driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe"); #Path given for the installed Chrome driver as I am using Google chrome
driver.maximize_window()
driver.get("https://platformrc.wyscout.com/app/")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login_username"]').send_keys("shantanursygmail.com")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login_password"]').send_keys("pw_IndiaTest!")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login_button"]').click()
time.sleep(2)
print("Invalid username or password")
screenshot = pyautogui.screenshot()
screenshot.save('image3.png')              #Additional verification as a screenshot of login page
time.sleep(2)
driver.close()