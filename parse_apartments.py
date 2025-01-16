from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

class apartment:
    def __init__(self, name, address, link, price, beds, amenities):
        self.name = name
        self.address = address
        self.link = link
        self.price = price
        self.beds = beds
        self.amenities = amenities
        with open('parsed_item_list.csv', 'w') as file:
            file.write("name, address, link, price, beds, amenities\n")

    def display(self):
        print(f"Name: {self.name}, Address: {self.address}, Link: {self.link}, Price: {self.price}, Beds: {self.beds}, Amenities: {self.amenities}")
    
    def create_csv_file(self, str):
        with open('parsed_item_list.csv', 'a') as file:
            file.write(str)
    
    def convert_csv_to_html(self, str):
        df = pd.read_csv("parsed_item_list.csv")
        html_table = df.to_html(index=False)
        with open('parsed_item_list.html', 'w') as file:
            file.write(html_table)

def test_get_apartments():
    all_listings_csv = ""
    all_listing_list = []
    # response = requests.get('https://www.apartments.com/new-york-ny/')

    # with open('downloaded.html', 'w') as file:
    #     file.write(str(response.text))

    with open('downloaded.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')    
    items = soup.find_all('article')

    for i in items:
        name = i.find('span', class_='js-placardTitle title').get_text()
        address = i.find('div', class_='property-address js-url').get_text()
        address = re.sub(",", "", str(address))
        link = i.find('a', class_='property-link')["href"]
        price = i.find('p', class_='property-pricing').get_text()
        price = re.sub(",", "", str(price))
        beds = i.find('p', class_='property-beds').get_text().strip('\n')
        amenities = i.find(attrs={"class": "property-amenities"})
        amenities = re.sub(r"^None$", "", str(amenities))
        amenities = re.sub(r"<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>", "", amenities)
        amenities = re.sub(r"\n", " ", amenities)
        # print(amenities)
        listing = apartment(name=name, address=address, link=link, price=price, beds=beds, amenities=amenities)
        all_listing_list.append(listing)
        all_listings_csv = all_listings_csv + (str(name) + ', ' + str(address) + ', ' + str(link) + ', ' + str(price) + ', ' + str(beds) + ', ' + str(amenities) + '\n')
    
    listing.create_csv_file(all_listings_csv)

    listing.convert_csv_to_html(all_listings_csv)
    