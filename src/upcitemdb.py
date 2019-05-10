import sys
import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def getAllUpc(name, browser):
    df_upc = pd.DataFrame(columns=['title', 'upc', 'color', 'size'])

    #browser.implicitly_wait(3)
    browser.get('https://www.upcitemdb.com/')

    input = browser.find_element_by_id('searchinput')
    input.send_keys(name)

    browser.find_element_by_xpath('//button[@class = "input-group-addon btn btn-primary btn-search"]').click()

    count = 1
    df_upc = recurseUPC(df_upc, browser, count, name)

    df_upc.to_csv('df_upc.csv')

    return df_upc

def recurseUPC(df_upc, browser, count, name):

    upc = browser.find_elements_by_xpath('//div[@class="rImage"]/a')
    title = browser.find_elements_by_xpath('//div[@class="rImage"]/p')

    print('##{}----------------'.format(count))
    info = {
        'title': '',
        'upc': '',
        'color': '',
        'size': ''
    }
    for t, u in zip(title, upc):
        isName = (name in t.text)
        if(isName):
            print(t.text)
            print(u.text)
            info['title'] = t.text
            info['upc'] = u.text
            str_replace = t.text.replace(name + ' ', '')
            str_split = str_replace.split(', ')
            info['color'] = str_split[0]
            info['size'] =  str_split[1]
            df_upc = df_upc.append(info, ignore_index = True)

    count = count + 1
    try:
        browser.find_element_by_xpath( '//div[@class = "page"]/a[{}]'.format(count) ).click()
        return recurseUPC(df_upc, browser, count, name)
    except:
        return df_upc
    
def findMatchedUPC(name, size, color, df_upc):
    df_size = df_upc[df_upc['size'] == size]
    for c in re.split('[/ \n,]', color):
        print('{0} -> {1}'.format(color, c))
        df_size_color = df_size[df_size['color'].str.contains(c)]
        length = len(df_size_color)
        if(length != 0):
            upc = df_size_color['upc'].iloc[0]
            drop_id = df_size_color.index[0]
            df_upc_new = df_upc.drop(index=drop_id)
            return upc, df_upc_new
    
    print('not found')
    return 0, df_upc
    
    
# def searchUpc(name, size, color, browser):
#     target = '{0} {1}, {2}'.format(name, color, size)
#     browser.implicitly_wait(3)

#     browser.get('https://www.upcitemdb.com/')

#     input = browser.find_element_by_id('searchinput')
#     input.send_keys(target)

#     # button
#     browser.find_element_by_xpath('//button[@class = "input-group-addon btn btn-primary btn-search"]').click()

#     try:
#         print('info')
#         upc = browser.find_element_by_xpath('//div[@class="rImage"]/a').text
#         title = browser.find_element_by_xpath('//div[@class="rImage"]/p').text

        

#         isName = (name in title)
#         isSize = (size in title)
#         isColor = (color in title)

#         judge = isName and isSize and isColor

#         if(judge):
#             return upc
#         else:
#             return ''
#     except:
#         return ''

if __name__ == '__main__':
    start = time.time()

    name = "Patagonia Torrentshell Jacket - Women's"
    color = 'Cobalt Blue'
    size = 'XS'

    options = Options()
    if(False):
        options.add_argument('--headless')

    # browser = webdriver.Chrome('../chromedriver.exe', chrome_options=options)
    # df_upc = getAllUpc(name, browser)
    df_upc = pd.read_csv('df_upc.csv', encoding='shift-jis')
    print('findMatchedUPC')
    upc, df_upc = findMatchedUPC(name, size, color, df_upc)
    print(upc)
    upc, df_upc = findMatchedUPC(name, size, color, df_upc)
    print(upc)

    elapsed_time = time.time() - start
    print ("elapsed_time:{0:.3f}".format(elapsed_time) + "[sec]")