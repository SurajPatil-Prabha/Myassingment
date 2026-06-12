class School:
    total_students = 0

    def __init__(self, name):
        self.name = name
        School.total_students += 1

    @classmethod
    def show_total(cls):
        print(cls.total_students)

s1 = School("A")
s2 = School("B")

School.show_total()