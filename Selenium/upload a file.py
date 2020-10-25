from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()

driver.get('http://testautomationpractice.blogspot.com/')


driver.switch_to_frame(0)
choose_file = driver.find_element_by_xpath('//*[@id="RESULT_FileUpload-10"]')
choose_file.send_keys(r'C:\Users\dhruv\Downloads\ship.jpg')
