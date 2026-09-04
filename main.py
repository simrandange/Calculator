"""
main.py

Simple command-line interface for the calculator.
Run with: python main.py
"""

from calculator import calculate, OPERATIONS


def get_number(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")


def get_operator(prompt):
    valid = ", ".join(OPERATIONS.keys())
    while True:
        op = input(prompt).strip()
        if op in OPERATIONS:
            return op
        print(f"Please enter a valid operator ({valid}).")


def main():
    print("=== Basic Calculator ===")
    print("Type 'q' at any prompt to quit.\n")

    while True:
        a_raw = input("Enter first number (or 'q' to quit): ").strip()
        if a_raw.lower() == "q":
            break
        try:
            a = float(a_raw)
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        op = get_operator(f"Enter operator ({', '.join(OPERATIONS.keys())}): ")
        b = get_number("Enter second number: ")

        try:
            result = calculate(a, op, b)
            # Print as an int if it's a whole number, otherwise as a float
            if result == int(result):
                result = int(result)
            print(f"Result: {a} {op} {b} = {result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")

    print("Goodbye!")


if __name__ == "__main__":
    main()
