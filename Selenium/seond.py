from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver  = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.google.com')

print(driver.title) #give site title
print(driver.current_url) # give current url
print()
print(driver.page_source) # give HTML
element = driver.find_element_by_xpath('//*[@id="gsr"]')
element.send_Key('amazon')
time.sleep(10)
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()

#driver.close() # close current browser
#driver.quit() #close all the browser