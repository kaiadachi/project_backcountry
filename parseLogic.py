def parse(driver, item):
    item['name'] = driver.find_element_by_xpath('//span[@class = "qa-brand-name"]').text
    
