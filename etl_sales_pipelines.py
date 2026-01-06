import pandas as pd

def extract_data():
    df = pd.read_csv('raw_sales_data.csv')
    return df

def transform_data(df):
    df['quantity'] = df['quantity'].fillna("Not Available")
    
    df.dropna(inplace=True)
    df['total_price'] = df['quantity']*df['price']
    return df

def load_data(df):
    df.to_csv("cleaned_sales_data.csv", index=False)


def main():
    raw_data = extract_data()
    clean_data = transform_data(raw_data)
    load_data(clean_data)



if __name__ == "__main__":
    main()

