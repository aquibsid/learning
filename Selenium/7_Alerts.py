from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://testautomationpractice.blogspot.com/')

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
time.sleep(4)
#driver.switch_to_alert().accept() #click ok
driver.switch_to_alert().dismiss() # it is working

time.sleep(3)




driver.get('https://www.geeksforgeeks.org/')

#driver.find_elements_by_xpath('/html/body/div[8]/div[3]/div/div[1]/span').click()

time.sleep(30)
driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[1]/span').click()


