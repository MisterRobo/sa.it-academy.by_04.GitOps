def sum(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the result of dividing two numbers.
       Throws an exception if the division is by zero.
    """
    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a / b
