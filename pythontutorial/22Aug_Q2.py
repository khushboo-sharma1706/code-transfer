# Person
#     Args:
#         - Name
#         - Birth Year
#         - Income
#     Methods:
#         - Print Name
#         - Print Birth Year
#         - Print Income
#     Inherit:
#         - Employee
#             - Income: Take Input
#         - Student
#             - Income: 0

class Person:
    def __init__(self, name, birth_year, income):
        self.name = name
        self.birth_year = birth_year
        self.income = income

    def print_name(self):
        print(self.name)

    def print_birth_year(self):
        print(self.birth_year)

    def print_income(self):
        print(self.income)

    def is_employed(self):
        return False


class Employee(Person):
    def __init__(self, name, birth_year, income):
        super().__init__(name, birth_year, income)

    def is_employed(self):
        return True


class Student(Person):
    def __init__(self, name, birth_year):
        super().__init__(name, birth_year, 0)


a = []
employee = Employee("Ravi", 2000, 500000)
student = Student("Shankar", 2004)
a.append(employee)
a.append(student)

print(a)

employee.is_employed()

for per in a:
    if per.is_employed():
        print(f"{per.name} is employee")
        per.print_income()
    else:
        print(f"{per.name} is student")
