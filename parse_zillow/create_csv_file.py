# import csv
# import re
import pandas as pd

def list_to_csv(mylist):
    pd.DataFrame(mylist).to_csv('zillow_agents_list.csv', index=False)
    # with open('zillow_agents_list.csv', 'w', newline='') as myfile:
    #     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #     wr.writerow([{mylist}])

    # with open('zillow_agents_list.csv', 'a', newline='') as myfile:
    #     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #     wr.writerow(mylist)

