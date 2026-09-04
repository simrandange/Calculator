"""
calculator.py

Core arithmetic functions for the calculator project.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(a, operator, b):
    """Apply the given operator ('+', '-', '*', '/') to a and b."""
    if operator not in OPERATIONS:
        raise ValueError(f"Unknown operator: {operator}")
    return OPERATIONS[operator](a, b)
