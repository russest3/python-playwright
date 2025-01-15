from bs4 import BeautifulSoup
import requests

class apartment:
    def __init__(self, name, address, link, price, beds, amenities):
        self.name = name
        self.address = address
        self.link = link
        self.price = price
        self.beds = beds
        self.amenities = amenities
        with open('parsed_items.csv', 'w') as file:
            file.write("name, address, link, price, beds, amenities\n")
        

    def display(self):
        print(f"Name: {self.name}, Address: {self.address}, Link: {self.link}, Price: {self.price}, Beds: {self.beds}, Amenities: {self.amenities}")
    
    def write_all_to_file(self, list):
        with open('parsed_item_list.txt', 'a') as file:
            file.write(list)

def test_get_apartments():
    all_listings = list()
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
        link = i.find('a', class_='property-link')["href"]
        price = i.find('p', class_='property-pricing').get_text()
        beds = i.find('p', class_='property-beds').get_text().strip('\n')
        amenities = i.find(attrs={"class": "property-amenities"})        
        listing = apartment(name=name, address=address, link=link, price=price, beds=beds, amenities=amenities)
        # all_listings.append(name, address, link, price, beds, amenities)
        all_listings.append(str(name) + ', ' + address + ', ' + link + ', ' + price + ', ' + beds + ', ' + amenities + '\n')
    
    with open('parsed_item_list.csv', 'a') as file:            
        file.write(all_listings)
    