import json
import os

file_path = 'Employees.json'


class Employee:
    def __init__(self, id, name, phone, age):
        self.id = id
        self.name = name
        self.phone = phone
        self.age = age

    def dict_employee(self):
        employee = {'id': self.id, 'name': self.name, 'phone': self.phone, 'age': self.age}
        return employee


employee1 = Employee(1, 'Jane Doe', 972567824516, 23)
employee2 = Employee(2, 'Luke Main', 972568930980, 25)


def load_employees():
    if not os.path.exists(file_path):
        return []

    with open('Employees.json', 'r') as json_file:
        read_file = json_file.read()
        if read_file == "":
            return []
        employees = json.loads(read_file)
        return [Employee(employee["id"], employee["name"], employee["phone"], employee["age"]) for employee in
                employees]


load_employees()


def save_employees(employees):
    dict_employees = [employee.dict_employee() for employee in employees]
    with open('Employees.json', 'w') as json_file:
        json_file.write(json.dumps(dict_employees, indent=2))


def add_employee_manually_to_employees_file(employee):
    employees = load_employees()
    employees.append(employee)
    save_employees(employees)


add_employee_manually_to_employees_file(employee1)
add_employee_manually_to_employees_file(employee2)
