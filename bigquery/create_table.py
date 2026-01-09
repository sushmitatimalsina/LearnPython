from google.cloud import bigquery
from google.oauth2 import service_account

# ✅ EXACT PATH TO YOUR JSON KEY
KEY_PATH = r"C:\bigquery_key\data-engineer-practice-481715-727e66147523.json"

credentials = service_account.Credentials.from_service_account_file(KEY_PATH)

client = bigquery.Client(
    credentials=credentials,
    project=credentials.project_id
)

table_id = "data-engineer-practice481715.practices_dw.user_details_python"

schema = [
    bigquery.SchemaField("user_id", "INTEGER"),
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("email", "STRING"),
    bigquery.SchemaField("city", "STRING"),
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)

print("✅ Table created successfully:", table.table_id)
