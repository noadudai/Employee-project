import json
import os
import datetime

file_path = 'Employees.json'
attendance_file_path = 'Attendance.json'
# new_path = str(input())


class Employee:
    def __init__(self, id, name, phone, age):
        self.id = id
        self.name = name
        self.phone = phone
        self.age = age

    def dict_employee(self):
        # Turning the employee instance into a dictionary
        employee = {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'age': self.age
        }
        return employee

    def __repr__(self):
        return F"Employee: {self.id}, {self.name}, {self.phone}, {self.age}"

    def __eq__(self, other):
        # Allowing the program to compare between instances.
        if not other:
            return False

        return self.id == other.id and self.name == other.name and \
               self.phone == other.phone and self.age == other.age


employee1 = Employee(1, 'Jane Doe', 972567824516, 23)
employee2 = Employee(2, 'Luke Main', 972568930980, 25)
employee3 = Employee(3, 'Noa Du', 972542027816, 23)


def load_employees():
    # Providing a list of all the employees
    # in the Employees-file that the user can work with.
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r') as json_file:
        read_file = json_file.read()
        if read_file == "":
            return []
        employees = json.loads(read_file)
        return [Employee(employee["id"], employee["name"], employee["phone"], employee["age"]) for employee in
                employees]


def save_employees(employees):
    # Saving a list of dictionaries of employees
    # to the Employees-file using a list of dictionaries.
    dict_employees = [employee.dict_employee() for employee in employees]
    with open(file_path, 'w') as json_file:
        json_file.write(json.dumps(dict_employees, indent=2))


def load_new_employees():
    # Providing a list of all the employees in a file that the user can work with.
    if not os.path.exists(new_path):
        return []

    with open(new_path, 'r') as json_file:
        read_file = json_file.read()
        if read_file == "":
            return []
        employees = json.loads(read_file)
        return [Employee(employee["id"], employee["name"], employee["phone"], employee["age"]) for employee in
                employees]

####################################################


def add_employee_manually_to_employees_file(employee):
    # Adding an employee instance to the Employees-file using the employee instance.
    employees = load_employees()
    employees.append(employee)
    save_employees(employees)


# new_employees = load_new_employees()


def add_employee_manually_from_file_to_employees_file(alist):
    # Adding an employee from a file to the Employees-file
    # using a list that contains all the employees in the file.
    employees = load_new_employees()
    for employee in alist:
        employees.append(employee)
    save_employees(employees)


# add_employee_manually_from_file_to_employees_file(new_employees)
# add_employee_manually_to_employees_file(employee1)
# add_employee_manually_to_employees_file(employee2)
# add_employee_manually_to_employees_file(employee3)


def delete_employee_manually_from_employees_file(employee):
    # Deleting an employee instance from the Employees-file
    # using the employee instance.
    employees = load_employees()
    new_employees = []
    for emp in employees:
        if emp != employee:
            new_employees.append(emp)
    save_employees(new_employees)


def delete_an_employee_in_employees_file_from_a_file(alist):
    # Deleting an employee that is in file from the Employees-file
    # using a list that contains all the employees in the file.
    employees = load_employees()
    new_employees_list = []
    for employee in employees:
        if employee not in alist:
            new_employees_list.append(employee)
    save_employees(new_employees_list)


# delete_an_employee_in_employees_file_from_a_file(new_employees)

#####################################################
#####################################################

def load_attendance():
    # Providing a list of dictionaries of all the attendances
    # in the Attendance-file that the user can work with.
    if not os.path.exists(attendance_file_path):
        return []

    with open(attendance_file_path, 'r') as json_file:
        read_file = json_file.read()
        if read_file == "":
            return []
        log = json.loads(read_file)
        return log


def save_log(log_list):
    # Saving a list of dictionaries of attendances
    # to the Attendance-file using a list of dictionaries.
    with open(attendance_file_path, 'w') as json_file:
        json_file.write(json.dumps(log_list, indent=2))


def log_enter(employee_id):
    # Using the employee-id,
    # the employee is marking his/her attendance in the Attendance-file.
    log = load_attendance()
    today = datetime.date.today()
    time = datetime.datetime.now().time()
    entrance = {'id': employee_id, 'day': str(today), 'start work at: ': str(time)}
    log.append(entrance)
    save_log(log)


# log_enter(employee1.id)
# log_enter(employee2.id)
# log_enter(employee3.id)


def attendance_report_of_an_employee(employee_id):
    # Using an employee-id,
    # an attendance report will be printed out
    # with all the attendances of that employee.
    log = load_attendance()
    employee_report = []
    for entrance in log:
        if entrance['id'] == employee_id:
            employee_report.append(entrance)
    print(employee_report)


def attendance_report_of_month(month, year):
    # Using a year and a month,
    # an attendance report will be printed out
    # with all the attendances of that month.
    log = load_attendance()
    month_log = []
    for entrance in log:
        day = datetime.date.fromisoformat(entrance['day'])
        if (day.month == month and
            day.year == year):
            month_log.append(entrance)
    print(month_log)


def attendance_report_for_late_employees(hour, minute, year):
    # Using an hour and a minute,
    # an attendance report will be printed out
    # with all the employees who marked their attendance
    # past the minute that provided.
    log = load_attendance()
    late_attendance_report = []
    for entrance in log:
        time = datetime.time.fromisoformat(entrance['start work at: '])
        day = datetime.date.fromisoformat(entrance['day'])
        if (time.hour == hour and
            time.minute >= minute and
            day.year == year):
            late_attendance_report.append(entrance)
    print(late_attendance_report)
