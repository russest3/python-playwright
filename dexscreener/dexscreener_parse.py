import dexscreener_get_search_results_links
import dexscreener_parse_single_place
from playwright.sync_api import sync_playwright
import json
from parsel import Selector
import ast
import create_csv_file
from playwright_stealth import stealth_sync
import proxyscrape

url = 'https://dexscreener.com/'

tokens_list = []

with sync_playwright() as p:
    # browser = p.chromium.launch(headless=False)
    # context = browser.new_context()
    # context.set_extra_http_headers({
    #     "Accept-Language": "en-US,en;q=0.5",
    #     })
    # page = context.new_page()
    # stealth_sync(page)
    # page.goto(url)
    # page.wait_for_load_state("networkidle")
    # page.wait_for_selector("//div[contains(@class, 'ds-table-data-cell')]")
    html = proxyscrape.get_page_contents(url)
    tokens_list.append(dexscreener_parse_single_place.parse_place(Selector(text=html)))

print(json.dumps(tokens_list, indent=2, ensure_ascii=False))

create_csv_file.dict_to_csv(tokens_list)

