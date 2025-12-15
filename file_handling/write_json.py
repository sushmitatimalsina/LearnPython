import pandas as pd
import json

employee = {
    "name": "Ram",
    "role": "Data Analyst",
    "country": "Nepal"
}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)