from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver  = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.google.com')

amazon_title = driver.title  #give site title

#time.sleep(3)

driver.get('https://www.amazon.in')
print(driver.title)

#time.sleep(3)
driver.back()
#time.sleep(3)

driver.forward()