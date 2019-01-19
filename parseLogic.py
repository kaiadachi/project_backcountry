import pandas as pd
from utility import *

def parse(driver, item, df):
    item['name'] = driver.find_element_by_xpath('//span[@class = "qa-brand-name"]').text
    item['product'] = driver.find_element_by_xpath('//li[@class = "product-details-accordion__item-number product-details-accordion__bulletpoint"]').text
    try:
        item['price'] = driver.find_element_by_xpath('//span[@class = "product-pricing__retail js-product-pricing__retail"]').text
    except:
        item['price'] = ''


    size_selector = driver.find_elements_by_xpath('//*[@id="size-attribute-selector"]/ul[@class = "buybox-dropdown__options js-basedropdown__options"]/li')
    sizes = getAttribute(size_selector, 'data-attribute-selector-key')

    for size, btn in zip(sizes, size_selector):
        driver.find_element_by_xpath('//*[@id="product-size-select"]').click()
        btn.click()

        color_selector = driver.find_elements_by_xpath('//*[@id="color-attribute-selector"]/ul[@class = "buybox-dropdown__options js-basedropdown__options"]/li')
        stocks = getAttribute(color_selector, 'class')
        colors = getAttribute(color_selector, 'data-img-title')
        item['size'] = size

        for color, stock in zip(colors, stocks):
            if 'is-inactive' in stock:
                is_stock = 0
            else:
                is_stock = 1

            item['stock'] = is_stock
            item['color'] = color
            #print(item['name'], item['product'], item['price'], item['size'], item['color'], item['stock'])
            series = pd.Series(item)
            df = df.append(series, ignore_index = True)

    return df
