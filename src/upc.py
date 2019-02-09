import sys
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def searchUpc(sku, browser):
    browser.get('https://upcdeal.us')
    browser.implicitly_wait(10)

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
        print("Not Found UPC")
        upc = ''
    return upc

if __name__ == '__main__':
    item_product = 'TNF03E0-URBNV-XS'
    upc = searchUpc(item_product)
    print(upc)
