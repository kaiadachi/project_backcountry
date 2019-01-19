import pandas as pd
import time
from utility import *

def parse(driver, item, df, folder_name):
    item['name'] = driver.find_element_by_xpath('//span[@class = "qa-brand-name"]').text
    item['product'] = driver.find_element_by_xpath('//li[@class = "product-details-accordion__item-number product-details-accordion__bulletpoint"]').text
    try:
        item['price'] = driver.find_element_by_xpath('//span[@class = "product-pricing__retail js-product-pricing__retail"]').text
    except:
        item['price'] = ''

    color_selector = driver.find_elements_by_xpath('//*[@id="color-attribute-selector"]/ul[@class = "buybox-dropdown__options js-basedropdown__options"]/li')
    colors = getAttribute(color_selector, 'data-img-title')

    for color, btn in zip(colors, color_selector):
        driver.find_element_by_xpath('//*[@id="product-color-select"]').click()
        btn.click()
        time.sleep(1)

        img_url = driver.find_element_by_xpath('//li[@class="ui-flexslider__item js-flexslider-item ui-flexslider-active-slide"]//img').get_attribute('src')
        item['img_name'] = saveImg(img_url, folder_name)

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

            series = pd.Series(item)
            df = df.append(series, ignore_index = True)

    return df
