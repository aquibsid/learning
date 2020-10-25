from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()

driver.get('https://www.seleniumeasy.com/test/drag-and-drop-demo.html')

drag = driver.find_element_by_xpath('//*[@id="todrag"]/span[2]')
drop1 = driver.find_element_by_xpath('//*[@id="mydropzone"]')
#time.sleep(1)
action = ActionChains(driver)
action.drag_and_drop(drag, drop1).perform()