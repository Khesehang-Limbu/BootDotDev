"""

Employee Management
"Age of Dragons, Inc." is growing rapidly. They need a way to keep track of all their employees. They've asked you to create an internal tool to help them manage their employees.

Challenge
Unfortunately, your team lead is asking you to make... an interesting design decision. She's asked you to use shared class variables to keep track of the company's name and the total number of employees inside of the Employee class. (You wanted to make a separate Company class, but she's the boss.)

Class Variables
Initialize the following class variables:

company_name set to "Age of Dragons, Inc.".
total_employees set to 0.
Constructor
The constructor should take the following parameters (in order) and set them to the corresponding instance variables:

first_name = first_name
last_name = last_name
id = id
position = position
salary = salary
Also, it should increment the total_employees class variable each time a new Employee is created. Remember, total_employees is a class variable, not an instance variable.

Getter
Add a get_name method that returns the employee's full name as a string (e.g. "John Carmack").

"""

class Employee:
    # ?
    company_name = "Age of Dragons, Inc."
    total_employees = 0

    def __init__(self, first_name, last_name, id, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.position = position
        self.salary = salary
        Employee.total_employees += 1

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

