import pandas as pd

def dict_to_csv(mydict):
    pd.DataFrame(mydict).to_csv('places.csv', index=False)
