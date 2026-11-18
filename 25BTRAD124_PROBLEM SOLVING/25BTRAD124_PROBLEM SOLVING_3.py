# Attendance Tracker using Lists and Dictionaries
students = {}
while True:
    print("\\n--- ATTENDANCE TRACKER ---")
    print("1. Add Student")
    print("2. Update Attendance")
    print("3. Display Attendance")
    print("4. Check Low Attendance")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        if name in students:
            print("Student already exists!")
        else:
            students[name] = []
            print("Student added successfully!")
    elif choice == "2":
        name = input("Enter student name: ")
        if name in students:
            status = input("Enter attendance (P/A): ").upper()
            if status in ["P", "A"]:
                students[name].append(status)
                print("Attendance updated successfully!")
            else:
                print("Invalid attendance status!")
        else:
            print("Student not found!")
    elif choice == "3":
        print("\\n--- ATTENDANCE DETAILS ---")
        if not students:
            print("No student records available!")
        for name, records in students.items():
            total = len(records)
            present = records.count("P")
            percentage = (present / total * 100) if total > 0 else 0
            print("Student:", name)
            print("Attendance records:", records)
            print("Attendance percentage: {:.2f}%".format(percentage))
    elif choice == "4":
        threshold = float(input("Enter attendance threshold (%): "))
        print("\\n--- STUDENTS BELOW THRESHOLD ---")
        found = False
        for name, records in students.items():
            total = len(records)
            percentage = (records.count("P") / total * 100) if total > 0 else 0
            if percentage < threshold:
                print(name, ":", "{:.2f}%".format(percentage))
                found = True
        if not found:
            print("No students below the threshold.")
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
