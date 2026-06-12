class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

e1 = Employee(101, "Suraj", 25000)
print(e1.emp_id, e1.name, e1.salary)