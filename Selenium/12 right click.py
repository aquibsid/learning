from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.onlinemictest.com/mouse-test/')
driver.maximize_window()

ele = driver.find_element_by_xpath('//*[@id="mouse"]')

action = ActionChains(driver)

# right click action
action.context_click(ele).perform()