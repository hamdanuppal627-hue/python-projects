std_marks = int(input("Enter Your marks: "))

if std_marks < 0 or std_marks > 100:
    print("Invalid Input!")
else:
    financial_aid = input("Do you have a Aid yes or no? ").lower()
    
    if std_marks <= 50:
        print("Unfortunately, you do not qualify for the scholarship.")
    elif std_marks >= 90 and financial_aid == "yes":
        print("Congratulations! You have been awarded a Full Scholarship")
    elif 50 <= std_marks <= 89 and std_marks % 2 == 0:
        print("You qualify for a Partial Scholarship")
    elif 50 <= std_marks <= 89 and std_marks % 2 != 0:
        print("You qualify for a base-level tuition grant.")