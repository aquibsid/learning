from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver  = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.amazon.in/')
# specify this one time in code
# wait for all element
driver.implicitly_wait(3) # wait untill site loading, 3 sec is enough
search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')

search.send_keys('laptop')

s_btn = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input')
s_btn.click()

driver.implicitly_wait(3)
#driver.close()

Cat_Asus = driver.find_element_by_xpath('//*[@id="p_89/ASUS"]/span/a/div/label/i').click()

hdd = driver.find_element_by_xpath('//*[@id="p_n_pattern_browse-bin/8609969031"]/span/a/div/label/i')
hdd.click()

sdd = driver.find_element_by_xpath('//*[@id="p_n_feature_eleven_browse-bin/7005059031"]/span/a/div/label/i').click()

graphics = driver.find_element_by_xpath('//*[@id="p_n_feature_seven_browse-bin/7005024031"]/span/a/div/label/i').click()

ram = driver.find_element_by_xpath('//*[@id="p_n_feature_browse-bin/1485945031"]/span/a/div/label/i').click()
