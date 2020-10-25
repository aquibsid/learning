from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver  = webdriver.Chrome(executable_path='chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.expedia.com/')

flight = driver.find_element_by_xpath('//*[@id="uitk-tabs-button-container"]/li[2]/a')
flight.click()

time.sleep(1)

# flight departure city
flight_depature = driver.find_element_by_class_name('uitk-faux-input').click()
time.sleep(1)
from_city = driver.find_element_by_id('location-field-leg1-origin')
from_city.send_keys('Delhi')
time.sleep(1)
from_city_conf = driver.find_element_by_xpath('//*[@id="location-field-leg1-origin-menu"]/div[2]/ul/li[1]/button/div/div[1]').click()
time.sleep(1)

# flight destination city
flight_destination = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div/div/div/div[1]/button').click()
time.sleep(1)
flight_destination_city = driver.find_element_by_id('location-field-leg1-destination')
time.sleep(1)
flight_destination_city.send_keys('Miami')
time.sleep(1)
to_city_conf = driver.find_element_by_xpath('//*[@id="location-field-leg1-destination-menu"]/div[2]/ul/li[2]/button/div/div[1]').click()
time.sleep(1)

# dep date of the flight
dep_date = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div/div/button[1]').click()
time.sleep(2)
# selecting 18 aug for departure
dep_date_sel = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[4]/td[4]/button').click()
time.sleep(2)
dep_date_sel_done = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div[2]/button').click()
# arrival date of flight
arr_date = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/button[1]').click()
time.sleep(2)
# selecting returning date
arr_date_sel = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr[3]/td[7]/button').click()
time.sleep(2)
arr_date_sel_done = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]/button').click()

time.sleep(1)

search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[3]/div[2]/button').click()
time.sleep(10)

driver.close()
