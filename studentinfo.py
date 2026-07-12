
student_1 = str(input("Enter the name of student 1: "))
student_2 = str(input("Enter the name of student 2: "))
student_3 = str(input("Enter the name of student 3: "))
student_4 = str(input("Enter the name of student 4: "))
student_5 = str(input("Enter the name of student 5: "))

# Ask which student to update (converted to integer)
choice = int(input("Which student do you want to update the name (1-5)? "))

if choice == 1:
    student_one = str(input("What's the new name? "))
    if student_1 == student_one:
        print("Student name is the same")
    else:
        student_1 = student_one

elif choice == 2:
    student_two = str(input("What's the new name? "))
    if student_2 == student_two:
        print("Student name is the same")
    else:
        student_2 = student_two

elif choice == 3:
    student_three = str(input("What's the new name? "))
    if student_3 == student_three:
        print("Student name is the same")
    else:
        student_3 = student_three

elif choice == 4:
    student_four = str(input("What's the new name? "))
    if student_4 == student_four:
        print("Student name is the same")
    else:
        student_4 = student_four

elif choice == 5:
    student_five = str(input("What's the new name? "))
    if student_5 == student_five:
        print("Student name is the same")
    else:
        student_5 = student_five

print("\nUpdated List:")
print("1.", student_1)
print("2.", student_2)
print("3.", student_3)
print("4.", student_4)
print("5.", student_5)
agechoice = ("which student do you want to add age?(1-5)")