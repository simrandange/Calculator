Basic Calculator

A simple Python command-line calculator supporting addition, subtraction, multiplication, and division.

Project Structure
calculator project:

-calculator.py       (core arithmetic functions)
-main.py              (command-line interface)
-test_calculator.py   (unit tests)
README.md

Requirements
Python 3.7+ 

Usage
Run the calculator from the project directory:
     bash
     python main.py

You will be prompted for a number, an operator (+, -, *, /), and a second number. Type q at the first prompt to quit.


Example-

   Basic Calculator 
Type 'q' at any prompt to quit.

Enter first number (or 'q' to quit): 10
Enter operator (+, -, *, /): /
Enter second number: 4
Result: 10.0 / 4.0 = 2.5

Enter first number (or 'q' to quit): q
Goodbye!


Running Tests
   bash
   python -m unittest test_calculator.py


Using as a Module
You can also import the calculator functions directly in your own scripts:
   python
   from calculator import add, subtract, multiply, divide, calculate
   add(2, 3)          # 5
   calculate(10, "/", 2)  # 5.0
