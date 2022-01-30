#!/bin/pyhon3
import os
os.system('pip3 install selenium')
os.system('pip3 install fake-useragent')
os.system('pip3 install pypasser')

import time as sleepy
import sys
from selenium.webdriver.chrome.service import Service
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from fake_useragent import UserAgent
from pypasser import reCaptchaV3
from pypasser import reCaptchaV2
from selenium.webdriver.support.ui import Select

now = datetime.now()
time = now.strftime('%H:%M')
bumps = 0

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
    pass

print('\n\n\n\n')
print("         Welcome to vProtect license script.\n")
print("This will send info to vprotect trail every 59 days..")
print()
while 1:
    options = Options()
    ua = UserAgent()
    UserAgent = ua.random
    #print(UserAgent)
    #options.add_argument(f'user-agent={UserAgent})')
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override","Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0")
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference("useAutomationExtension", False)
    profile.set_preference("marionette.enabled", False)
    profile.update_preferences()
    browser = webdriver.Firefox(firefox_profile=profile)
    # s = Service('./chromedriver.exe')
    # browser = webdriver.Chrome(service=s)
    browser.maximize_window()
    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    browser.get("https://storware.eu/licenses/vprotect/trial/")
    sleepy.sleep(10)
    browser.switch_to.frame(browser.find_element(By.ID, 'calculatorFrame'))
    browser.execute_script("document.getElementsByClassName('custom-control custom-radio custom-control-inline')[0].children[0].click()")
    browser.execute_script("document.getElementsByClassName('panel card panel-default')[0].children[0].click()")
    browser.execute_script("document.getElementsByClassName('custom-control custom-checkbox')[4].children[0].click()")
    value = browser.execute_script("return document.getElementsByClassName('form-control ng-untouched ng-pristine ng-valid')[0]")
    try:
        value.send_keys(Keys.CONTROL + 'a')
        value.send_keys('2')
    except:
        value.click()
        value.send_keys(Keys.CONTROL + 'a')
        value.send_keys('2')

    browser.switch_to.default_content()
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleepy.sleep(10)
    browser.switch_to.frame(browser.find_element(By.ID, 'calculatorFrame'))
    sleepy.sleep(1)
    try:
        zbtn = browser.find_element(By.ID, 'proceedButton')
        print(f'1. {zbtn.text}')
        zbtn.click()
        try:
            print(browser.execute_script("return document.getElementById('proceedButton').textContent"))
            browser.execute_script("document.getElementById('proceedButton').click()")
        except:
            pass
    except:
        pass
    sleepy.sleep(4)



    fname = browser.find_element_by_xpath('//*[@id="first-name"]')
    lname = browser.find_element_by_xpath('//*[@id="last-name"]')
    fname.send_keys("David")
    lname.send_keys("Saharov")
    email = browser.find_element_by_xpath('//*[@id="email"]')
    email.send_keys('vp@bhop-il.net')#   Add your email
    sleepy.sleep(2)
    company_name = browser.find_element_by_xpath('//*[@id="company"]')
    company_name.send_keys('bhop-il')                  #   Add your password
    sleepy.sleep(2)
    mobile = browser.find_element_by_xpath('//*[@id="phone"]')
    mobile.send_keys("+97250000005")
    address = browser.find_element_by_xpath('//*[@id="address"]')
    address.send_keys("Jerusalem 22 Israel")
    city = browser.find_element_by_xpath('//*[@id="city"]')
    city.send_keys("Tel Aviv")
    role = browser.find_element_by_xpath("/html/body/app-root/app-layout/app-registration-form/form/div/div[1]/div/div[3]/div[2]/select/option[8]")
    role.click()
    zipcode = browser.find_element_by_xpath('//*[@id="zipCode"]')
    zipcode.send_keys("91119")
    sleepy.sleep(2)
    country = browser.execute_script("return document.getElementsByClassName('ngx-dropdown-button')[0]")
    country.click()
    country.send_keys(Keys.TAB)
    for i in range(0, 107):
        country.send_keys(Keys.DOWN)
    sleepy.sleep(2)
    country.send_keys(Keys.RETURN)

    browser.execute_script("document.getElementsByClassName('custom-control custom-checkbox')[1].children[0].click()")

    cap = browser.execute_script("return document.getElementsByClassName('custom-control custom-checkbox')[1].nextElementSibling.children[0]")
    cap = cap.find_elements(By.TAG_NAME, 'iframe')[0]

    browser.switch_to.frame(cap)

    browser.execute_script("document.getElementsByClassName('recaptcha-checkbox-border')[0].click()")
    sleepy.sleep(5)

    browser.switch_to.default_content()
    browser.switch_to.frame(browser.find_element(By.ID, 'calculatorFrame'))

    sleepy.sleep(5)
    get_license = browser.find_element_by_xpath("/html/body/app-root/app-layout/app-registration-form/form/div/div[2]/div/button")
    get_license.click()
    sleepy.sleep(5)
    browser.close() #Remove comment at end testing

    bumps = bumps + 1

    print(time, ": Work.       ( work", bumps, ")")
    print()
    countdown = 86400

    for i in range(0, 8):
        minutes = countdown / 60
        countdown = countdown - 900
        print('Next bump in: ', minutes, 'minutes.' )
        sleepy.sleep(900)
       
