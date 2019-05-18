import sys
import time
import traceback
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.settings import *
from src.utility import *
from src.parseLogic import *
from src.convert import *
from src.toolReplace import *
from src.setupLogic import *

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
        driver = goNext(driver, init_url, i)

    return driver, urls

def parseElement(driver, df, folder_img):
    item = setStructure()
    df = parse(driver, item, df, folder_img)

    return df

def getLastPage(driver):
    last_page = driver.find_elements_by_xpath('//li[@class = "page-link page-number"]/a')[-1].text

    return int(last_page)

def goNext(driver, init_url, i):
    driver.get('{0}?page={1}'.format(init_url, i+1))

    return driver
