import csv


class Employee:
    def __init__(self, id, name, phone, age):
        self.id = id
        self.name = name
        self.phone = phone
        self.age = age


with open('Employees.csv', 'w', newline='') as csv_employees_file:
    fieldnames = ['id', 'name', 'phone', 'age']
    writer = csv.DictWriter(csv_employees_file, fieldnames = fieldnames)
    writer.writeheader()


employee1 = Employee(1, "Jeane Dee", 972598386743, 23)


def add_employee_manually(self):
    with open('Employees.csv', 'a', newline='') as csvfile:
        fieldnames = ['id', 'name', 'phone', 'age']
        my_writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        my_writer.writerow({'id': self.id, 'name': self.name, 'phone': self.phone, 'age': self.age})


add_employee_manually(employee1)