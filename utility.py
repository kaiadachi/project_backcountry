def getAttribute(selenium_array, type):
    return [i.get_attribute(type) for i in selenium_array]

def getLastPage(driver):
    last_page = driver.find_elements_by_xpath('//li[@class = "page-link page-number"]/a')[-1].text

    return int(last_page)

def goNext(driver, init_url):
    driver.get('{0}?page={1}'.format(init_url, i+1))

    return driver
