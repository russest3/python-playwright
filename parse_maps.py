from playwright.sync_api import Page, expect, Response

def test_parse_map(page: Page):
    response: Response = page.goto(f"https://www.google.com/maps/search/Chinese+Restaurants/@35.5819249,-78.8496384,15z?entry=ttu&g_ep=EgoyMDI1MDEwOC4wIKXMDSoASAFQAw%3D%3D")
    results = page.locator('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]')
    print(results.all_inner_texts())
    




