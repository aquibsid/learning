from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')

# neet to verify we are able to delete and create cookie
driver.get('https://www.amazon.in/')

# capture all cookie

cookies = driver.get_cookies()
print(len(cookies))
print(cookies) # print all the cookie on page

# adding new cookie to the browser
cookie ={'name':'Mycookie', 'value':'1234567890'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))
print(cookies) # print all the cookie on page


# deleting the cookie, name of cookie is req
driver.delete_cookie('Mycookie')

cookies = driver.get_cookies()
print(len(cookies))
print(cookies) # print all the cookie on page


# deleting all the cookie
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))
#print(cookies) # print all the cookie on page