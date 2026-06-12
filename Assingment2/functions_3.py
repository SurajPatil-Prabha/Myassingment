# Advanced Function Concepts (Q31-Q35)

# Q31 - Default argument
def display(name, city="Pune"):
    print(name, city)

display("Suraj")

# Q32 - Keyword arguments
def student_info(name, age):
    print(name, age)

student_info(age=20, name="Suraj")

# Q33 - Multiple arguments
def show_numbers(*args):
    for num in args:
        print(num)

show_numbers(10, 20, 30)

# Q34 - Maximum and Minimum
def max_min(numbers):
    return max(numbers), min(numbers)

print(max_min([10, 25, 5, 40]))

# Q35 - Count vowels
def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"

    for char in text:
        if char in vowels:
            count += 1

    return count

print(count_vowels("Python Programming"))