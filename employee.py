import json
import os


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


def add_employee_manually_to_epmloyees_file(emp):
    x = emp.dict_employee()
    with open('Employees.json', 'r') as json_file:



add_employee_manually_to_epmloyees_file(employee1)
add_employee_manually_to_epmloyees_file(employee2)
