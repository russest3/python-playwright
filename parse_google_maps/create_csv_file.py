import pandas as pd
import re

def dict_to_csv(mydict, search_term):
    search_term = re.sub(" ", "-", search_term)
    pd.DataFrame(mydict).to_csv(search_term + '.csv', index=False)
