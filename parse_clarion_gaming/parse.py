import parse_single_place
from playwright.sync_api import sync_playwright, Page
from parsel import Selector
# import ast
# import create_csv_file
import re

url = "https://event.clariongaming.com/event/ice-2025/exhibitors/RXZlbnRWaWV3XzkxOTQ5OQ=="
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

var results = waitCss("div.sc-4f9e9086-0 iXvNRj, a", n=10, require=false);
return Array.from(results).map((el) => el.getAttribute("href"))
"""

new_urls = ['https://event.clariongaming.com/event/ice-2025/exhibitor/RXhoaWJpdG9yXzIxMzE5MDU=']

# with sync_playwright() as p:
    # browser = p.chromium.launch(headless=False)
    # page = browser.new_page()
    # page.goto(url)
    # urls = page.evaluate("() => {" + script + "}")
    # for url in urls:
    #     if re.match("^/event/ice-2025/exhibitor.*$", url):
    #         new_urls.append('https://event.clariongaming.com' + url)
    # print(new_urls)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    context.set_extra_http_headers({
        "Accept-Language": "en-US,en;q=0.5",
        })
    page = context.new_page()

    for url in new_urls:
        
        page.goto(url)
        page.query_selector("button[data-hook='cookie-banner-accept-all-button']").click()
        places.append(parse_single_place.parse_place(Selector(text=page.content()), page=page))

# print(json.dumps(places, indent=2, ensure_ascii=False))

# create_csv_file.dict_to_csv(places)