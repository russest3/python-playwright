import google_maps_get_search_results_links
import google_maps_parse_single_place
from playwright.sync_api import sync_playwright
import json
from parsel import Selector
import ast
import create_csv_file

search_term = "Roofers in Lincoln Nebraska"
# div_identifier must be looked up from a manual search 
div_identifier = 'div.Nv2PK a.hfpxzc, div.tH5CWc a.hfpxzc, div.THOPZb a.hfpxzc' # "Roofers in Lincoln Nebraska"

places = []

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()    
    search_results = f'{google_maps_get_search_results_links.search(search_term, page=page)}'
    search_results = ast.literal_eval(search_results)
    # print(search_results)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    context.set_extra_http_headers({
        "Accept-Language": "en-US,en;q=0.5",
        })
    page = context.new_page()
    for url in search_results:
        page.goto(url)
        page.wait_for_selector("//button[contains(@jsaction, 'reviewlegaldisclosure')]")
        places.append(google_maps_parse_single_place.parse_place(Selector(text=page.content())))

print(json.dumps(places, indent=2, ensure_ascii=False))

create_csv_file.dict_to_csv(places, search_term)