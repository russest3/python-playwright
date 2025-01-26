from parsel import Selector
from playwright.sync_api import sync_playwright, Page
import re

def parse_place(selector, page):
    _name = selector.css("h1.sc-24b68d11-7 ::text").get().strip()
    _stand_location = selector.css("span.sc-c3d23e77-0 ::text").get().strip()
    print(_stand_location)
    _description = selector.css("div.sc-24b68d11-14 ::text").getall()
    print(_description)
