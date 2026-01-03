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