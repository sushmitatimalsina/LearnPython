import csv

data = [
    ['Name', 'Age', 'Grade'],
    ['David', 23, 'B'],
    ['Eva', 21, 'A']
]

# Write CSV file
with open('new_students.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)