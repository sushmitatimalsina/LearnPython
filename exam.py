import pandas as pd

def clean_email(email):
    if email is None:
        return "noemail@unknown.com"
    return email.lower()

users = [
    {"id": 1, "name": "Ram"},
    {"id": 2, "name": "Sita"}
]

for user in users:
    print(user["name"])

for i in range(5):
    print(i)    

df = pd.read_csv("users.csv")    
df.to_csv("users_clean.csv", index=False)
df.drop_duplicates(inplace=True)
df.fillna("Unknown", inplace=True)