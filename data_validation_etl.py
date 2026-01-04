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
