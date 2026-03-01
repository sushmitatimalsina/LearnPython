def load_data(df, output_path):
    print("Loading data...")
    df.to_csv(output_path, index=False)