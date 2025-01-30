from parsel import Selector
from playwright.sync_api import sync_playwright
import re

def parse_place(selector):
    """parse Google Maps place"""
    
    def aria_with_label(label):
        """gets aria element as is"""
        return selector.css(f"*[aria-label*='{label}']::attr(aria-label)")

    def aria_no_label(label):
        """gets aria element as text with label stripped off"""
        if aria_with_label(label).get("") != "None":
            text = aria_with_label(label).get("")
            text = re.sub("Address: ", "", str(text)).strip()
            text = re.sub("Phone: ", "", str(text)).strip()
            text = re.sub("Website: ", "", str(text)).strip()
            return text

    result = {
        "name": selector.css("h1 ::text").get(),
        "category": selector.xpath(
            "//button[contains(@jsaction, 'category')]/text()"
        ).get(),
        # most of the data can be extracted through accessibility labels:
        "address": aria_no_label("Address: "),
        "website": aria_no_label("Website: "),
        "phone": aria_no_label("Phone: "),
        "review_count": aria_with_label(" reviews").get(),
        # to extract star numbers from text we can use regex pattern for numbers: "\d+"
        "stars": aria_with_label(" stars").re("\d+.*\d+")[0],
        "5_stars": aria_with_label("5 stars").re(r"(\d+) review")[0],
        "4_stars": aria_with_label("4 stars").re(r"(\d+) review")[0],
        "3_stars": aria_with_label("3 stars").re(r"(\d+) review")[0],
        "2_stars": aria_with_label("2 stars").re(r"(\d+) review")[0],
        "1_stars": aria_with_label("1 stars").re(r"(\d+) review")[0],
    }
    return result


########## For Testing ##################################3
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     context.set_extra_http_headers({
#         "Accept-Language": "en-US,en;q=0.5",
#         })
#     page = context.new_page()
#     page.goto("https://www.google.com/maps/place/Blackbird+Ordinary/data=!4m7!3m6!1s0x88d9b684efe016b1:0xe976c9967fe1438b!8m2!3d25.7667169!4d-80.1951854!16s%2Fg%2F1tfv5y6z!19sChIJsRbg74S22YgRi0Phf5bJduk?authuser=0&hl=en&rclk=1")
#     page.wait_for_selector("#QA0Szd, div, div, div.w6VYqd, div:nth-child(1), ul, li:nth-child(9), button, div.NP7r5c, div.xSVTVc, div.wiquBf")

#     print(parse_place(Selector(text=page.content())))