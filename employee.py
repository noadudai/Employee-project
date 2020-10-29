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
        employee = {'id': self.id, 'name': self.name, 'phone': self.phone, 'age': self.age}
        return employee

    def __repr__(self):
        return F"Employee: {self.id}, {self.name}, {self.phone}, {self.age}"

    def __eq__(self, other):
        if not other:
            return False

        return self.id == other.id and self.name == other.name and \
               self.phone == other.phone and self.age == other.age


employee1 = Employee(1, 'Jane Doe', 972567824516, 23)
employee2 = Employee(2, 'Luke Main', 972568930980, 25)
employee3 = Employee(3, 'Noa Du', 972542027816, 23)


def load_employees():
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
    dict_employees = [employee.dict_employee() for employee in employees]
    with open(file_path, 'w') as json_file:
        json_file.write(json.dumps(dict_employees, indent=2))


def load_new_employees():
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
    employees = load_employees()
    employees.append(employee)
    save_employees(employees)


# new_employees = load_new_employees()


def add_employee_manually_from_file_to_employees_file(alist):
    employees = load_employees()
    for employee in alist:
        employees.append(employee)
    save_employees(employees)


# add_employee_manually_to_employees_file(employee1)
# add_employee_manually_to_employees_file(employee2)
# add_employee_manually_to_employees_file(employee3)


def delete_employee_manually_from_employees_file(employee):
    employees = load_employees()
    new_employees = []
    for emp in employees:
        if emp != employee:
            new_employees.append(emp)
    save_employees(new_employees)


def delete_an_employee_in_employees_file_from_a_file(alist):
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
    if not os.path.exists(attendance_file_path):
        return []

    with open(attendance_file_path, 'r') as json_file:
        read_file = json_file.read()
        if read_file == "":
            return []
        log = json.loads(read_file)
        return log


def save_log(log_list):
    with open(attendance_file_path, 'w') as json_file:
        json_file.write(json.dumps(log_list, indent=2))


def log_enter(employee_id):
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
    log = load_attendance()
    employee_report = []
    for entrance in log:
        if entrance['id'] == employee_id:
            employee_report.append(entrance)
    print(employee_report)


def attendance_report_of_month(month, year):
    log = load_attendance()
    month_log = []
    for entrance in log:
        day = datetime.date.fromisoformat(entrance['day'])
        if day.month == month and day.year == year:
            month_log.append(entrance)
    print(month_log)


def attendance_report_for_late_employees(minute):
    log = load_attendance()
    late_attendance_report = []
    for entrance in log:
        time = datetime.time.fromisoformat(entrance['start work at: '])
        if time.minute >= minute:
            late_attendance_report.append(entrance)
    print(late_attendance_report)
