
import time

import password

obj = password.login()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = obj.user_name
passw = obj.passw
EXE_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=EXE_PATH)
driver.get("https://www.facebook.com")
element = driver.find_element_by_id("email")

element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(passw)
element.send_keys(Keys.RETURN)
element.close()


#element_f = driver.find_element_by_class_name('method':'class selector','l9j0dhe7 stjgntxs ni8dbmo4').click()
#element.send_keys(Keys.RETURN)
#driver.close()

