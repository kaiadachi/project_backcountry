import sys
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def searchUpc(sku):
    driver = webdriver.Chrome()
    driver.get('https://upcdeal.us')
    driver.implicitly_wait(20)

    input = driver.find_element_by_xpath('//div[@class = "small-10 columns"]/input')
    input.send_keys(sku)

    # button
    driver.find_element_by_xpath('//button[@class = "button tiny postfix"]').click()

    # try:
    #     element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.ID, "containerprice"))
    #     )
    # except:
    #     driver.quit()

    upc = driver.find_element_by_xpath('//h1').text
    upc = re.split('[ \n]', upc)[1]
    driver.close()
    return upc

if __name__ == '__main__':
    item_product = 'TNF03E0-URBNV-XS'
    upc = searchUpc(item_product)
    print(upc)
