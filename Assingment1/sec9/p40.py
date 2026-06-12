marks = [80, 90, 70, 85, 95]

average = sum(marks) / len(marks)

print("Average =", average)
print("Highest =", max(marks))

if average >= 90:
    print("A")
elif average >= 75:
    print("B")
elif average >= 50:
    print("C")
else:
    print("Fail")