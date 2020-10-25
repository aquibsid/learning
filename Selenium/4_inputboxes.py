import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.roboform.com/filling-test-all-fields')

#inputboxes = driver.find_elements_by_class_name('col-xs-6')
#print(len(inputboxes))

title = driver.find_element_by_name('01___title')
title.send_keys('Fuck OFF')

time.sleep(5)
driver.close()