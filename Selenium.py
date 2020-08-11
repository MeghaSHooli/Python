import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/mhooli/Desktop/Automation/Drivers/77/chromedriver.exe')
driver.get('https://www.google.com')
time.sleep(3)
driver.find_element_by_xpath("//div[@class='FPdoLc tfB0Bf']//input[@name='btnK']").verifyElementPresent('Google Search')
driver.find_element_by_xpath("//input[@name='q']").sendkeys('abc')