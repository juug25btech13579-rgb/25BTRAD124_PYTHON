# ---------------------------------------------------------------------------
# Lab Exercise 14: Bank account system using OOP
# ---------------------------------------------------------------------------
class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance")

    def balance_enquiry(self):
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Current Balance:", self.__balance)


def lab14_bank_account():
    account = BankAccount("Varshini", 101, 5000)

    while True:
        print("\n--- BANK ACCOUNT SYSTEM ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Enquiry")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == 3:
            account.balance_enquiry()
        elif choice == 4:
            print("Thank you for using our bank!")
            break
        else:
            print("Invalid choice")


# ---------------------------------------------------------------------------
# Lab Exercise 15: Library management system
# ---------------------------------------------------------------------------
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Availability:", "Available" if self.available else "Issued")

    def issue_book(self):
        if self.available:
            self.available = False
            print("Book issued successfully!")
        else:
            print("Book is already issued")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned successfully!")
        else:
            print("Book was not issued")


def lab15_library_management():
    book = Book(101, "Python Programming", "Guido van Rossum")

    while True:
        print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
        print("1. Display Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            book.display()
        elif choice == 2:
            book.issue_book()
        elif choice == 3:
            book.return_book()
        elif choice == 4:
            print("Thank you!")
            break
        else:
            print("Invalid choice")


# ---------------------------------------------------------------------------
# Lab Exercise 16: Dice simulator using random module
# ---------------------------------------------------------------------------
def lab16_dice_simulator():
    while True:
        print("\n--- DICE SIMULATOR ---")
        print("1. Roll Dice")
        print("2. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter number of dice: "))
            if n <= 0:
                print("Enter a valid number of dice")
                continue
            for i in range(n):
                result = random.randint(1, 6)
                print("Dice", i + 1, ":", result)
        elif choice == 2:
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice")


# ---------------------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------------------
EXERCISES = {
    2: ("Hello World", lab2_hello_world),
    3: ("Input and basic arithmetic", lab3_basic_arithmetic),
    4: ("Arithmetic operations and area of rectangle", lab4_arithmetic_and_area),
    5: ("Number guessing game", lab5_guessing_game),
    6: ("Prime number and factorial", lab6_prime_and_factorial),
    7: ("Fibonacci series using recursion", lab7_fibonacci),
    8: ("Contact book (lists and dictionaries)", lab8_contact_book),
    9: ("Student grading system", lab9_grading_system),
    10: ("Frequency counter (dictionaries)", lab10_frequency_counter),
    11: ("Log file reader", lab11_log_file_reader),
    12: ("Student data manager (files)", lab12_student_data_manager),
    13: ("CSV-based payroll system", lab13_payroll_system),
    14: ("Bank account system (OOP)", lab14_bank_account),
    15: ("Library management system", lab15_library_management),
    16: ("Dice simulator (random module)", lab16_dice_simulator),
}


def main():
    while True:
        print("\n===== PYTHON LAB EXPERIMENTS =====")
        for number, (title, _) in EXERCISES.items():
            print(f"{number:>2}. {title}")
        print(" 0. Exit")

        try:
            choice = int(input("Select exercise number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            print("Goodbye!")
            break
        elif choice in EXERCISES:
            print(f"\n--- Lab Exercise {choice}: {EXERCISES[choice][0]} ---")
            try:
                EXERCISES[choice][1]()
            except ValueError:
                print("Invalid input. Please enter the correct type of value.")
        else:
            print("Invalid exercise number.")


if __name__ == "__main__":
    main()
