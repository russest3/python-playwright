# import parse_amazonuk_category_fees
import parse_single_place
from playwright.sync_api import sync_playwright
from parsel import Selector
import create_csv_file

url = 'https://sell.amazon.co.uk/pricing'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    context.set_extra_http_headers({
        "Accept-Language": "en-US,en;q=0.5",
        })
    page = context.new_page()
    page.goto(url)

    # with open('downloaded.html', 'w') as file:
    #     file.write(str(page.content()))

    with open('downloaded.html', 'r') as file:
        results = file.read()

    results = parse_single_place.parse_category(Selector(text=page.content()))  

create_csv_file.create(results)