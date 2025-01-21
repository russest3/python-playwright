from parsel import Selector
from playwright.sync_api import sync_playwright, Page
import re

def parse_place(selector, page):
    _name = selector.css("h1.product-name ::text").get().strip()
    _price = selector.xpath("//div[@class='product-detail-content js-product-detail']/div[3]/div[@class='col-12']/div[@class='product-prices prices']/h3[@class='price back-to-product-anchor-js mb-0']/span[@class='default-price']/span[@class='sales']/span[@class='value']/text()").get().strip()
    _image_link = 'screenshots/' + re.sub(" ", "-", _name) + '.png'
    # btn = selector.xpath("//*[@id='pdp-default']/div[1]/div/div[2]/div[2]/div[2]/div/div[4]/ul/li[2]/button")
    btn_value = "\n            \n                Product Details &amp; Shipping\n            \n        \n"
    btn = selector.xpath('//button[@value="\n            \n                Product Details &amp; Shipping\n            \n        \n"]').get()

    btn.click()
    _details = selector.xpath("//*[@id='nav-details']/div[2]/p/text()").get().strip()
    result = {
        "name": _name,
        "price": _price,
        "Image Link": _image_link,
        "Details": _details
    }
    page.screenshot(path=_image_link, full_page=True)
    print(result)
    return result
