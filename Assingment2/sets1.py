# Set Basics (Q11-Q15)

# Q11 - Create and print set
numbers = {10, 20, 30, 40, 50}

for num in numbers:
    print(num)

# Q12 - Add elements
numbers.add(60)
numbers.add(70)
print(numbers)

# Q13 - Remove elements
numbers.remove(70)
numbers.discard(60)
print(numbers)

# Q14 - Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)

# Q15 - Common elements
print(set1.intersection(set2))