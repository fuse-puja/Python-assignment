""" Create a Python class to represent a University. The university should have
attributes like name, location, and a list of departments. Implement encapsulation to
protect the internal data of the University class. Create a Department class that
inherits from the University class. The Department class should have attributes like
department name, head of the department, and a list of courses offered. Implement
polymorphism by defining a common method for both the University and
Department classes to display their details."""

class University:
    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._departments = []

    def add_department(self, department):
        self._departments.append(department)

    def display_details(self):
        print(f"University Name: {self._name}")
        print(f"Location: {self._location}")
        print("Departments:")
        for department in self._departments:
            department.display_details()

class Department(University):
    def __init__(self, name, head_of_department):
        super().__init__(name, None) 
        self._head_of_department = head_of_department
        self._courses_offered = []

    def add_course(self, course):
        self._courses_offered.append(course)

    def display_details(self):
        print(f"Department Name: {self._name}")
        print(f"Head of Department: {self._head_of_department}")
        print("Courses Offered:")
        for course in self._courses_offered:
            print(f"  - {course}")

university = University("Pokhara University", "Pokhara")
dept = Department("Computer Science", "Prof. Ramcharan")
dept.add_course("Object Oriented Programming")
dept.add_course("Data Structures")
university.add_department(dept)
university.display_details()

""" Build a Python class to represent a simple banking system. Create a class for a
BankAccount, and another for Customer. The BankAccount class should have a
constructor to initialize the account details (account number, balance, account type).
The Customer class should have a constructor to set the customer's details (name,
age, address) and create a BankAccount object for each customer. Implement a
destructor for both classes to display a message when objects are destroyed."""

class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __del__(self):
        print(f"BankAccount {self.account_number} is being destroyed.")

class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = None

    def create_bank_account(self, account_number, balance, account_type):
        self.bank_account = BankAccount(account_number, balance, account_type)

    def __del__(self):
        print(f"Customer {self.name} is being destroyed.")


customer1 = Customer("Ram", 23, "Bhaktapur")
customer1.create_bank_account("76534", 1000, "Savings")