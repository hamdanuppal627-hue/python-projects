admin_username = "admin"
admin_password = "admin123"
survey = []
ratings = []
while True:
    user_input_username = input("\nEnter your username (or type 'quit' to shut down code): ")
    if user_input_username.lower() == 'quit':
        print("System shutting down. Goodbye!")
        break
    user_input_password = input("Enter your Password: ")
    if user_input_password == admin_password and user_input_username == admin_username:
        admin = True
        print("-" * 14)
        print("Welcome Admin!")
        print("-" * 14)
    else:
        admin = False
        print("-" * 14)
        print("Welcome User!")
        print("-" * 14)
    if admin == True:
        while admin == True:
            print("\n1. Add a Survey")
            print("2. Remove a Survey")
            print("3. Edit a Survey")
            print("4. View Surveys")
            print("5. Log Out")
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                new_survey = input("Enter your Survey: ")
                survey.append(new_survey)
                ratings.append([])
                print("Survey added!")
            elif choice == 2:
                if len(survey) == 0:
                    print("There are no surveys.")
                else:
                    print("\nSurveys:")
                    for x in range(len(survey)):
                        print(f"{x + 1}. {survey[x]}")
                    index = int(input("Enter the survey number you want to remove: "))
                    index = index - 1
                    if index >= 0 and index < len(survey):
                        survey.pop(index)
                        ratings.pop(index)
                        print("Survey removed!")
                    else:
                        print("Invalid survey number!")
            elif choice == 3:
                if len(survey) == 0:
                    print("There are no surveys.")
                else:
                    print("\nSurveys:")
                    for x in range(len(survey)):
                        print(f"{x + 1}. {survey[x]}")
                    index = int(input("Enter the survey number you want to edit: "))
                    index = index - 1
                    if index >= 0 and index < len(survey):
                        survey[index] = input("Enter the new Survey: ")
                        print("Survey updated!")
                    else:
                        print("Invalid survey number!")
            elif choice == 4:
                if len(survey) == 0:
                    print("There are no surveys.")
                else:
                    print("\nSurveys:")
                    for x in range(len(survey)):
                        print(f"{x + 1}. {survey[x]}")
            elif choice == 5:
                print("Logging out Admin...")
                admin = False
            else:
                print("Invalid choice!")
    else:
        if len(survey) == 0:
            print("There are no surveys available.")
        else:
            print("\nAvailable Surveys:")
            for x in range(len(survey)):
                print(f"{x + 1}. {survey[x]}")
            choice = int(input("\nEnter the survey number you want to rate: "))
            choice = choice - 1
            if choice >= 0 and choice < len(survey):
                rating = int(input("Rate it from 1-5: "))
                if rating >= 1 and rating <= 5:
                    ratings[choice].append(rating)
                    print("Thank you for your rating!")
                    total = sum(ratings[choice])
                    amount = len(ratings[choice])
                    average = total / amount
                    print(f"Average Rating: {average:.1f}/5")
                else:
                    print("Rating must be between 1 and 5!")
            else:
                print("Invalid survey number!")
        print("\nReturning to the login screen...")
