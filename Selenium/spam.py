from selenium import webdriver
import time
import random


list = ['hi', 'how are you', 'rich kid', 'ohhooo', 'lalalalalal','sasti','hello friend chai pi lo','memes bhej','la la mar gya m****d','hehehhe','arey ladke','evening class huh','bye','tata','khatm','ok']

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://web.whatsapp.com/')
time.sleep(6)
name = 'Richh' # do paste same emoji if name have any
meme_lords =  driver.find_element_by_xpath("//span[@title='{}']".format(name)).click()
msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
#time.sleep(2)

i = 0
while i < 1000:
    a = random.randint(0, 9)
    msg.send_keys(list[a])
    try:
        send_msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
    except:
        continue
    print(i)
    i+=1
    #time.sleep(2)
