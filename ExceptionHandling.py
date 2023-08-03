
#Implementation of exception handling 

def divide_numbers(num1, num2):
    """
    Perform division between two numbers.

    Args:
        num1 (int): The dividend.
        num2 (int): The divisor.

    Returns:
        float or str: The division result if num2 is not zero, otherwise an error message.
    """
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
division_result = divide_numbers(num1, num2)
print("Division Result:", division_result)


# exception handling for file not found

def display_file_contents(filename):
    """
    Display the contents of a file.

    Args:
        filename (str): Name of the file to be opened and displayed.

    Returns:
        None
    """
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File Contents:")
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

filename = input("Enter the filename: ")
display_file_contents(filename)

# exception handling for value error

try:
    user_input = input("Enter an integer: ")
    converted_integer = int(user_input)
    print("Converted Integer:", converted_integer)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

# exception handling using custom expection

class InvalidAgeError(Exception):
    """Custom exception for invalid age values."""
    pass

def check_age(age):
    """
    Check if the given age is valid.

    Args:
        age (int): Age to be checked.

    Raises:
        InvalidAgeError: If age is below 0 or above 120.
    """
    if age < 0 or age > 120:
        raise InvalidAgeError("Invalid age: Age should be between 0 and 120")

try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Valid age:", age)
except ValueError:
    print("Error: Please enter a valid integer.")
except InvalidAgeError as e:
    print(e)

# Custom Exception handling inheriting Exception

class WeakPasswordError(Exception):
    """Custom exception for weak passwords."""
    pass

def check_password_strength(password):
    """
    Check if the given password meets the minimum length requirement.

    Args:
        password (str): Password to be checked.

    Raises:
        WeakPasswordError: If password is shorter than 8 characters.
    """
    if len(password) < 8:
        raise WeakPasswordError("Weak password: Password should be at least 8 characters long.")

try:
    password = input("Enter a password: ")
    check_password_strength(password)
    print("Strong password:", password)
except WeakPasswordError as e:
    print(e)

