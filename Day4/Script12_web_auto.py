#!/usr/bin/python3
"""
Author: Jason Brummal
Create date: 
Purpose:
"""

from selenium import webdriver
import getpass
import time

# --Constant

def main():
    profile = webdriver.FirefoxProfile()
    browser = webdriver.Firefox(executable_path=r"C:\Users\brummja\Downloads\geckodriver.exe")


    browser.get("https://www.dominos.com/en/pages/customer/#!/customer/login/")

    time.sleep(10)
    # --Use the INSPECT in the browser and then copy the xpath variable here
    useremailElm = browser.find_element_by_xpath('//*[@id="Email"]')
    useremailElm.send_keys("jason.brummal@gmail.com")

    passElm = browser.find_element_by_xpath('//*[@id="Password"]')
    passElm.send_keys("test")

# --Run it
main()