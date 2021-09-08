# Validatrion to choose a plan
from selenium import webdriver
import time
import pyautogui

from selenium.webdriver.common.keys import Keys 
driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe"); #Path given for the installed Chrome driver as I am using Google chrome
driver.maximize_window()
driver.get("https://platformrc.wyscout.com/app/")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login_form"]/div/div/div[1]/div[3]/a').click()
time.sleep(2)
screenshot = pyautogui.screenshot()
screenshot.save('image7.png')  #Additional verification as a screenshot of login page
assert driver.find_element_by_xpath('//*[@id="menu-item-7402"]/a').is_displayed()==True
print("You can now start your free trial")        
driver.close()