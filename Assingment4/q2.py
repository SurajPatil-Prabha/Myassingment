class Employee:
    employee_count = 0

    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
        Employee.employee_count += 1

    def display_employee(self):
        print("\nEmployee Details")
        print("ID:", self.emp_id)
        print("Name:", self.emp_name)
        print("Salary:", self.salary)

    @classmethod
    def show_total_employees(cls):
        print("\nTotal Employees:", cls.employee_count)


emp1 = Employee(101, "Amit", 35000)
emp2 = Employee(102, "Rahul", 45000)
emp3 = Employee(103, "Priya", 50000)

emp1.display_employee()
emp2.display_employee()
emp3.display_employee()

Employee.show_total_employees()