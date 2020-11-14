
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

if __name__ == '__main__':
    employee1 = Employee(1, 'Jane Doe', 972567824516, 23)
    employee2 = Employee(2, 'Luke Main', 972568930980, 25)
    employee3 = Employee(3, 'Noa Du', 972542027816, 23)

