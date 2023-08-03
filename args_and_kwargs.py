# Implementation of args

def sum_numbers(*args):
    """
    Calculate the sum of an arbitrary number of numbers.

    Args:
        *args: An arbitrary number of positional arguments (numbers).

    Returns:
        int: The sum of all the numbers.
    """
    total = 0
    for num in args:
        total += num
    return total


def concat_strings(*args):
    """
    Concatenate an arbitrary number of strings.

    Args:
        *args: An arbitrary number of positional arguments (strings).

    Returns:
        str: The concatenated string.
    """
    return ''.join(args)


print(sum_numbers(1, 2, 3, 4, 5))  
print(sum_numbers(10, 20, 30))

print(concat_strings("Hello", " ", "World"))  
print(concat_strings("This", " ", "is", " ", "a", " ", "string"))  
print(concat_strings("I", " ", "Love", " ", "Nepal"))

# Implementation of kwargs

def calculate_total_cost(**kwargs):
    """
    Calculate the total cost of items purchased from a store.

    Args:
        **kwargs: Arbitrary keyword arguments for items and their respective prices.

    Returns:
        float: The total cost of all items.
    """
    total_cost = sum(kwargs.values())
    return total_cost


print(calculate_total_cost(rice=199, daal=249, curry=120))
print(calculate_total_cost(shoes=5000, bag=1250,))

