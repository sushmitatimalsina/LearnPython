from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    "C:\\bigquery_key\\data-engineer-practice-481715-727e66147523.json"
)

client = bigquery.Client(
    credentials=credentials,
    project="data-engineer-practice"
)

dataset_id = f"{client.project}.my_dataset"
dataset = bigquery.Dataset(dataset_id)

dataset = client.create_dataset(dataset, exists_ok=True)
print(f"Dataset {dataset.dataset_id} created successfully")
