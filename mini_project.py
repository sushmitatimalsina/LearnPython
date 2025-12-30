import pandas as pd
import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()
print(f"Fetched {len(data)} users from API")