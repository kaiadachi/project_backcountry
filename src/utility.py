import requests
import pandas as pd

def saveImg(img_url, folder_name):
    if("https:" not in img_url):
        img_url = "https:" + img_url

    re = requests.get(img_url)

    img_name = img_url.split('/')[-1]
    with open("{0}/{1}".format(folder_name, img_name), 'wb') as f:
        f.write(re.content)

    return img_name


def getAttribute(selenium_array, type):
    return [i.get_attribute(type) for i in selenium_array]

def getLastPage(driver):
    last_page = driver.find_elements_by_xpath('//li[@class = "page-link page-number"]/a')[-1].text

    return int(last_page)

def goNext(driver, init_url):
    driver.get('{0}?page={1}'.format(init_url, i+1))

    return driver

def createCsv(data, name, folder_csv):
    try:
            data.to_csv('{0}/{1}'.format(folder_csv, name))
    except:
        try:
            data.to_csv('{0}/{1}'.format(folder_csv, name), encoding="Shift_jis")
        except:
            data.to_csv('{0}/{1}'.format(folder_csv, name), encoding="utf-8")
