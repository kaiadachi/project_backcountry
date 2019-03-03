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

def parseElement(driver, df, folder_img, trans_browser):
    item = setStructure()
    df = parse(driver, item, df, folder_img, trans_browser)

    return df

if __name__ == '__main__':
    init = setConst()
    df = pd.DataFrame(index=[])
    driver = setSelenium(init['url'])
    trans_browser = webdriver.Chrome()
    trans_browser.implicitly_wait(10)
    driver.implicitly_wait(10)
    last_page = getLastPage(driver)
    driver, urls = getHref(driver, last_page, init['limit'])

    for count, url in enumerate(urls):
        print("Now: {0}/{1}".format(count+1, init['limit']))
        driver.get(url)
        df = parseElement(driver, df, init['folder'] + '_img', trans_browser)

    createCsv(df, init['folder'] + '_csv', init['csv_name'], True, ',')
    driver.close()
    trans_browser.close()

    try:
        runCsvList(init, ['replace_csv/Material.csv', 'replace_csv/name.csv'], ['Material', 'name'])
    except:
        print('replace error !!!')

    convertAmazon()
