import parse_single_agent
import user_agents
from playwright.sync_api import sync_playwright, Page
from parsel import Selector
import create_csv_file
import sys
# from twocaptcha import TwoCaptcha
import time

# Pass in api key from command line:  python3 parse.py '${api_key}'
# if len(sys.argv) > 1:
#     api_key = sys.argv[1]

base_url = "https://www.zillow.com/professionals/real-estate-agent-reviews"
# Must be in this format
location_to_search = '/erie-pa'
url = base_url + location_to_search

list_of_agents = []

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

var results = waitCss("a.StyledCard-c11n-8-101-3__sc-1w6p0lv-0", n=10, require=false);
return Array.from(results).map((el) => el.getAttribute("href"))
"""

script2 = """
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

var results = waitCss("a.StyledCard-c11n-8-107-0__sc-1w6p0lv-0", n=10, require=false);
return Array.from(results).map((el) => el.getAttribute("href"))
"""

# First parse the page for links to each agency name
with sync_playwright() as p:
    agency_name_urls = []
    browser = p.chromium.launch(headless=False)
    browser.new_context(user_agent=user_agents.getRandomUserAgent())
    # solver = TwoCaptcha(api_key)
    page = browser.new_page()
    page.goto(url)

# Captcha #
    # Wait for potential CAPTCHA to appear
    while page.locator('text=Click & Hold').is_visible():
        time.sleep(5)  # Pause script execution for manual CAPTCHA solving
# Captcha #


    urls = page.evaluate("() => {" + script + "}")
    for url in urls:
        agency_name_urls.append('https://zillow.com' + url)

print(agency_name_urls)

# Then parse the page for each agent link
with sync_playwright() as p:
    agents_urls = []
    agents_urls_list = []
    for url in agency_name_urls:
        browser = p.chromium.launch(headless=False)
        browser.new_context(user_agent=user_agents.getRandomUserAgent())
        page = browser.new_page()
        page.goto(url)


# Captcha #
    # Wait for potential CAPTCHA to appear
    while page.locator('text=Click & Hold').is_visible():
        time.sleep(5)  # Pause script execution for manual CAPTCHA solving
# Captcha #


        # Check for the CAPTCHA presence
        # if page.locator('text=Press & Hold').is_visible():
        #     print("CAPTCHA detected. Solving...")
            
            # Find the CAPTCHA button
            # captcha_button = page.get_by_text('Press & Hold', exact=True)
            # box = captcha_button.bounding_box()
            
            # Simulate the "click and hold" interaction
            # if box:
              # # Calculate the center of the button
              # start_x = box['x'] + box['width'] / 2
              # start_y = box['y'] + box['height'] / 2

              # Move the mouse gradually to the center of the button
              # steps = 50
              # current_x, current_y = start_x - 20, start_y - 20  # Start from a point slightly outside the button
              # for i in range(steps):
              #     next_x = current_x + (start_x - current_x) / (steps - i)
              #     next_y = current_y + (start_y - current_y) / (steps - i)
              #     page.mouse.move(next_x, next_y, steps=1)
              #     time.sleep(0.02)  # Small delay to simulate human-like movement
              #     current_x, current_y = next_x, next_y

              # Click and hold the button
            #   page.mouse.down()
            #   time.sleep(10)  # Hold for the required time
            #   page.mouse.up()
            #   print("CAPTCHA cleared.")
            # else:
            #   print("Could not locate CAPTCHA button.")

        agents_urls.append(page.evaluate("() => {" + script2 + "}"))
        for url in agents_urls:
            agents_urls_list.append('https://zillow.com' + str(url))

print(agents_urls_list)

# agents_urls_list = ['https://zillow.com/profile/erik1155']

# Then parse the agents page
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=True)
#     browser.new_context(user_agent=user_agents.getRandomUserAgent())
#     page = browser.new_page    

#     for url in agents_urls_list:
#         page.goto(url)
#         if page.get_by_text('Press & Hold', exact=True).is_visible():
#             btn = page.get_by_text('Press & Hold', exact=True)
#             btn.click( delay=30000)
#         list_of_agents.append(parse_single_agent.parse_agent(Selector(text=page.content())))

# create_csv_file.list_to_csv(list_of_agents)