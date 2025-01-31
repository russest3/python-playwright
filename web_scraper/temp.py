import pandas as pd
import re
import csv
import ast

results = "{{'name': 'Blackbird Ordinary', 'category': 'Bar', 'address': '729 SW 1st Ave, Miami, FL 33130', 'website': '', 'phone': '(305) 671-3307', 'review_count': '2,458 reviews', 'stars': '4.2', '5_stars': '451', '4_stars': '543', '3_stars': '227', '2_stars': '83', '1_stars': '154'}} {{'name': 'Lola bar', 'category': 'Bar', 'address': '401 Biscayne Blvd S118, Miami, FL 33132', 'website': '', 'phone': '', 'review_count': '2,534 reviews', 'stars': '4.9', '5_stars': '415', '4_stars': '27', '3_stars': '15', '2_stars': '11', '1_stars': '66'}}"
            #   {{'name': 'Gramps', 'category': 'Bar', 'address': '176 NW 24th St, Miami, FL 33127', 'website': 'Website: gramps.cfd', 'phone': '(855) 732-8992', 'review_count': '2,047 reviews', 'stars': '4.5', '5_stars': '396', '4_stars': '422', '3_stars': '131', '2_stars': '31', '1_stars': '67'}} {{'name': 'Rosa Sky', 'category': 'Restaurant', 'address': '115 SW 8th St 22nd Floor, Miami, FL 33130', 'website': 'Website: rosaskyrooftop.com', 'phone': '(786) 628-1515', 'review_count': '4,040 reviews', 'stars': '4.7', '5_stars': '554', '4_stars': '194', '3_stars': '75', '2_stars': '48', '1_stars': '169'}} {{'name': 'Tipsy Flamingo Cocktail Bar', 'category': 'Cocktail bar', 'address': '40 NE 1st Ave #101, Miami, FL 33132', 'website': 'Website: tipsyflamingomiami.com', 'phone': '(305) 646-9967', 'review_count': '314 reviews', 'stars': '4.5', '5_stars': '255', '4_stars': '22', '3_stars': '7', '2_stars': '11', '1_stars': '19'}} {{'name': 'MO Bar & Lounge', 'category': 'Bar', 'address': '500 Brickell Key Dr, Miami, FL 33131', 'website': 'Website: mandarinoriental.com', 'phone': '(305) 913-8358', 'review_count': '447 reviews', 'stars': '4.6', '5_stars': '339', '4_stars': '79', '3_stars': '13', '2_stars': '4', '1_stars': '12']


results = re.sub("{{", "{", results)
results = re.sub("}}", "}, ", results)

my_dict = ast.literal_eval(results)

print(my_dict)

# header = ["name", "category", "address", "website", "phone", "review_count", "stars", "5_stars", "4_stars", "3_stars", "2_stars", "1_stars"]
# with open('test.csv', 'w') as file:
#     writer = csv.DictWriter(file, fieldnames=header)
#     writer.writeheader()
#     writer.writerows(results)


# results = re.sub("{{", "", results)
# results = re.sub("}}", "", results)
# # results = list(results)
# print(results)

# df = pd.DataFrame(results)
# df.to_csv("temp.csv")

# print(results)

