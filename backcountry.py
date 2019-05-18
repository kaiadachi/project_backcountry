import sys, os
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

if __name__ == '__main__':
    init = setConst()
    df_name = '{}_csv/{}'.format(init['folder'], init['csv_name'] )
    isFile = os.path.isfile(df_name)
    if(isFile):
        df = pd.read_csv(df_name, encoding="shift-jis")
        df.loc[df['parent_child']=='child', 'stock'] = 0
    else:
        df = pd.DataFrame(index=[])

    driver = setSelenium(init['url'])
    driver.implicitly_wait(10)

    # 翻訳用ブラウザ
    # trans_browser = webdriver.Chrome()
    # trans_browser.implicitly_wait(10)

    last_page = getLastPage(driver)
    driver, urls = getHref(driver, last_page, init['limit'])

    print('taget_url:', len(urls))

    for count, url in enumerate(urls):
        print("Now: {0}/{1}".format(count+1, init['limit']))
        driver.get(url)

        try:
            df = parseElement(driver, df, init['folder'] + '_img')
        except Exception as e:
            print(traceback.format_exc())

    createCsv(df, init['folder'] + '_csv', init['csv_name'], True, ',')
    driver.close()
    # trans_browser.close()

    try:
        runCsvList(init, ['replace_csv/Material.csv', 'replace_csv/name.csv'], ['Material', 'name'])
    except:
        print('replace error !!!')

    convertAmazon()
