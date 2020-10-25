from selenium import webdriver
import time
import random




driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.instagram.com/accounts/login/?hl=en')
time.sleep(6)
#name = 'Pocchiiii 😘' # do paste same emoji if name have any
user_name_element =  driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
user_name_element.send_keys('USername / id ') # username or id

pass_ele = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
pass_ele.send_keys('password')

login_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(6)
not_now = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(2)
turn_off_notification = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
time.sleep(1)
direct = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
time.sleep(4)

user = driver.find_element_by_xpath('//div[contains(text(), "Target_username")]').click() # target username

time.sleep(1)

list = ['', 'hii', 'hehe', 'ohhooo', 'lalalalalal']
i = 1
while i< 3001:
    try:
        msg_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        #a = random.randint(0, 4)

    except:
        continue
    msg_box.send_keys('message')
    send = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
    print('Mesaages sent - ',i)
    i += 1
    #time.sleep(1)
