class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

from employee import Employee  # Importing the Employee class from employee module

# Creating an Employee object
emp = Employee("John Doe", 50000)

# Displaying name and salary using methods
print("Employee Name:", emp.get_name())
print("Employee Salary:", emp.get_salary())
