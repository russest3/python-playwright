import google_maps_get_search_results_links
import google_maps_parse_single_place
from playwright.sync_api import sync_playwright
from parsel import Selector
import ast

places = []

class parse_google_maps:
    def __init__(self, search_term):
        self.search_term = search_term

    def get_search_results_links(self, search_term):
        with sync_playwright() as p:
            browser = self.p.chromium.launch()
            page = browser.new_page()    
            search_results_links = f'{google_maps_get_search_results_links.search(search_term, page=page)}'
            search_results_links = ast.literal_eval(search_results_links)
            return search_results_links
    
    def get_search_results(self, search_results_links):
        with sync_playwright() as p:
            browser = self.p.chromium.launch(headless=True)
            context = browser.new_context()
            context.set_extra_http_headers({
                "Accept-Language": "en-US,en;q=0.5",
                })
            page = context.new_page()
            for url in search_results_links:
                page.goto(url)
                page.wait_for_selector("//button[contains(@jsaction, 'reviewlegaldisclosure')]")
                places.append(google_maps_parse_single_place.parse_place(Selector(text=page.content())))
        return places

if __name__ == "__main__":
    results = parse_google_maps()
