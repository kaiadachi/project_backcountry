import sys
import time
import traceback
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from settings import *
from utility import *
from parseLogic import *


def getAttribute(selenium_array, type):
    return [i.get_attribute(type) for i in selenium_array]

def parseElement(driver):
    item = setStructure()


    color_selector = driver.find_elements_by_xpath('//*[@id="color-attribute-selector"]/ul[@class = "buybox-dropdown__options js-basedropdown__options"]/li')
    colors = getAttribute(color_selector, 'data-img-title')


    for color, btn in zip(colors, color_selector):
        driver.find_element_by_xpath('//*[@id="product-color-select"]').click()
        btn.click()

        size_selector = driver.find_elements_by_xpath('//*[@id="size-attribute-selector"]/ul[@class = "buybox-dropdown__options js-basedropdown__options"]/li')
        stocks = getAttribute(size_selector, 'class')
        sizes = getAttribute(size_selector, 'data-attribute-selector-key')

        item['color'] = color

        for size, stock in zip(sizes, stocks):
            if 'is-inactive' in stock:
                is_stock = 0
            else:
                is_stock = 1

            item['stock'] = is_stock
            item['size'] = size

            print(item['color'], item['stock'], item['size'])

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.backcountry.com/the-north-face-arctic-parka-womens?skid=TNF03E0-URBNV-XS&ti=UExQIENhdDpXb21lbidzIENsb3RoaW5nIEJlc3QgU2VsbGVyczoxOjE6YmMtd29tZW5zLWNsb3RoaW5n')
    parseElement(driver)
