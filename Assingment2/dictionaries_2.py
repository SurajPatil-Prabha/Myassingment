

# Q6 - Print keys, values and pairs
data = {"a": 10, "b": 20, "c": 30}

for key in data.keys():
    print(key)

for value in data.values():
    print(value)

for key, value in data.items():
    print(key, value)

# Q7 - Count subjects
marks = {
    "Math": 80,
    "Science": 75,
    "English": 90,
    "History": 70
}

print(len(marks))

# Q8 - Calculate marks
marks5 = {
    "Math": 80,
    "Science": 75,
    "English": 90,
    "History": 70,
    "Computer": 95
}

print(sum(marks5.values()))

# Q9 - Check key exists
if "Math" in marks5:
    print("Key exists")
else:
    print("Key does not exist")

# Q10 - Products above 500
products = {
    "Mouse": 300,
    "Keyboard": 700,
    "Monitor": 12000,
    "Headphones": 1500
}

for product, price in products.items():
    if price > 500:
        print(product, price)