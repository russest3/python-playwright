from playwright.sync_api import sync_playwright
from playwright.sync_api import Mouse
from playwright.sync_api import Keyboard
from playwright.sync_api import Page
from time import sleep

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

var results = waitCss("div.CpccDe a.hfpxzc, div.Nv2PK a.hfpxzc, div.tH5CWc a.hfpxzc, div.THOPZb a.hfpxzc", n=10, require=false);
return Array.from(results).map((el) => el.getAttribute("href"))
"""

def search(query, page):
    url = f"https://www.google.com/maps/search/{query.replace(' ', '+')}/?hl=en"
    page.goto(url)    
    page.mouse.click(375, 78)
    page.keyboard.press('PageDown')
    sleep(2)
    page.keyboard.press('PageDown')
    sleep(2)
    page.keyboard.press('PageDown')
    sleep(2)
    page.keyboard.press('PageDown')
    sleep(5)
    urls = page.evaluate("() => {" + script + "}")
    return urls or [url]
