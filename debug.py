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
    try:
        item['price'] = driver.find_element_by_xpath('//span[@class = "product-pricing__retail js-product-pricing__retail"]').text
        print("1")
    except:
        try:
            item['price'] = driver.find_element_by_xpath('//span[@class = "product-pricing__inactive js-product-pricing__inactive"]').text
            print("2")
        except:
            try:
                item['price'] = driver.find_element_by_xpath('//span[@class = "product-pricing__sale"]').text
                print("3")
            except:
                try:
                    item['price'] = driver.find_element_by_xpath('//span[@class = "product-pricing__retail"]').text
                    print("4")
                except Exception as e:
                    print(traceback.format_exc())

    print(item['price'])

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.backcountry.com/patagonia-active-hipster-brief-womens?skid=PAT02BG-SESTSMPK-XS&ti=U2VhcmNoIFJlc3VsdHM6UGF0YWdvbmlhIEFjdGl2ZSBIaXBzdGVyIEJyaWVmIC0gV29tZW4nczoxOjE6UGF0YWdvbmlhIEFjdGl2ZSBIaXBzdGVyIEJyaWVmIC0gV29tZW4ncw==')
    parseElement(driver)
