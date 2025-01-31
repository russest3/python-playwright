import google_maps_get_search_results_links as gsrl
import google_maps_parse_single_place as gmpsp
from parsel import Selector
from playwright.sync_api import sync_playwright, Playwright

places = []

def get_search_results_links(search_term):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # NEED TO SCROLL DOWN HERE TO GET MORE RESULTS FIRST!!!!
        search_results_links = gsrl.search(search_term, page=page)
        return search_results_links

def get_search_results(search_results_links):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        context.set_extra_http_headers({
            "Accept-Language": "en-US,en;q=0.5",
            })
        page = context.new_page()
        for url in search_results_links:
            page.goto(url)
            clip = {"x": 503, "y": 66, "width": 400, "height": 840}
            page.screenshot(clip=clip)
            places.append(gmpsp.parse_place(Selector(text=page.content())))
        return places

###### For Testing ###################33
# results = get_search_results_links('Bars in Miami')
# print(results)
# final_results = get_search_results(results)
# print(final_results)