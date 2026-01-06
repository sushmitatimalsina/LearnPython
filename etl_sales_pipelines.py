import pandas as pd

def extract_data():
    df = pd.read_csv('raw_sales_data.csv')
    return df

def transform_data(df):
    df.dropna(inplace=True)
    df['total_price'] = df['quantity']*df['unit_price']
    return df

def load_data(df):
    df.to_csv("cleaned_sales_data.csv", index=False)
    
