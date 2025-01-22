from parsel import Selector
from playwright.sync_api import sync_playwright, Page
import re

def parse_place(selector, page):
    _name = selector.css("h1.product-name ::text").get().strip()
    _price = selector.xpath("//div[@class='product-detail-content js-product-detail']/div[3]/div[@class='col-12']/div[@class='product-prices prices']/h3[@class='price back-to-product-anchor-js mb-0']/span[@class='default-price']/span[@class='sales']/span[@class='value']/text()").get()
    _price = re.sub("\n", "", _price)
    _price = re.sub(" ", "", _price)
    _image_link = 'screenshots/' + re.sub(" ", "-", _name) + '.png'
    btn = page.get_by_text('Product Details')
    btn.click()
    _details = selector.xpath("//*[@id='nav-details']/div[2]/p/text()").getall()
    _details = re.sub(r"\n", "", str(_details))
    _details = re.sub(r"• ", "", str(_details))
    _details = re.sub(r"\\n", "", str(_details))
    _details = re.sub(r" ", "", str(_details))
    result = {
        "name": _name,
        "price": _price,
        "Image Link": _image_link,
        "Details": str(_details)
    }
    page.screenshot(path=_image_link, full_page=True)
    print(result)
    return result
