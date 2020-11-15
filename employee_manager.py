import json
import os

from employee import Employee


class EmployeeManager:
    def __init__(self, employee_file_path):
        self._employee_file_path = employee_file_path

    def load_employees(self):
        # Providing a list of all the employees
        # in the Employees-file that the user can work with.
        if not os.path.exists(self._employee_file_path):
            return []

        with open(self._employee_file_path, 'r') as json_file:
            read_file = json_file.read()
            if read_file == "":
                return []
            employees = json.loads(read_file)
            return [Employee(employee["id"], employee["name"], employee["phone"], employee["age"]) for employee in
                    employees]

    def save_employees(self, employees):
        # Saving a list of dictionaries of employees
        # to the Employees-file using a list of dictionaries.
        dict_employees = [employee.dict_employee() for employee in employees]
        with open(self._employee_file_path, 'w') as json_file:
            json_file.write(json.dumps(dict_employees, indent=2))

    def add_employee_manually_from_file_to_employees_file(self, employees):
        # Adding an employee from a file to the Employees-file
        # using a list that contains all the employees in the file.
        loaded_employees = self.load_employees()
        for employee in employees:
            loaded_employees.append(employee)
        self.save_employees(loaded_employees)

    def add_employee_manually_to_employees_file(self, employee):
        # Adding an employee instance to the Employees-file using the employee instance.
        employees = self.load_employees()
        employees.append(employee)
        self.save_employees(employees)

    def delete_employee_manually_from_employees_file(self, employee):
        # Deleting an employee instance from the Employees-file
        # using the employee instance.
        employees = self.load_employees()
        new_employees = []
        for emp in employees:
            if emp != employee:
                new_employees.append(emp)
        self.save_employees(new_employees)

    def delete_an_employee_in_employees_file_from_a_file(self, employees):
        # Deleting an employee that is in file from the Employees-file
        # using a list that contains all the employees in the file.
        loaded_employees = self.load_employees()
        new_employees_list = []
        for employee in loaded_employees:
            if employee not in employees:
                new_employees_list.append(employee)
        self.save_employees(new_employees_list)
