from selenium import webdriver




driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.amazon.in/')
# .jpg, .jpeg use whatever you want
driver.save_screenshot(r'C:\Users\dhruv\Downloads\test_folder\sele2.png')


# this accept only .png ext
#driver.get_screenshot_as_file(r'C:\Users\dhruv\Downloads\test_folder/sele1.png')