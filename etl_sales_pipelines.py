import pandas as pd

def extract_data():
    df = pd.read_csv('raw_sales_data.csv')
    return df


