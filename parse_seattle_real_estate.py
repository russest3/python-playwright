from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

class real_estate:
    def __init__(self, broker_name, email, phone):
        self.broker_name = broker_name
        self.email = email
        self.phone = phone
        with open('parsed_item_list.csv', 'w') as file:
            file.write("broker_name, email, phone\n")

    def display(self):
        print(f"broker_name: {self.broker_name}, email: {self.email}, phone: {self.phone}")
    
    def create_csv_file(self, str):
        with open('parsed_item_list.csv', 'a') as file:
            file.write(str)
    
    def convert_csv_to_html(self, str):
        df = pd.read_csv("parsed_item_list.csv")
        html_table = df.to_html(index=False)
        with open('parsed_item_list.html', 'w') as file:
            file.write(html_table)

def test_get_real_estates():
    all_listings_csv = ""
    all_listing_list = []
    html_content = requests.get('https://www.google.com/maps/search/brokerage+firms/@47.6196875,-122.671461,10z/data=!3m1!4b1?entry=ttu&g_ep=EgoyMDI1MDExMC4wIKXMDSoASAFQAw%3D%3D')

    # with open('downloaded.html', 'w') as file:
    #     file.write(str(html_content.text))

    with open('downloaded.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    #QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd.QjC7t    
    soup = BeautifulSoup(html_content, 'html.parser')    
    broker_names = soup.find('a').get_text()
    print(broker_names)


    # link = i.find('a', class_='hfpxzc')["href"]
    # print(link).get_text()

        # email = i.find('div', class_='property-email js-url').get_text()
        # email = re.sub(",", "", str(email))
        # phone = i.find('a', class_='property-phone')["href"]
        # price = i.find('p', class_='property-pricing').get_text()
        # price = re.sub(",", "", str(price))
        # beds = i.find('p', class_='property-beds').get_text().strip('\n')
        # amenities = i.find(attrs={"class": "property-amenities"})
        # amenities = re.sub(r"^None$", "", str(amenities))
        # amenities = re.sub(r"<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>", "", amenities)
        # amenities = re.sub(r"\n", " ", amenities)
        # print(amenities)
    #     listing = real_estate(broker_name=broker_name, email=email, phone=phone, price=price, beds=beds, amenities=amenities)
    #     all_listing_list.append(listing)
    #     all_listings_csv = all_listings_csv + (str(broker_name) + ', ' + str(email) + ', ' + str(phone) + ', ' + str(price) + ', ' + str(beds) + ', ' + str(amenities) + '\n')
    
    # listing.create_csv_file(all_listings_csv)

    # listing.convert_csv_to_html(all_listings_csv)
    