from selenium import webdriver
import time
import random
from datetime import datetime




driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://web.whatsapp.com/')
time.sleep(6)
name = 'Parvez'
meme_lords =  driver.find_element_by_xpath("//span[@title='{}']".format(name)).click()
msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
time.sleep(2)

while True :
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    if current_time == 12:08:00.0 :
        try:
            send_msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
        except:
            continue
        msg.send_keys('lol ch')
        break

