#!/bin/pyhon3
import os
os.system('pip3 install selenium')
os.system('pip3 install fake-useragent')
os.system('pip3 install pypasser')

import time as sleepy
import sys
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from fake_useragent import UserAgent
from pypasser import reCaptchaV3
from pypasser import reCaptchaV2

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
    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    #print(profile)
    browser.get("https://storware.eu/licenses/vprotect/trial/")
    sleepy.sleep(20)
    perhost = browser.find_element_by_xpath("/html/body/app-root/app-layout/app-license-wizard/form/div[1]/div/div/app-license-wizard-form-models/div/div/div[1]/label")
    perhost.click()
    hyper = browser.find_element_by_xpath("/html/body/app-root/app-layout/app-license-wizard/form/div[1]/div/div/accordion/accordion-group[1]/div/div[1]/div/div/div")
    hyper.click()
    esxi = browser.find_element_by_xpath("/html/body/app-root/app-layout/app-license-wizard/form/div[1]/div/div/accordion/accordion-group[1]/div/div[2]/div/app-license-wizard-form-virtual-platforms/div/div/div[5]/div[1]/div/label")
    esxi.click()
    esxi_host = browser.find_element_by_xpath("/html/body/app-root/app-layout/app-license-wizard/form/div[1]/div/div/accordion/accordion-group[1]/div/div[2]/div/app-license-wizard-form-virtual-platforms/div/div/div[5]/div[2]/input")
    esxi_host.send_keys("2")
    next_step = browser.find_element_by_xpath('//*[@id="proceedButton"]')
    next_step.click()
    sleepy.sleep(35)
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
    zipcode = browser.find_element_by_xpath('//*[@id="zipCode"]')
    zipcode.send_keys("91119")
    country = browser.find_element_by_xpath("/html/body/app-root/app-layout/app-registration-form/form/div/div[1]/div/div[7]/div[3]/ngx-select-dropdown/div")
    country.send_keys("Israel")
    country_name = browser.find_element_by_xpath("/html/body/app-root/app-layout/app-registration-form/form/div/div[1]/div/div[7]/div[3]/ngx-select-dropdown/div/div/ul[1]/li")
    country_name.click()
    privacy = browser.find_element_by_xpath("/html/body/app-root/app-layout/app-registration-form/form/div/div[2]/div/div[2]/label")
    privacy.click()
    cap = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]")
    cap.click()
    get_license = browser.find_element_by_xpath("/html/body/app-root/app-layout/app-registration-form/form/div/div[2]/div/button")
    get_license.click()
    sleepy.sleep(5)
    browser.close() #Remove comment at end testing

    bumps = bumps + 1

    print(time, ": Work.       ( work", bumps, ")")
    print()
    #exit 0
    countdown = 86400

    for i in range(0, 8):
        minutes = countdown / 60
        countdown = countdown - 900
        print('Next bump in: ', minutes, 'minutes.' )
        sleepy.sleep(900)
