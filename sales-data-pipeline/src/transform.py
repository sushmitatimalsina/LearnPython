import pandas as pd

def transform_data(df):
    print("Transforming data ......")
    df = df.dropna(subset=["amount"])
    df["amount"] = df["amount"].astype(float)
    df["tax"] = df["amount"]*0.13
    return df