from playwright.sync_api import sync_playwright
import time
import csv

def scrape_zillow_agents_with_captcha_handling(url, output_csv='zillow_agents.csv'):
    """
    Scrape Zillow for agent data, including handling "Click & Hold" CAPTCHA.
    
    Parameters:
        url (str): The Zillow URL to scrape from (ensure it's agent-specific).
        output_csv (str): The name of the CSV file to save data.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to False to observe CAPTCHA solving
        context = browser.new_context()
        page = context.new_page()
        
        print(f"Navigating to {url}...")
        page.goto(url)

        # Wait for potential CAPTCHA to appear
        while page.locator('text=Click & Hold').is_visible():
            input()  # Pause script execution for manual CAPTCHA solving

        # Wait for the agent cards to load
        page.wait_for_selector('div[class*="agent-card"]')

        # List to store agent data
        agents_data = []

        # Scrape agent details
        agents = page.query_selector_all('div[class*="agent-card"]')
        for agent in agents:
            try:
                name = agent.query_selector('h3[class*="agent-name"]').inner_text()
                business_phone = agent.query_selector('div[class*="business-phone"]').inner_text() if agent.query_selector('div[class*="business-phone"]') else None
                cell_phone = agent.query_selector('div[class*="cell-phone"]').inner_text() if agent.query_selector('div[class*="cell-phone"]') else None
                email = agent.query_selector('a[href^="mailto:"]').get_attribute('href').replace('mailto:', '') if agent.query_selector('a[href^="mailto:"]') else None
                address = agent.query_selector('div[class*="agent-address"]').inner_text() if agent.query_selector('div[class*="agent-address"]') else None
                realtor_name = agent.query_selector('div[class*="agency-name"]').inner_text() if agent.query_selector('div[class*="agency-name"]') else None

                agents_data.append({
                    'Name': name,
                    'Business Phone': business_phone,
                    'Cell Phone': cell_phone,
                    'Email': email,
                    'Address': address,
                    'Realtor Name': realtor_name
                })
            except Exception as e:
                print(f"Error scraping agent data: {e}")

        # Save data to CSV
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'Business Phone', 'Cell Phone', 'Email', 'Address', 'Realtor Name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(agents_data)

        print(f"Scraped data saved to {output_csv}")
        browser.close()

# Example usage:
zillow_url = 'https://www.zillow.com/professionals/real-estate-agent-reviews/erie-pa/'  # Ensure the URL is specific to agents
scrape_zillow_agents_with_captcha_handling(zillow_url)
