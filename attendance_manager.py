import json
import os

import datetime


ID_FIELD = 'id'
START_WORK_AT_FIELD = 'start work at: '
DAY_FIELD = 'day'


class AttendanceManager:
    def __init__(self, attendance_file_path):
        self._attendance_file_path = attendance_file_path

    def load_attendance(self):
        # Providing a list of dictionaries of all the attendances
        # in the Attendance-file that the user can work with.
        if not os.path.exists(self._attendance_file_path):
            return []

        with open(self._attendance_file_path, 'r') as json_file:
            read_file = json_file.read()
            if read_file == "":
                return []
            log = json.loads(read_file)
            return log

    def save_log(self, log_list):
        # Saving a list of dictionaries of attendances
        # to the Attendance-file using a list of dictionaries.
        with open(self._attendance_file_path, 'w') as json_file:
            json_file.write(json.dumps(log_list, indent=2))

    def log_enter(self, employee_id):
        # Using the employee-id,
        # the employee is marking his/her attendance in the Attendance-file.
        log = self.load_attendance()
        today = datetime.date.today()
        time = datetime.datetime.now().time()
        entrance = {ID_FIELD: employee_id, DAY_FIELD: str(today), START_WORK_AT_FIELD: str(time)}
        log.append(entrance)
        self.save_log(log)

    def attendance_report_of_an_employee(self, employee_id):
        # Using an employee-id,
        # an attendance report will be printed out
        # with all the attendances of that employee.
        log = self.load_attendance()
        employee_report = []
        for entrance in log:
            if entrance[ID_FIELD] == employee_id:
                employee_report.append(entrance)
        return employee_report

    def attendance_report_of_month(self, month, year):
        # Using a year and a month,
        # an attendance report will be printed out
        # with all the attendances of that month.
        log = self.load_attendance()
        month_log = []
        for entrance in log:
            day = datetime.date.fromisoformat(entrance[DAY_FIELD])
            if (day.month == month and
                    day.year == year):
                month_log.append(entrance)
        return month_log

    def attendance_report_for_late_employees(self, hour, minute, year):
        # Using an hour and a minute,
        # an attendance report will be printed out
        # with all the employees who marked their attendance
        # past the minute that provided.
        log = self.load_attendance()
        late_attendance_report = []
        for entrance in log:
            time = datetime.time.fromisoformat(entrance[START_WORK_AT_FIELD])
            day = datetime.date.fromisoformat(entrance[DAY_FIELD])
            if (time.hour == hour and
                    time.minute >= minute and
                    day.year == year):
                late_attendance_report.append(entrance)
        return late_attendance_report
