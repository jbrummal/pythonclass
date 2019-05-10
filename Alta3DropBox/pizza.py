#!/usr/bin/python3

import time
import getpass

from selenium import webdriver

#https://sites.google.com/a/chromium.org/chromedriver/
browser = webdriver.Chrome(executable_path=r"C:\Users\Achimedes\Downloads\chromedriver_win32\chromedriver.exe")

browser.get("https://www.dominos.com/en/pages/customer/#!/customer/login/")

time.sleep(3)

useremailElm = browser.find_element_by_xpath('//*[@id="Email"]')
useremailElm.send_keys('rzfeeserspam@gmail.com')

passElm = browser.find_element_by_xpath('//*[@id="Password"]')
passElm.send_keys('PizzaPie123')

browser.find_element_by_xpath('//*[@id="customerLoginPage"]/div/div/div[2]/div/form/div[14]/div[1]/button').click()

time.sleep(3)

locElm = browser.find_element_by_xpath('//*[@id="_dpz"]/header/nav[1]/div[1]/ul/li[6]/a').click()

time.sleep(3)

stateElm = browser.find_element_by_name('Region')
stateElm.send_keys('PA')

for x in pagestotest:
    try:
        ## log in with selenium
    except:
        ## that page is unavail


