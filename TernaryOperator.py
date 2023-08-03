# Implementation of ternary operators\

def check_odd_even(number):
    """
    Check if the input integer is even or odd using a ternary operator.

    Args:
        number (int): Integer to be checked.

    Returns:
        str: "Even" if the number is even, "Odd" if the number is odd.
    """
    result = "Even" if number % 2 == 0 else "Odd"
    return result

num1 = 44
num2 = 1
print(num1, "is", check_odd_even(num1))  
print(num2, "is",check_odd_even(num2))  

# Ternary operator to find leap year or not
def check_leap_year(year):
    """
    Check if the input year is a leap year using a ternary operator.

    Args:
        year (int): Year to be checked.

    Returns:
        str: "Leap Year" if the year is a leap year, "Not a Leap Year" otherwise.
    """
    result = "Leap Year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a Leap Year"
    return result


year1 = 2020
year2 = 1900
year3 = 2000
print(year1, "is", check_leap_year(year1))  
print(year2, "is", check_leap_year(year2)) 
print(year3, "is", check_leap_year(year3))  

#Ternary operator to find maximum number 
def find_bigger_number(a, b, c):
    """
    Find the larger number among three integers using a ternary operator.

    Args:
        a (int): First integer.
        b (int): Second integer.
        c (int): Third integer.

    Returns:
        int or str: Larger number among a, b, and c, or "Equal" if all three are equal.
    """
    result = max(a, b, c) if a != b != c else "Equal"
    return result

num1, num2, num3 = 5, 1, 9
print(find_bigger_number(num1, num2, num3))  

num4, num5, num6 = 2, 2, 2
print(find_bigger_number(num4, num5, num6))  
