from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipline():
    raw_path = "sales-data-pipline/data/daily_sales.csv"
    processed_path = "sales-data-pipline/data/processed/cleaned_sales.csv"

    df = extract_data(raw_path)
    df = transform_data(df)
    load_data(df, processed_path)

    print("Pipeline completed successfully!")
    if __name__ == "__main__":
        run_pipline()