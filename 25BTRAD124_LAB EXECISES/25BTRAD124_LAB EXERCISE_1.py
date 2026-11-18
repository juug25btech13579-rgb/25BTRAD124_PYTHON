Lab Exercise 1 (environment setup) has no code. Summary:
  1. Install Python from python.org and tick "Add Python to PATH";
     verify with `python --version`.
  2. Install VS Code (with the Python extension) or PyCharm and select
     the Python interpreter.
  3. Install Jupyter Notebook with `pip install notebook`, then run
     `jupyter notebook` to write code in separate cells.


import csv
import random


# ---------------------------------------------------------------------------
# Lab Exercise 2: Hello World
# ---------------------------------------------------------------------------
def lab2_hello_world():
    print("Hello World")


# ---------------------------------------------------------------------------
# Lab Exercise 3: Input and basic arithmetic
# ---------------------------------------------------------------------------
def lab3_basic_arithmetic():
    name = input("Enter your name: ")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Hello", name)
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: cannot divide by zero")


# ---------------------------------------------------------------------------
# Lab Exercise 4: Arithmetic operations and area of rectangle
# ---------------------------------------------------------------------------
def lab4_arithmetic_and_area():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)
    if b != 0:
        print("Division =", a / b)
    else:
        print("Division = cannot divide by zero")

    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print("Area of rectangle =", length * width)
