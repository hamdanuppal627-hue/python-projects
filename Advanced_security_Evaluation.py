flag = True

Age = int(input("|Enter your Age: |"))
education_level = input("|Enter your Education level: |").lower()
Python_score = int(input("|Enter your Python skill (0-100): |"))
problem_solving = int(input("|Enter your problem-solving score: |"))
Number_project = int(input("|Enter Number of projects completed: |"))
Experience = int(input("|How many years of Experience do you have?: |"))
criminal_record = input("|Do you have any criminal record? (yes-no): |").lower()
coding_test_passed = input("|Did you pass your Coding test? (yes-no): |").lower()
interview_score = int(input("|What is your interview score? (0-100): |"))
discipline = input("|What is your Discipline rating? (high-medium-low): |").lower()



if Age >= 16 and (education_level == "alevel" or education_level == "university"):
    print("|You are eligible|")
else:
    print("|Rejected: Basic requirement not met|")
    flag = False



if flag == True:
    if criminal_record == "yes":
        print("|Rejected: Criminal record found|")
        flag = False
    else:
        print("|Security verification passed|")



if flag == True:
    if ((Python_score >= 80 and problem_solving >= 75) or 
        (Number_project >= 5 and Experience >= 2)):
        print("|Technical round passed|")
    else:
        print("|Technical round failed|")
        flag = False



if flag == True:
    if interview_score >= 85 and discipline == "high":
        print("|Congratulations! You are accepted|")

    elif ((interview_score >= 60 and interview_score <= 84) 
          or discipline == "medium"):
        print("|You need a further interview|")
        flag = False

    elif interview_score < 60 or discipline == "low":
        print("|You are rejected|")
        flag = False



if flag == True:
    if Python_score >= 95 and Number_project >= 10 and Experience >= 3:
        print("|Elite Developer Status Granted|")