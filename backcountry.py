# https://www.backcountry.com/
from settings import setConst

def setSelenium(target_url):
    # options = Options()
    # options.add_argument('--headless')
    # self.driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome()
    driver.get(target_url)

    return driver

if __name__ == '__main__':
    init = setConst()
    print(init['url'])
    #driver = setSelenium(init['url'])
