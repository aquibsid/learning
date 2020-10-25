from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver  = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.google.com')

Search_ele = driver.find_element_by_name('q')

print(Search_ele.is_displayed()) # give True/False
print(Search_ele.is_enabled()) # give True/False

Search_btn_ele = driver.find_element_by_name('btnK') # Search button

print(Search_btn_ele.is_displayed()) # give True/False
print(Search_btn_ele.is_enabled()) # give True/False

Search_ele.send_keys('Amazon')
time.sleep(1)
Search_btn_ele.click()


# to use the CSS selector, value is diff here
#roundtrip = driver.find_element_by_css_selector('input[value=roundTrip]')
#roundtrip.is_selected()
