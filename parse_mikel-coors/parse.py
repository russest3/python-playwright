import parse_single_place
from playwright.sync_api import sync_playwright
from parsel import Selector
# import ast
# import create_csv_file
import re

url = "https://www.michaelkors.com/outlet/view-all/"
places = []

script = """
function waitCss(selector, n=1, require=false, timeout=5000) {
  console.log(selector, n, require, timeout);
  var start = Date.now();
  while (Date.now() - start < timeout){
  	if (document.querySelectorAll(selector).length >= n){
      return document.querySelectorAll(selector);
    }
  }
  if (require){
      throw new Error(`selector "${selector}" timed out in ${Date.now() - start} ms`);
  } else {
      return document.querySelectorAll(selector);
  }
}

var results = waitCss("div.image-container, a.product-tile-image-link", n=10, require=false);
return Array.from(results).map((el) => el.getAttribute("href"))
"""

with sync_playwright() as p:
    # browser = p.chromium.launch(headless=False)
    # page = browser.new_page()
    # page.goto(url)
    # urls = page.evaluate("() => {" + script + "}")

    urls = [None, '/pratt-medium-shoulder-bag/35S4S3FS2I.html?astc=true', None, '/pratt-small-signature-logo-convertible-shoulder-bag/35S4S3FM5V.html?astc=true']
    new_urls = [x for x in urls if x != None]
    new_urls = ["https://www.michaelkors.com" + item for item in new_urls]
    # print(new_urls)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    context.set_extra_http_headers({
        "Accept-Language": "en-US,en;q=0.5",
        })
    page = context.new_page()
    url = 'https://www.michaelkors.com/pratt-small-signature-logo-shoulder-bag/35S4G3FM5B.html?astc=true&dwvar_35S4G3FM5B_color=2605'
    for url in new_urls:
        page.goto(url)
        # page.wait_for_selector("#pdp-default > div.container > div > div.product-detail.product-wrapper.position-relative > div.image-detail-container.row > div.product-detail-container.col-xs-12.col-lg-6 > div > div.attributes > div.prices-add-to-cart-actions > div.d-flex.quantity-addtocart-grid-pdp.add-to-cart-grid--js > div.cart-and-ipay > div > button", timeout=60000)    
        places.append(parse_single_place.parse_place(Selector(text=page.content()), page=page))

# print(json.dumps(places, indent=2, ensure_ascii=False))

# create_csv_file.dict_to_csv(places)