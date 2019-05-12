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


def getAttribute(selenium_array, type):
    return [i.get_attribute(type) for i in selenium_array]

def parseElement(driver):
    item = setStructure()
    init = setConst()
    try:
        item['price'] = driver.find_element_by_xpath('//span[@class = "product-pricing__retail js-product-pricing__retail"]').text
    except:
        try:
            item['price'] = driver.find_element_by_xpath('//span[@class = "product-pricing__inactive js-product-pricing__inactive"]').text
        except:
            try:
                item['price'] = driver.find_element_by_xpath('//span[@class = "product-pricing__sale"]').text
            except:
                try:
                    item['price'] = driver.find_element_by_xpath('//span[@class = "product-pricing__retail"]').text
                except Exception as e:
                    print(traceback.format_exc())

    item['price'] = item['price'].replace('$', '')
    item['price'] = item['price'].replace(',', '')
    print(item['price'])
    if float(item['price']) < 50.0:
        item['price'] = float(item['price']) * init['highweight']
    else:
        item['price'] = float(item['price']) * init['weight']

    print(item['price'])

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.backcountry.com/patagonia-better-sweater-1-4-zip-fleece-jacket-womens?skid=PAT010V-TOM-XXS&ti=UExQIENhdDo6OjE6')
    parseElement(driver)
