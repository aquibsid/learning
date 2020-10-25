'''import test_class as ts


place_name = str(input('enter the city name: '))
obj = ts.profile(place_name)

obj.print_var()'''
import time

import selenium.webdriver.common.keys as Keys
from selenium import webdriver

driver  = webdriver.Chrome(executable_path='chromedriver.exe')
#driver.implicitly_wait(5)
#driver.maximize_window()
driver.get('https://www.google.com/')

search_bar = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
#time.sleep(1)
search_bar.send_keys('getstarted')
time.sleep(1)
search_btn = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]').click()

time.sleep(2)
driver.back()

time.sleep(2)
driver.forward()

time.sleep(10)

driver.close()