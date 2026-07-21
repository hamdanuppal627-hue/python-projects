name = []
standard_level = []
city = []
guardian_name = []
contact_number = []
flag = True
while flag:
    print("\n----Information----")
    print("1. Add a Student")
    print("2. Update a Student")
    print("3. Remove a Student")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name_student = input("Enter the student's name: ").lower()
        name.append(name_student)
        print("Updated names:", name)
        standard_level.append(int(input("Enter class level: ")))
        print("Updated classes:", standard_level)
        city.append(input("Enter city: ").lower())
        print("Updated cities:", city)
        guardian_name.append(input("Enter guardian name: ").lower())
        print("Updated guardians:", guardian_name)
        contact_number.append(int(input("Enter phone number: ")))
        print("Updated contacts:", contact_number)
        ans = input("Do you want to add another student? (yes/no): ").lower()
        if ans != "yes":
            print("Thank you for choosing my information system.")
            flag = False
    elif choice == "2":
        print("Current student names:", name)
        choice_2 = input("Enter the name you want to update: ").lower()
        if choice_2 in name:
            usefulShit = name.index(choice_2)
            print("What do you want to change? (Name, Level, City, Guardian, Contact)")
            field_choice = input("Enter choice: ").lower()
            if field_choice == "name":
                name[usefulShit] = input("Enter updated name: ").lower()
            elif field_choice == "level":
                standard_level[usefulShit] = int(input("Enter updated level: "))
            elif field_choice == "city":
                city[usefulShit] = input("Enter updated city: ").lower()
            elif field_choice == "guardian":
                guardian_name[usefulShit] = input("Enter updated guardian name: ").lower()
            elif field_choice == "contact":
                contact_number[usefulShit] = int(input("Enter updated contact: "))
            else:
                print("Invalid Input!")
        else:
            print("Name not found.")
    elif choice == "3":
        print("Current student names:", name)
        choice_3 = input("Enter the name of student you want to remove: ").lower()
        if choice_3 in name:
            useful_shit_2 = name.index(choice_3)
            name.pop(useful_shit_2)
            standard_level.pop(useful_shit_2)
            city.pop(useful_shit_2)
            guardian_name.pop(useful_shit_2)
            contact_number.pop(useful_shit_2)
            print(f"Information for {choice_3} has been removed successfully!")
        else:
            print("Name not found.")
    elif choice == "4":
        print("Thanks! We are available 24/7.")
        flag = False
    else:
        print("Invalid menu choice. Please select 1-4.")
