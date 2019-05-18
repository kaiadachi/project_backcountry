import sys
import time
import traceback
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.settings import *
from src.utility import *
from src.setupLogic import *
from src.parseLogic import *
from src.convert import *
from src.toolReplace import *

if __name__ == '__main__':
    init = setConst()
    df = pd.DataFrame(index=[])
    driver = setSelenium(init['single_url'])
    # trans_browser = webdriver.Chrome()
    # trans_browser.implicitly_wait(10)
    driver.implicitly_wait(10)

    df = parseElement(driver, df, init['folder'] + '_img')

    createCsv(df, init['folder'] + '_csv', init['csv_name'], True, ',')
    driver.close()
    # trans_browser.close()

    try:
        runCsvList(init, ['replace_csv/Material.csv', 'replace_csv/name.csv'], ['Material', 'name'])
    except:
        print('replace error !!!')

    convertAmazon()
