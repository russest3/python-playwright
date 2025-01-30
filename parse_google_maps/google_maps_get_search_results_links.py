from playwright.sync_api import sync_playwright

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
    urls = page.evaluate("() => {" + script + "}")
    return urls or [url]
