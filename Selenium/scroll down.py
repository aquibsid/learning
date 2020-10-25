from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')

#1 scroll till 1000px
#driver.execute_script('window.scrollBy(0, 1000)','')

#2 scroll untill find the desired element
#flag = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img')
#driver.execute_script('arguments[0].scrollIntoView();',flag)

#3 scroll till the end of the page
#driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')