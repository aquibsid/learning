import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='chromedriver.exe')


driver.get('https://www.roboform.com/filling-test-all-fields')

drop = Select(driver.find_element_by_name("40cc__type"))
# select drop down
#drop.select(element)
drop.select_by_value('1')

time.sleep(3)
# method 1 select by visible text
drop.select_by_visible_text('Master Card')
time.sleep(3)
# method 2 select by Index
drop.select_by_index(5)
time.sleep(3)
# method 3 select by value
drop.select_by_value('4')

# capture all options of drop down list and print them
all_options = drop.options
print(len(all_options))

for option in all_options:
    print(option.text)