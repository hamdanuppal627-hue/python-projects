username = "admin"
password = "admin123"
print("\n|Welcome To Social Survey App!|")
user_identify = input("Are you admin or User?: ").lower()
if user_identify == "admin":
    print("|Welcome Admin|")
    user_name = input("Enter your Username: ")
    pass_word = input("Enter your Password: ")
    if user_name == username and pass_word == password:
        print("Login Successful!")
        flag = True
        while flag == True:
            print("1. Add Survey\n2. Clear All Data\n3. List Surveys\n4. Exit")
            input_choice = int(input("Enter option (1-4): "))
            
            if input_choice == 1:
                add_survey = input("Enter a topic you want to poll users on: ")
                with open("Poll.txt", 'a', encoding='utf-8') as file:
                    file.write(add_survey + "\n")
            elif input_choice == 2:
                with open("Poll.txt", "w", encoding="utf-8") as file: file.write("")
                with open("Votes.txt", "w", encoding="utf-8") as file: file.write("")
                print("All data cleared.")
            elif input_choice == 3:
                with open("Poll.txt", "r", encoding="utf-8") as file:
                    print(file.read())
            elif input_choice == 4:
                flag = False
elif user_identify == "user":
    print("Active Surveys:")
    with open("Poll.txt", "r", encoding="utf-8") as file:
        print(file.read()) 
    target_topic = input("Type the exact survey topic you want to vote on: ")
    user_vote = input("Do you agree or disagree?: ").lower()
    with open("Votes.txt", "a", encoding="utf-8") as file:
        file.write(target_topic + "," + user_vote + "\n")
    print("Vote recorded!")
    total_votes = 0
    agree_votes = 0

    with open("Votes.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line.strip(): 
                stored_topic, stored_vote = line.strip().split(",")
                if stored_topic == target_topic:
                    total_votes = total_votes + 1
                    if stored_vote == "agree":
                        agree_votes = agree_votes + 1
    agree_percentage = (agree_votes / total_votes) * 100
    print("\n--- Results for: " + target_topic + " ---")
    print("Total Votes: " + str(total_votes))
    print("Agree: " + str(agree_percentage) + "%")
    print("Disagree: " + str(100 - agree_percentage) + "%")
