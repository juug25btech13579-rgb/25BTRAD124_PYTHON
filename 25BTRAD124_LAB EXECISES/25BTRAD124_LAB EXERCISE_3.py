# ---------------------------------------------------------------------------
# Lab Exercise 8: Contact book using lists and dictionaries
# ---------------------------------------------------------------------------
def lab8_contact_book():
    contacts = []

    # Add Contact
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("\nContact added successfully!")

    # Display Contacts
    print("\nContact Details:")
    for c in contacts:
        print("Name:", c["name"])
        print("Phone:", c["phone"])
        print("Email:", c["email"])

    # Search Contact
    search = input("\nEnter name to search: ")
    for c in contacts:
        if c["name"] == search:
            print("Contact found!")
            print(c)
            break
    else:
        print("Contact not found!")

    # Update Contact
    update = input("\nEnter name to update: ")
    for c in contacts:
        if c["name"] == update:
            c["phone"] = input("Enter new phone number: ")
            c["email"] = input("Enter new email: ")
            print("Contact updated successfully!")
            break
    else:
        print("Contact not found!")

    # Delete Contact
    delete = input("\nEnter name to delete: ")
    for c in contacts:
        if c["name"] == delete:
            contacts.remove(c)
            print("Contact deleted successfully!")
            break
    else:
        print("Contact not found!")

    # Final Display
    print("\nFinal Contact List:")
    for c in contacts:
        print(c)


# ---------------------------------------------------------------------------
# Lab Exercise 9: Student grading system
# ---------------------------------------------------------------------------
def lab9_grading_system():
    students = {}
    n = int(input("Enter number of students: "))

    for _ in range(n):
        name = input("\nEnter student name: ")
        marks = float(input("Enter marks (0-100): "))
        students[name] = marks

    print("\n--- STUDENT GRADING SYSTEM ---")
    for name, marks in students.items():
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "F"

        print("\nStudent Name:", name)
        print("Marks:", marks)
        print("Grade:", grade)


# ---------------------------------------------------------------------------
# Lab Exercise 10: Frequency counter using dictionaries (word frequency)
# ---------------------------------------------------------------------------
def lab10_frequency_counter():
    sentence = input("Enter a sentence: ")
    frequency = {}

    for word in sentence.lower().split():
        frequency[word] = frequency.get(word, 0) + 1

    print("\n--- WORD FREQUENCY COUNTER ---")
    for word, count in frequency.items():
        print(word, ":", count)
