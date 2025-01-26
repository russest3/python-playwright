from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a python developer interested in html web scraping projects."},
        {
            "role": "user",
            "content": "Write Python code that will scrape zillow.com for real estate agents in Erie PA, include their name, phone, email address, physical address, and realtor company.  Then construct a CSV file from this data."
        }
    ]
)

print(completion.choices[0].message)