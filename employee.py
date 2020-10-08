import json


class Employee:
    def __init__(self, id, name, phone, age):
        self.id = id
        self.name = name
        self.phone = phone
        self.age = age


def dict_employee(self):
    employee = {"id": self.id, "name": self.name, "phone": self.phone, "age": self.age}
    return employee


employee1 = Employee(1, 'Jane Doe', 972568792519, 23)


def add_employee_manually_to_epmloyees_file(self):
    with open('Employees.jason', 'a') as json_file:
        x = dict_employee(self)
        json_file.write(json.dumps(x))


add_employee_manually_to_epmloyees_file(employee1)