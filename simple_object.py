student = {
    "name": "Sushmita Timalsina",
    "age": 22,
    "courses": ["Math", "Science", "History"]
    
}

print(student)
print(student["name"])
print(student["courses"][1])
student["age"] = 23
student["email"] = "ajjashdahsj@gmail.com"
print(student)
del student["age"]
print(student)

