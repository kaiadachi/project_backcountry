import sys
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def doTrans(sentence, browser):
    browser.get('https://translate.google.co.jp/')

    input = browser.find_element_by_xpath('//*[@id="source"]')
    input.send_keys(sentence)

    transList = browser.find_elements_by_xpath('//span[@class="tlid-translation translation"]')

    trans = ''
    for i in transList:
        trans = trans + i.text
    time.sleep(3)

    return trans

if __name__ == '__main__':
    result = doTrans("Patagonia is one of the most popular brands around today for a reasonthey make good stuff. And the Patagonia Women's Organic Cotton Quilt Snap-T Pullover Sweatshirt is one of the best things they make. There's a reason its light-wearing comfort and easy warmth stick around season after season. Made from a soft organic cotton blend, this pullover sports a classic diamond quilted pattern that also works as an effective heat-trapping system, letting you wear it alone to keep cozy on the couch or throw it on as a layer for your next winter adventure. Keep the cold out on fall hikes or summer nights around the campfire with a buttoned stand up collar and cuffs at the hip and sleeves. A buttoned chest pocket adds detailing and convenient storage for smaller items.")
    print(result)
