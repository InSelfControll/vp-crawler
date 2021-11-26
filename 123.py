import time as sleepy
import sys
import os
import subprocess
import pkg_resources

list_installed = {"selenium", "fake-useragent","webdriver_manager", "pyvirtualdisplay"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = list_installed - installed
if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', * missing], 
            stdout = subprocess.DEVNULL)
#for x in list_installed:
    #print(x)
    #sleepy.sleep(3)
    #installed = os.system('pip3 freeze | cut -d"=" -f1 | grep x')
    #installed = os.system('pip3 show list_installed[x] | grep "Name: list_installed[x]" | cut -d" " -f2')
    #installed = os.system('pip3 list x | cut -d" " -f2')
    #installed = subprocess.checkcall([sys.executable, '-m', 'pip3', 'install',
 #   installed = sys.modules
  #  if x not in installed:
   #     print("Starting installation")
#        os.system('pip3 install selenium')
 #       os.system('pip3 install fake-useragent')
  #      os.system('pip3 install pypasser')
   #     os.system('pip3 install pyvirtualdisplay')
    #    os.system('pip3 install webdriver-manager')

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
    pass


from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from pyvirtualdisplay import Display

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
with Display() as display:
    while 1:
        options = Options()
        ua = UserAgent()
        UserAgent = ua.random
        profile = webdriver.FirefoxProfile()
        # options.headless = True
        profile.set_preference("general.useragent.override",
                               "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0")
        profile.set_preference("dom.webdriver.enabled", False)
        profile.set_preference("useAutomationExtension", False)
        profile.set_preference("marionette.enabled", False)
        profile.update_preferences()
        browser = webdriver.Firefox(firefox_profile=profile, options=options)
        # s = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
        # browser = webdriver.Chrome(service=s)
        browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        browser.get("https://licenses.storware.eu/vprotect/")
        sleepy.sleep(5)
        div = browser.find_element(By.XPATH, '//*[@id="post-3341"]/section[2]/div/div/div/div[2]/div')
        a = div.find_element(By.TAG_NAME, 'a')
        browser.execute_script("arguments[0].click();", a)
        iframe = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, 'calculatorFrame')))
        browser.switch_to.frame(iframe)
        WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, 'proceedButton')))
        a = browser.find_element(By.ID, 'licenseModel1')
        browser.execute_script("arguments[0].click();", a)
        sleepy.sleep(2)
        a = browser.find_element(By.XPATH,
                                 '/html/body/app-root/app-layout/app-license-wizard/form/div[1]/div/div/accordion/accordion-group[1]/div/div[1]/div/div/div')
        browser.execute_script("arguments[0].click();", a)
        sleepy.sleep(2)
        a = browser.find_element(By.ID, 'Esxi')
        browser.execute_script("arguments[0].click();", a)
        sleepy.sleep(2)
        browser.find_element(By.XPATH,
                             '/html/body/app-root/app-layout/app-license-wizard/form/div[1]/div/div/accordion/accordion-group[1]/div/div[2]/div/app-license-wizard-form-virtual-platforms/div/div/div[5]/div[2]/input').send_keys(
            '4')
        sleepy.sleep(2)
        a = browser.find_element(By.ID, 'proceedButton')
        browser.execute_script("arguments[0].click();", a)
        sleepy.sleep(5)
        fname = browser.find_element_by_xpath('//*[@id="first-name"]')
        lname = browser.find_element_by_xpath('//*[@id="last-name"]')
        fname.send_keys("David")
        lname.send_keys("Saharov")
        email = browser.find_element_by_xpath('//*[@id="email"]')
        email.send_keys('vp@bhop-il.net')  # Add your email
        sleepy.sleep(2)
        company_name = browser.find_element_by_xpath('//*[@id="company"]')
        company_name.send_keys('bhop-il')  # Add your password
        sleepy.sleep(2)
        mobile = browser.find_element_by_xpath('//*[@id="phone"]')
        mobile.send_keys("+97250000005")
        address = browser.find_element_by_xpath('//*[@id="address"]')
        address.send_keys("Jerusalem 22 Israel")
        city = browser.find_element_by_xpath('//*[@id="city"]')
        city.send_keys("Tel Aviv")
        role = browser.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-registration-form/form/div/div[1]/div/div[3]/div[2]/select/option[8]")
        role.click()
        zipcode = browser.find_element_by_xpath('//*[@id="zipCode"]')
        zipcode.send_keys("91119")
        country = browser.find_element_by_xpath(
            '//*[@id="app"]/app-root/app-layout/app-registration-form/form/div/div[1]/div/div[7]/div[3]/ngx-select-dropdown/div/button')
        country.click()
        country.send_keys(Keys.TAB)
        for xx in range(0, 107):
            country.send_keys(Keys.DOWN)
        country.send_keys(Keys.RETURN)

#        a = browser.find_element(By.ID, 'newsletterCheckbox')
 #       browser.execute_script("arguments[0].click();", a)
        a = browser.find_element(By.ID, 'privacyCheckbox')
        browser.execute_script("arguments[0].click();", a)
        try:
            browser.switch_to.frame(browser.find_element(By.XPATH,
                                                         '/html/body/app-root/app-layout/app-registration-form/form/div/div[2]/div/div[3]/re-captcha/div/div/iframe'))
        except:
            x = browser.find_element(By.ID, 'ngrecaptcha-0')
            x = x.find_elements(By.TAG_NAME, 'iframe')
            browser.switch_to.frame(x[0])
        sleepy.sleep(1)
        browser.execute_script(
            "var ele = document.getElementById('recaptcha-anchor'); ele.click(); console.log(ele, 'Done');")
        input('Was recaptcha handled?')
        browser.switch_to.default_content()
        sleepy.sleep(1)
        browser.switch_to.frame(browser.find_element(By.ID, 'calculatorFrame'))
        sleepy.sleep(1)
        a = browser.find_element(By.XPATH,
                                 '//*[@id="app"]/app-root/app-layout/app-registration-form/form/div/div[2]/div/button')
        browser.execute_script("arguments[0].click();", a)
        sleepy.sleep(10)

        browser.close()

        bumps = bumps + 1

        print(time, ": Work.       ( work", bumps, ")")
        print()
        days = 59
        start_time = sleepy.time()
        print(f'Starting sleep for {days} days')
        while True:
            if sleepy.time() - start_time > days*86400:
                break

