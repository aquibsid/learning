# How many links present on a page
# count and print them
# find a link on a page by the name od the link
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.vpnmentor.com/blog/10-best-torrent-websites/')

links = driver.find_elements_by_tag_name('a')
print('total links ',len(links))

'''for link in links:
    print(link.text)'''

# find link by Link Text

driver.find_element_by_link_text('The Pirate Bay').click()