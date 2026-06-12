# Intermediate Functions (Q26-Q30)

# Q26 - Rectangle area
def area(length, width):
    print(length * width)

area(10, 5)

# Q27 - Greater number
def greater(a, b):
    return a if a > b else b

print(greater(20, 15))

# Q28 - Print 1 to 10
def numbers():
    for i in range(1, 11):
        print(i)

numbers()

# Q29 - Sum of list
def list_sum(values):
    return sum(values)

print(list_sum([10, 20, 30, 40]))

# Q30 - Pass or Fail
def result(marks):
    if marks >= 35:
        print("Pass")
    else:
        print("Fail")

result(50)