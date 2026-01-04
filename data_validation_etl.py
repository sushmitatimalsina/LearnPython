import requests
import logging

def validate_user(user):
    if not user.get("id"):
        return False
    if not user.get("email"):
        return False
    return True


users = [
    {"id": 1, "email": "ram@gmail.com"},
    {"id": 2, "email": None}
]

valid_users = []

for user in users:
    if validate_user(user):
        valid_users.append(user)

print(valid_users)
def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("API error:", e)
        return []

logging.basicConfig(level=logging.INFO)

logging.info("ETL started")
logging.warning("Missing email detected")
logging.error("Database connection failed")