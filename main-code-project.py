from employee import *

if __name__ == '__main__':
    try:
        # Here user is creating an "employee card" from the information he is given,
        # If one or more information is missing, the user is getting a message
        # that one or more information is missing, and he needs to try again.
        employee1 = Employee(1, 'Jane Doe', 972567824516, 23)
    except TypeError:
        print("You did not provide all the employee information."
              " One or more of these are missing: id, name, phone, age.")

    try:
        # Here the user is adding a new employee to the Employees-file,
        # Using the "employee card" that the user created above,
        # if the "employee card" is not exist,
        # the user is getting a message that he needs to add an existing employee.
        add_employee_manually_to_employees_file(employee1)
    except NameError:
        print("The employee that provided is not an employee here."
              " Please try to enter an employee again")


    # Here the user enters a file name that contains employees,
    # and the program adds all the employees in it to the Employees-file.
    # If the name of the file that the user has provided is not a real file,
    # an empty list will be added to the Employees-file
    add_employee_manually_from_file_to_employees_file(new_employees)


    try:
        # Here the user is deleting an employee from the Employees-file.
        # Using the "employee card" that the user created above,
        # if the "employee card" is not exist,
        # the user is getting a message that he needs to add an existing employee.
        delete_employee_manually_from_employees_file(employee1)
    except NameError:
        print("The employee that provided is not an employee here."
              " Please try to enter an employee again")


    # Here the user enters a file name that contains employees,
    # and the program deletes all the employees in it from the Employees-file.
    # If the name of the file that the user has provided is an empty file,
    # nothing will happen.
    delete_an_employee_in_employees_file_from_a_file(new_employees)


    try:
        # The employee enters his/her id
        # and the attendance is marked in the attendance-file.
        # If the employee enters something that is not an 'employee.id'
        # a message will say - you need to provide an id.
        log_enter(employee1.id)
    except TypeError:
        print("You did not provide your id!, Try again.")


    try:
        # The user enters an employee id
        # and all the entries of that given employee is printed out.
        # If the user enters something that is not an 'employee.id'
        # a message will say - you need to provide an id.
        attendance_report_of_an_employee(employee1.id)
    except TypeError:
        print("You did not provide your id!, Try again.")


    # Here the user enters 2 numbers,
    # the first is the month of the attendance report he/she wants
    # and the second number of the year.
    # What will be printed out is
    # the attendance report of all entries in that given month.
    attendance_report_of_month(10, 2020)


    # Here the user enters 2 numbers,
    # the first is the hour and the second is the minute,
    # the third number is the year
    # of the time the user wants to print the attendance report.
    # All the employees who entered after the time that is given are late.
    # What will be printed out is all the employees who are late that year.
    attendance_report_for_late_employees(9, 30, 2020)
