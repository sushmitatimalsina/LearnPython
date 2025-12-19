import pandas as pd
import requests

class ETLPipeline:
    def __init__(self, api_url):
        self.api_url = api_url
        self.df = None

    def extract(self):
        response = requests.get(self.api_url)
        data = response.json()
        self.df = pd.DataFrame(data)
        print("Data extracted")
        return self.df

    def transform(self):
        # Example transformation: keep only selected columns
        self.df = self.df[['id', 'name', 'email']]
        print("Data transformed")
        return self.df

    def load(self, file_name):
        self.df.to_csv(file_name, index=False)
        print(f"Data loaded into {file_name}")

# Usage
pipeline = ETLPipeline("https://jsonplaceholder.typicode.com/users")
pipeline.extract()
pipeline.transform()
pipeline.load("users_clean.csv")
