import sys
import time
import traceback
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from settings import *

def getAttribute(selenium_array, type):
    return [i.get_attribute(type) for i in selenium_array]

def getLastPage(driver):
    last_page = driver.find_elements_by_xpath('//li[@class = "page-link page-number"]/a')[-1].text

    return int(last_page)

def goNext(driver, init_url):
    driver.get('{0}?page={1}'.format(init_url, i+1))

    return driver

def setSelenium(target_url):
    # options = Options()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome()
    driver.get(target_url)

    return driver

def getHref(driver, last_page, limit):
    urls = []
    init_url = driver.current_url
    for i in range(last_page):
        selenium_urls = driver.find_elements_by_xpath('//div[@class = "ui-pli-wrap js-pli-wrap"]/a')
        urls = urls + getAttribute(selenium_urls, 'href')
        if len(urls) >= limit:
            urls = urls[0:limit]
            break
        driver = goNext(driver, init_url)

    return driver, urls

def parseElement(driver):
    item = setStructure()
    item['name'] = driver.find_element_by_xpath('//span[@class = "qa-brand-name"]').text

if __name__ == '__main__':
    init = setConst()
    driver = setSelenium(init['url'])
    last_page = getLastPage(driver)
    driver, urls = getHref(driver, last_page, init['limit'])
    for count, url in enumerate(urls):
        print("Now: {0}/{1}".format(count+1, init['limit']))
        driver.get(url)
        parseElement(driver)

    driver.close()
