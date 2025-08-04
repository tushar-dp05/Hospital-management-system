def add_patient():
    name = input("Enter patient's name: ").strip()
    age = input("Enter patient's age: ").strip()
    condition = input("Enter patient's condition: ").strip()
    with open('patients.txt', 'a') as file:
        file.write(f"{name},{age},{condition}\n")
    print("Patient added successfully!\n")

def view_patients():
    try:
        with open("patients.txt", 'r') as file:
            patients = file.readlines()
            if not patients:
                print("No patients found.\n")
            else:
                print("List of patients:")
                for patient in patients:
                    name, age, condition = patient.strip().split(',')
                    print(f"Name: {name}, Age: {age}, Condition: {condition}")
                print()
    except FileNotFoundError:
        print("No patients found. Please add a patient first.\n")


while True:
    print("Welcome to the JBMM Patient Management System!")
    print("1. Add a new patient")
    print("2. View all patients")
    print("3. Exit")

    choice = input(" enter your choice : ")
    if choice == '1':
        add_patient()
    elif choice == '2':
        view_patients()
    elif choice == '3':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.\n")
