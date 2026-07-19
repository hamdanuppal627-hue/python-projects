To_do = []
flag = True
while flag == True:
    print("\n -----Task Manager-----")
    print("1. Add a Task")
    print("2. Remove a Task")
    print("3. Update a Task")
    print("4. Exit")
    user_choice = int(input("Input a Task you want to execute(1-4): "))
    if user_choice == 1:
        user_input_1 = input("Enter your Task: ")
        if user_input_1 in To_do:
            print("The task already exist in the List Do you want to add anyways(yes-no)")
            if input().lower() == "no":
                print("Task Not added")
            else:
                To_do.append(user_input_1)
        else:
            To_do.append(user_input_1)
        print("Your Updated List is", To_do) 
    elif user_choice == 2:
        print("Here is your Task List: ")
        print(To_do)
        user_input_2 = int(input("Enter the Task You want to remove in Integer!: "))
        user_comp = user_input_2 - 1
        To_do.pop(user_comp) 
        print("Here is your Updated list", To_do) 
    elif user_choice == 3:
        print("Here is your Task list: ")
        print(To_do)
        user_input_3 = int(input("Enter the Task you want to update: "))
        user_comp_2 = user_input_3 - 1
        task_updated = input("Enter your updated Task: ")
        To_do[user_comp_2] = task_updated 
        print("Here is your Updated List", To_do)
    elif user_choice == 4:
        flag = False
        print("Goodbye!")
    else:
        print("Invalid Input!")
