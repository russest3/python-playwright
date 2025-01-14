import re
from playwright.sync_api import expect, Page
from pprint import pprint

def test_get_apartments(page: Page):
    page.goto('https://www.apartments.com/new-york-ny/')
    results = page.locator('//*[@id="placardContainer"]/ul')
    parsed = []
    combined_text = ""

    for line in results.element_handles():
        spans = line.query_selector_all("li section div[class='property-info'] div[class='content-wrapper'] a[class='property-link'] p[class='property-amenities'] span")
        for span in spans:
            combined_text = span.inner_text() + ", "
        parsed.append({
            "Name": line.query_selector('li header div a div span').inner_text(),
            "Address": line.query_selector("li header div a div[class='property-address js-url']").text_content(),
            "Price": line.query_selector("li section div[class='property-info'] div div a p").text_content(),
            "Bedrooms": line.query_selector("li section div[class='property-info'] div div a p[class='property-beds']").text_content(),
            "Amenities": combined_text
            
            # "username": box.query_selector(".tw-link").inner_text(),
            # "viewers": box.query_selector(".tw-media-card-stat").inner_text(),
            # # tags are not always present:
            # "tags": box.query_selector(".tw-tag").inner_text() if box.query_selector(".tw-tag") else None,
        })
    
    print(parsed)

