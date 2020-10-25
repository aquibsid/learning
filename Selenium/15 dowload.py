from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# set path for the download
chromeOptions = Options()
chromeOptions.add_experimental_option('pref', {'download.default_directory' : r'C:\Downloads\test_folder'})

driver  = webdriver.Chrome('chromedriver.exe')



