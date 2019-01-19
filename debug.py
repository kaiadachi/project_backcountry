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

    size_selector = driver.find_elements_by_xpath('//*[@id="size-attribute-selector"]/ul[@class = "buybox-dropdown__options js-basedropdown__options"]/li')
    sizes = getAttribute(size_selector, 'data-attribute-selector-key')

    for size, btn in zip(sizes, size_selector):
        driver.find_element_by_xpath('//*[@id="product-size-select"]').click()
        btn.click()

        color_selector = driver.find_elements_by_xpath('//*[@id="color-attribute-selector"]/ul[@class = "buybox-dropdown__options js-basedropdown__options"]/li')
        stocks = getAttribute(color_selector, 'class')
        colors = getAttribute(color_selector, 'data-img-title')
        # size
        item['size'] = size
        print(item['size'])

        for color, stock in zip(colors, stocks):
            if 'is-inactive' in stock:
                is_stock = 0
            else:
                is_stock = 1

            item['stock'] = is_stock
            item['color'] = color

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.backcountry.com/the-north-face-arctic-parka-womens?skid=TNF03E0-URBNV-XS&ti=UExQIENhdDpXb21lbidzIENsb3RoaW5nIEJlc3QgU2VsbGVyczoxOjE6YmMtd29tZW5zLWNsb3RoaW5n')
    parseElement(driver)
