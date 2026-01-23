import csv

def read_data():
    with open("data_engineer_practice/data/users.csv", "r") as file:
        return list(csv.DictReader(file))

def validate_and_clean(users):
    clean_users = []

    for user in users:
        age = user["age"]
        city = user["city"].strip()

        # validation
        if age.isdigit() and int(age) > 0:
            if city == "Unknown" or city == "":
                user["city"] = "Not Provided"

            clean_users.append(user)

    return clean_users

def save_data(users):
    with open("data_engineer_practice/data/clean_users1.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["id", "name", "age", "city"]
        )
        writer.writeheader()
        writer.writerows(users)

def main():
    users = read_data()
    clean_users = validate_and_clean(users)
    save_data(clean_users)
    print("Pipeline completed successfully")

main()
