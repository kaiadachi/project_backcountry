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

def setSelenium(target_url):
    # options = Options()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome()
    driver.get(target_url)

    return driver


def parseElement(driver):
    a = driver.find_elements_by_xpath('//div[@class = "ui-pli-wrap js-pli-wrap"]/a')


if __name__ == '__main__':
    driver = setSelenium('https://www.backcountry.com/the-north-face-arctic-parka-womens?skid=TNF03E0-URBNV-XS&ti=UExQIENhdDpXb21lbidzIENsb3RoaW5nIEJlc3QgU2VsbGVyczoxOjE6YmMtd29tZW5zLWNsb3RoaW5n')
    parseElement(driver)
