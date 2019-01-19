def parse(driver, item):
    item['name'] = driver.find_element_by_xpath('//span[@class = "qa-brand-name"]').text
    item['product_number'] = driver.find_element_by_xpath('//li[@class = "product-details-accordion__item-number product-details-accordion__bulletpoint"]').text
    item['price'] = driver.find_element_by_xpath('//span[@class = "product-pricing__retail"]').text
