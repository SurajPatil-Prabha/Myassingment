# Dictionary Basics (Q1-Q5)

# Q1 - Create and print student dictionary values
student = {
    "name": "Suraj",
    "age": 20,
    "course": "Python",
    "city": "Mumbai"
}

for value in student.values():
    print(value)

# Q2 - Access employee details using keys
employee = {
    "name": "Rahul",
    "salary": 50000,
    "department": "IT"
}

print(employee["name"])
print(employee["salary"])
print(employee["department"])

# Q3 - Add new key-value pair
student["email"] = "suraj@gmail.com"
print(student)

# Q4 - Update existing value
student["city"] = "Pune"
print(student)

# Q5 - Remove keys
student.pop("email")
print(student)

del student["city"]
print(student)