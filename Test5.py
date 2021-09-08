# Test 5 -- Validating 'forgot / loss your password'
from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.common.keys import Keys 
driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe"); #Path given for the installed Chrome driver as I am using Google chrome
driver.maximize_window()
driver.get("https://platformrc.wyscout.com/app/")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login_username"]').send_keys("shantanursy@gmail.com")
driver.find_element_by_xpath('//*[@id="login_form"]/div/div/div[1]/div[2]/div[2]/div[1]/a').click()
print("Enter email address associated with Wyscout account")
time.sleep(10)
driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="password_recovery_container"]/iframe'))
time.sleep(2)
driver.find_element_by_xpath('//*[@id="search"]/input').send_keys("shantanursy@gmail.com") 
time.sleep(2)
driver.find_element_by_xpath('//*[@id="request"]/div/div[2]/div[2]/button').click()
screenshot = pyautogui.screenshot()
screenshot.save('image5.png')              #Additional verification as a screenshot of login page
time.sleep(2)
# driver.close() 