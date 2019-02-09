import pandas as pd
import time
from src.utility import *
from src.upc import *
from src.settings import *
import traceback


def parse(driver, item, df, folder_img):
    # parent
    item['url'] = driver.current_url

    try:
        item['product'] = driver.find_element_by_xpath('//li[@class="product-details-accordion__item-number product-details-accordion__bulletpoint"]').text.replace("Item #", "")
        item['name'] = driver.find_element_by_xpath('//h1[@class="product-name qa-product-title"]').text
        item['brand'] = driver.find_element_by_xpath('//span[@class = "qa-brand-name"]').text
    except Exception as e:
        print(traceback.format_exc())

    item['parent_child'] = 'parent'

    series = pd.Series(item)
    df = df.append(series, ignore_index = True)

    # child
    try:
        item['price'] = driver.find_element_by_xpath('//span[@class = "product-pricing__retail js-product-pricing__retail"]').text
    except:
        try:
            item['price'] = driver.find_element_by_xpath('//span[@class = "product-pricing__sale js-product-pricing__sale"]').text
        except:
            try:
                item['price'] = driver.find_element_by_xpath('//span[@class = "product-pricing__sale"]').text
            except Exception as e:
                print(traceback.format_exc())

    item['price'] = item['price'].replace('$', '')
    item['price'] = float(item['price']) * setConst()['weight']

    description = driver.find_element_by_xpath('//div[@class = "ui-product-details__description"]').text
    for i in driver.find_elements_by_xpath('//li[@class = "product-details-accordion__bulletpoint"]'):
        description = description + '\n - ' + i.text
    item['description'] = description

    # driver.find_element_by_xpath('//span[@class = "ui-accordion-header-icon ui-icon product-details-accordion__header--inactive"]').click()
    name_selector = driver.find_elements_by_xpath('//div[@class = "td ui-product-details__techspec-name"]')
    value_selector = driver.find_elements_by_xpath('//div[@class = "td ui-product-details__techspec-value"]')
    for name, value in zip(name_selector,value_selector):
        #print("%s:%s" %(name.text, value.text))
        item[name.text] = value.text

    color_selector = driver.find_elements_by_xpath('//*[@id="color-attribute-selector"]/ul[@class = "buybox-dropdown__options js-basedropdown__options"]/li')
    colors = getAttribute(color_selector, 'data-img-title')

    item['parent_sku'] = item['product']
    item['parent_child'] = 'child'

    # upc
    browser = webdriver.Chrome()
    for color, color_btn in zip(colors, color_selector):
        color_selectbox = driver.find_element_by_xpath('//*[@id="product-color-select"]')
        color_selectbox.click()
        color_btn.click()

        # img_url = driver.find_element_by_xpath('//li[@class="ui-flexslider__item js-flexslider-item ui-flexslider-active-slide"]//img').get_attribute('src')
        # item['img_name'] = saveImg(img_url, folder_img)

        size_selector = driver.find_elements_by_xpath('//*[@id="size-attribute-selector"]/ul[@class = "buybox-dropdown__options js-basedropdown__options"]/li')
        isinActives = getAttribute(size_selector, 'class')
        sizes = getAttribute(size_selector, 'data-attribute-selector-key')

        item['color'] = color

        for size, isinActive, size_btn in zip(sizes, isinActives, size_selector):
            if 'is-inactive' not in isinActive:
                size_selectbox = driver.find_element_by_xpath('//*[@id="product-size-select"]')
                size_selectbox.click()
                size_btn.click()

                item['stock'] = 1
                item['size'] = size

                item['product'] = driver.find_element_by_xpath('//input[@class = "js-selected-product-variant"]').get_attribute('value')
                print(item['product'])
                item['upc'] = searchUpc(item['product'], browser)

                series = pd.Series(item)
                df = df.append(series, ignore_index = True)

    browser.close()
    return df
