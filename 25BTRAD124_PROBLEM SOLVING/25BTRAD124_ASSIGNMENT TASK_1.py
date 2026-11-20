# Task 1: Print name, department and college, each on a separate line
def task1():
    print("Varshini")
    print("CSE-AIDE")
    print("Jain University")


# Task 2: Print a pattern of stars
def task2():
    print("*******")
    print("*******")
    print("*******")


# Task 3: Print using a single print() statement
def task3():
    print("Python is Easy")


# Task 4: Print number pattern
def task4():
    print("1\n12\n123\n1234\n12345")


# Task 5: Use \n to print Computer, Science, Engineering on separate lines
def task5():
    print("Computer\nScience\nEngineering")


# Task 6: Use \t to print Name, Age and City
def task6():
    print("Name\tAge\tCity")
    print("Varshini\t18\tBangalore")


# Task 7: Program with a single-line comment
def task7():
    # This program displays my name and department.
    name = "Varshini"
    department = "Computer Science"

    print("Name:", name)
    print("Department:", department)


# Task 8: Program using multi-line comments
def task8():
    """
    This is a multi-line comment.
    This program displays the student's name and department.
    It is written using basic Python.
    """
    name = "Varshini"
    department = "Computer Science"
    print("Name:", name)
    print("Department:", department)


# Task 9: Three comments and three print statements
def task9():
    # This is the first comment
    print("Hello, World!")
    # This is the second comment
    print("My name is Varshini")
    # This is the third comment
    print("Department: Computer Science")


# Task 10: Store your name in a variable and print it
def task10():
    name = "Varshini"
    print(name)


# Task 11: Store 10, 20, 30 in three variables and print them
def task11():
    a = 10
    b = 20
    c = 30

    print(a)
    print(b)
    print(c)


# Task 12: Convert the string "100" to an integer; show value and data type
def task12():
    value = "100"
    number = int(value)
    print("Value:", number)
    print("Data type:", type(number))


# Task 13: Convert integer 25 to float; show result and type
def task13():
    number = 25
    result = float(number)
    print("Value:", result)
    print("Data type:", type(result))


# Task 14: Accept age, convert to integer and display it
def task14():
    age = int(input("Enter your age: "))
    print("Your age is:", age)


# Task 15: Accept two numbers and display their sum
def task15():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    total = num1 + num2
    print("Sum =", total)


# Task 16: Accept student's name, age and CGPA and display them
def task16():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    cgpa = float(input("Enter CGPA: "))
    print(f"My name is {name}. I am {age} years old and my CGPA is {cgpa}.")


# Task 17: Celsius to Fahrenheit, F = (C * 9/5) + 32, two decimal places
def task17():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")


# Task 18: Even or odd using the % operator
def task18():
    num = int(input("Enter number: "))
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")


TASKS = {
    1: ("Print name, department, college", task1),
    2: ("Star pattern", task2),
    3: ("Single print() statement", task3),
    4: ("Number pattern", task4),
    5: ("Using \\n", task5),
    6: ("Using \\t", task6),
    7: ("Single-line comment", task7),
    8: ("Multi-line comment", task8),
    9: ("Three comments, three prints", task9),
    10: ("Variable called name", task10),
    11: ("Three variables", task11),
    12: ("String to integer", task12),
    13: ("Integer to float", task13),
    14: ("Accept age", task14),
    15: ("Sum of two numbers", task15),
    16: ("Student name, age and CGPA", task16),
    17: ("Celsius to Fahrenheit", task17),
    18: ("Even or odd", task18),
}


def main():
    while True:
        print("\n===== ASSIGNMENT TASKS - UNIT 1 =====")
        for number, (title, _) in TASKS.items():
            print(f"{number:>2}. {title}")
        print(" 0. Exit")

        try:
            choice = int(input("Select task number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            print("Goodbye!")
            break
        elif choice in TASKS:
            print(f"\n--- Task {choice}: {TASKS[choice][0]} ---")
            try:
                TASKS[choice][1]()
            except ValueError:
                print("Invalid input. Please enter the correct type of value.")
        else:
            print("Invalid task number.")


if __name__ == "__main__":
    main()
