import random
import time
std_name = []
std_age = []
std_city = []
std_id = []
count = 0
choice = input("Do you want to add a student for admission? (yes/no): ").lower()
while True:
    if choice == "no":
        break
    elif choice == "yes":
        name = input("Enter the student's name: ")
        std_name.append(name)
        age = int(input("Enter the student's age: "))
        std_age.append(age)
        city = input("Enter the student's city: ")
        std_city.append(city)
        student_id = random.randint(1000, 9999)
        std_id.append(student_id)
        print("The student's ID is:", student_id)
        count += 1
        choice = input("Do you want to add a new student? (yes/no): ").lower()
        if choice == "no":
            break
    else:
        print("Invalid input")
        break
count_2 = 0
ext = input("Do you want to get information of all students stored? (yes/no): ").lower()
if ext == "yes":
    while count_2 < count:
        print("\nStudent ID:", std_id[count_2])
        print("Student Name:", std_name[count_2])
        print("Student Age:", std_age[count_2])
        print("Student City:", std_city[count_2])
        count_2 += 1
else:
    print("Thank you for registering!")
print("Loading...")
for i in range(10):
    print("█", end="", flush=True)
    time.sleep(0.5)
print("\nDone!")
print("\nYour Information has been updated in our Database!")
while True:
    user_preference = input("Do you want to login into your School portal (Yes-No): ").lower()
    if user_preference == "yes":
        IDS = int(input("Enter your id number: "))
        name_login = input("Enter your username: ")
        if name_login in std_name:
            name_index = std_name.index(name_login)
            if IDS == std_id[name_index]:
                print("Login successful")
                break
            else:
                print("Incorrect ID")
                break
        else:
            print("Username not found")
            break
    elif user_preference == "no":
        print("Thank you for visiting!")
        break
    else:
        print("Invalid choice!")
scholorship = input("Are you Interested in A scholarship?: ").lower()
valid_grades = ["A*", "A", "B", "C", "D", "E", "F", "G", "U"]
if scholorship == "yes":
    while True:
        Islamiat = input("Enter your Islamiat grade (A*-U): ").upper()
        if Islamiat in valid_grades:
            print("Grade accepted:", Islamiat)
            break
        else:
            print("Invalid grade! Please enter a grade from A* to U.")
    while True:
        pakistanstudies = input("Enter your pakistan-studies grade (A*-U): ").upper()
        if pakistanstudies in valid_grades:
            print("Grade accepted:", pakistanstudies)
            break
        else:
            print("Invalid grade! Please enter a grade from A* to U.")
    while True:
        Urdu = input("Enter your Urdu grade (A*-U): ").upper()
        if Urdu in valid_grades:
            print("Grade accepted:", Urdu)
            break
        else:
            print("Invalid grade! Please enter a grade from A* to U.")
    match Islamiat:
        case "A*": grade_islamiat = 7
        case "A":  grade_islamiat = 6
        case "B":  grade_islamiat = 5
        case "C":  grade_islamiat = 4
        case "D":  grade_islamiat = 3
        case "E":  grade_islamiat = 2
        case "U":  grade_islamiat = 1
        case _:    grade_islamiat = 0
    match pakistanstudies:
        case "A*": grade_pakistanstudies = 7
        case "A":  grade_pakistanstudies = 6
        case "B":  grade_pakistanstudies = 5
        case "C":  grade_pakistanstudies = 4
        case "D":  grade_pakistanstudies = 3
        case "E":  grade_pakistanstudies = 2
        case "U":  grade_pakistanstudies = 1
        case _:    grade_pakistanstudies = 0
    match Urdu:
        case "A*": grade_urdu = 7
        case "A":  grade_urdu = 6
        case "B":  grade_urdu = 5
        case "C":  grade_urdu = 4
        case "D":  grade_urdu = 3
        case "E":  grade_urdu = 2
        case "U":  grade_urdu = 1
        case _:    grade_urdu = 0
    if grade_islamiat == 7 and grade_pakistanstudies == 7 and grade_urdu == 7:
        print("Absolutely nailed it! You get 100% scholarship")
    elif grade_islamiat > 5 and grade_pakistanstudies > 4 and grade_urdu > 6:
        print("Congratulations! You got a 50% scholarship")
    else:
        print("Better luck next time")
