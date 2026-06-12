# More Set Operations (Q16-Q20)

# Q16 - Check value exists
set1 = {1, 2, 3, 4}

if 3 in set1:
    print("Exists")
else:
    print("Not Exists")

# Q17 - Remove duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
print(set(numbers))

# Q18 - Count unique students
students = {"Suraj", "Rahul", "Amit", "Suraj", "Priya"}
print(len(students))

# Q19 - Compare sets
s1 = {1, 2, 3}
s2 = {1, 2, 3}

if s1 == s2:
    print("Equal")
else:
    print("Not Equal")

# Q20 - Clear set
s1.clear()
print(s1)