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
from src.toolReplace import *


def getAttribute(selenium_array, type):
    return [i.get_attribute(type) for i in selenium_array]

def parseElement(driver):
    item = setStructure()
    init = setConst()
    try:
        item['product'] = driver.find_elements_by_xpath('//ul[@class="product-details-accordion__list"]/li')[-1].text.replace("Item #", "")
        item['name'] = driver.find_element_by_xpath('//h1[@class="product-name qa-product-title"]').text
        item['brand'] = driver.find_element_by_xpath('//span[@class = "qa-brand-name"]').text
    except Exception as e:
        print(traceback.format_exc())
    runCsvList(init, ['replace_csv/Material.csv', 'replace_csv/name.csv'], ['Material', 'name'])

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.backcountry.com/patagonia-better-sweater-1-4-zip-fleece-jacket-womens?skid=PAT010V-TOM-XXS&ti=UExQIENhdDo6OjE6')
    parseElement(driver)
