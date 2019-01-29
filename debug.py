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
    item['product'] = driver.find_element_by_xpath('//meta[@itemprop = "productID"]').get_attribute('content')

    print(item['product'])

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.backcountry.com/the-north-face-arctic-parka-womens?skid=TNF03E0-URBNV-XS&ti=UExQIENhdDpXb21lbidzIENsb3RoaW5nIEJlc3QgU2VsbGVyczoxOjE6YmMtd29tZW5zLWNsb3RoaW5n')
    parseElement(driver)
