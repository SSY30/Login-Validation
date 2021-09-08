# Test 2 - Trying to login when already the account is logged in

from selenium import webdriver
import time
import pyautogui

from selenium.webdriver.common.keys import Keys 
driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe"); #Path given for the installed Chrome driver as I am using Google chrome
driver.maximize_window()

driver.get("https://platformrc.wyscout.com/app/")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login_username"]').send_keys("shantanursy@gmail.com")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login_password"]').send_keys("pw_IndiaTest!")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login_button"]').click()
time.sleep(10)
screenshot = pyautogui.screenshot()
screenshot.save('image2.png')                  # #Additional verification as a screenshot of login page
print('Multiple access attempt')  
time.sleep(5)
driver.find_element_by_xpath('//*[@id="login_restrictor_dialog_container"]/div/div[2]/button').click() #To click force login button
time.sleep(5)
driver.close()

