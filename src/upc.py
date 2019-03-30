import sys
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def searchUpc(sku, browser):
    browser.implicitly_wait(5)

    browser.get('https://upcdeal.us')

    input = browser.find_element_by_xpath('//div[@class = "small-10 columns"]/input')
    input.send_keys(sku)

    # button
    browser.find_element_by_xpath('//button[@class = "button tiny postfix"]').click()

    # try:
    #     element = WebbrowserWait(browser, 10).until(
    #         EC.presence_of_element_located((By.ID, "containerprice"))
    #     )
    # except:
    #     browser.quit()

    try:
        upc = browser.find_element_by_xpath('//h1').text
        upc = re.split('[ \n]', upc)[1]
    except:
        try:
            upc = browser.find_element_by_xpath('//div[@class="medium-8 columns"]/h4/a').text
            upc = re.split(' ', upc)[0]
        except:
            print("Not Found UPC")
            upc = ''

    return upc

if __name__ == '__main__':
    item_product = 'PAT010V-BIRWH-S' # PAT010V-BIRWH-S#TNF03E0-URBNV-XS
    browser = webdriver.Chrome('../chromedriver.exe')
    upc = searchUpc(item_product, browser)
    print(upc)
