import json


class Employee:
    def __init__(self, id, name, phone, age):
        self.id = id
        self.name = name
        self.phone = phone
        self.age = age


employee1 = Employee(1, 'Jane Doe', 972567824516, 23)
employee2 = Employee(2, 'Luke Main', 972568930980, 25)


def dict_employee(self):
    employee = {'id': self.id, 'name': self.name, 'phone': self.phone, 'age': self.age}
    return employee


def add_employee_manually_to_epmloyees_file(emp):
    x = dict_employee(emp)
    with open('Employees.json', 'a') as json_file:
        json_file.write(json.dumps(x) + ', \n')


add_employee_manually_to_epmloyees_file(employee1)
add_employee_manually_to_epmloyees_file(employee2)