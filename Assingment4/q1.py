class Student:
    school_name = "ABC College"

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_student(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("School:", Student.school_name)

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name


student1 = Student("Suraj", 20, "Python")
student2 = Student("Rahul", 21, "Data Science")

print("Before Changing School Name")
student1.display_student()
student2.display_student()

Student.change_school_name("XYZ College")

print("\nAfter Changing School Name")
student1.display_student()
student2.display_student()