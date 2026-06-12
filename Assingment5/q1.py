class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Suraj", 20)
s2 = Student("Rahul", 21)
s3 = Student("Amit", 22)

print(s1.name, s1.age)
print(s2.name, s2.age)
print(s3.name, s3.age)