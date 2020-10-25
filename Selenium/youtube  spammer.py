from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://youtu.be/kP5AJ6mozJw")
time.sleep(4)
chat = driver.find_element_by_xpath('//*[@id="button"]').click()
chat.send_keys('big fan')


