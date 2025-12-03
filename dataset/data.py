users = [
    {"id": 1, "name": "John", "email": "john@example.com"},
    {"id": 2, "name": "Alice", "email": "alice@example.com"}
]

for user in users:
    print(f"{user['id']} - {user['name']} - {user['email']}")