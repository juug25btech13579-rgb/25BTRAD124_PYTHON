# ---------------------------------------------------------------------------
# Lab Exercise 11: Log file reader program
# (needs a "log.txt" file in the same folder, with lines containing
#  ERROR, WARNING or INFO)
# ---------------------------------------------------------------------------
def lab11_log_file_reader():
    try:
        error_count = 0
        warning_count = 0
        info_count = 0

        with open("log.txt", "r") as file:
            for line in file:
                if "ERROR" in line:
                    error_count += 1
                elif "WARNING" in line:
                    warning_count += 1
                elif "INFO" in line:
                    info_count += 1

        print("\n--- LOG FILE SUMMARY ---")
        print("ERROR count:", error_count)
        print("WARNING count:", warning_count)
        print("INFO count:", info_count)

    except FileNotFoundError:
        print("Log file not found!")
    except Exception as e:
        print("An error occurred:", e)


# ---------------------------------------------------------------------------
# Lab Exercise 12: Student data manager using files
# ---------------------------------------------------------------------------
def lab12_student_data_manager():
    while True:
        print("\n--- STUDENT DATA MANAGER ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            roll = input("Enter roll number: ")
            marks = input("Enter marks: ")
            with open("students.txt", "a") as f:
                f.write(roll + "," + name + "," + marks + "\n")
            print("Student added successfully!")

        elif choice == 2:
            try:
                with open("students.txt", "r") as f:
                    print("\n--- STUDENT RECORDS ---")
                    for line in f:
                        roll, name, marks = line.strip().split(",")
                        print("Roll Number:", roll)
                        print("Name:", name)
                        print("Marks:", marks)
                        print()
            except FileNotFoundError:
                print("No student records found!")

        elif choice == 3:
            roll = input("Enter roll number to search: ")
            found = False
            try:
                with open("students.txt", "r") as f:
                    for line in f:
                        r, name, marks = line.strip().split(",")
                        if r == roll:
                            print("Student Found!")
                            print("Name:", name)
                            print("Marks:", marks)
                            found = True
                            break
                if not found:
                    print("Student not found!")
            except FileNotFoundError:
                print("File not found!")

        elif choice == 4:
            roll = input("Enter roll number to update: ")
            found = False
            try:
                with open("students.txt", "r") as f:
                    records = f.readlines()

                with open("students.txt", "w") as f:
                    for line in records:
                        r, name, marks = line.strip().split(",")
                        if r == roll:
                            name = input("Enter new name: ")
                            marks = input("Enter new marks: ")
                            found = True
                        f.write(r + "," + name + "," + marks + "\n")

                if found:
                    print("Student updated successfully!")
                else:
                    print("Student not found!")
            except FileNotFoundError:
                print("File not found!")

        elif choice == 5:
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


# ---------------------------------------------------------------------------
# Lab Exercise 13: CSV-based payroll management system
# (needs "employees.csv" with columns: Name,Basic,HRA,DA)
# ---------------------------------------------------------------------------
def lab13_payroll_system():
    try:
        with open("employees.csv", "r") as file:
            reader = csv.DictReader(file)
            print("\n--- EMPLOYEE PAYROLL ---")

            for row in reader:
                name = row["Name"]
                basic = float(row["Basic"])
                hra = float(row["HRA"])
                da = float(row["DA"])

                gross = basic + hra + da
                deduction = gross * 0.10
                net_salary = gross - deduction

                print("\nEmployee Name:", name)
                print("Basic Salary:", basic)
                print("HRA:", hra)
                print("DA:", da)
                print("Gross Salary:", gross)
                print("Deduction (10%):", deduction)
                print("Net Salary:", net_salary)

    except FileNotFoundError:
        print("CSV file not found!")
    except (ValueError, KeyError):
        print("Invalid employee data in CSV file!")
