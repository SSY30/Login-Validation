from selenium import webdriver
import time
import pyautogui

from selenium.webdriver.common.keys import Keys 
driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe"); #Path given for the installed Chrome driver as I am using Google chrome
driver.maximize_window()
driver.get("https://platformrc.wyscout.com/app/")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login_form"]/div/div/div[2]/a[2]').click()
time.sleep(5)
screenshot = pyautogui.screenshot()
screenshot.save('image9.png') 
time.sleep(2)                    
driver.close()