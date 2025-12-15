import pandas as pd
import json

employee = {
    "name": "Ram",
    "role": "Data Analyst",
    "country": "Nepal"
}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)

countries = {
    "countries": ["Nepal", "India", "USA", "UK"]
}

with open("countries.json", "w") as file:
    json.dump(countries, file, indent=4)    