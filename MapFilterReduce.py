# Impementation of Map 

def square_numbers(input_list):
    """
    Calculate the square of each element in the input list using the map function.

    Args:
        input_list (list of int): List of integers.

    Returns:
        list of int: List containing the square of each element.
    """
    squared_list = list(map(lambda x: x ** 2, input_list))
    return squared_list
 

def convert_to_uppercase(input_list):
    """
    Convert each string in the input list to uppercase using the map function.

    Args:
        input_list (list of str): List of strings.

    Returns:
        list of str: List containing uppercase versions of input strings.
    """
    uppercase_list = list(map(lambda s: s.upper(), input_list))
    return uppercase_list

input_list = [1, 2, 3]
result = square_numbers(input_list)
print("Squared numbers are: ", result) 

input_list = ["hello", "pokhara"]
result = convert_to_uppercase(input_list)
print("After converting to uppercase: ", result) 


# Impementation of Filter 

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def filter_prime_numbers(numbers_list):
    """
    Filter prime numbers from the input list of integers using the filter function.

    Args:
        numbers_list (list): A list of integers.

    Returns:
        list: A new list containing only the prime numbers.

    """
    prime_numbers_iterator = filter(is_prime, numbers_list)
    prime_numbers_list = list(prime_numbers_iterator)
    return prime_numbers_list

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_prime_numbers(input_list)
print("Prime numbers are: ",result)

# Impementation of Reduce 

from functools import reduce

def calculate_factorial(n):
    """
    Calculate the factorial of the input integer using the reduce function.

    Args:
        n (int): Integer for which factorial needs to be calculated.

    Returns:
        int: Factorial of the input integer.
    """
    if n == 0 or n == 1:
        return 1
    factorial = reduce(lambda x, y: x * y, range(1, n + 1))
    return factorial

num = 5
result = calculate_factorial(num)
print("Factorial is: ", result)  
