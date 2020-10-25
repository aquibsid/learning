from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()

driver.get('https://www.onlinemictest.com/mouse-test/')

#to move mouse curser
tools = driver.find_element_by_xpath('//*[@id="menu-item-12"]/a')
Microphone_Test = driver.find_element_by_xpath('//*[@id="menu-item-273"]/a')
webcam_test = driver.find_element_by_xpath('//*[@id="menu-item-272"]/a')
sound_test = driver.find_element_by_xpath('//*[@id="menu-item-270"]/a')
key_board_test = driver.find_element_by_xpath('//*[@id="menu-item-271"]/a')
mouse_test = driver.find_element_by_xpath('//*[@id="menu-item-362"]/a')

time.sleep(2)
# mouse Hover 
actions = ActionChains(driver)
actions.move_to_element(tools).move_to_element(Microphone_Test).move_to_element(webcam_test).move_to_element(sound_test)\
    .move_to_element(key_board_test).move_to_element(mouse_test).click().perform()