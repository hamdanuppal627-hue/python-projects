# def candies():
#     candies = ["chocolate","White chocolate","sour patch", "Diary milk"]
#     print(f"Hi {name}, How you doin?")
#     print(candies)
#     inp_candy = input("Enter the Chocolate you want to add to the list: ")
#     candies.append(inp_candy)
#     choice = input("Which chocolate you love from the list: ")
#     if choice in candies:
#         print(f"So you love {choice}, You know what is Also like {choice}")
#     else:
#         print("invalid Choice(Candy not in list!)")
# name = input("Enter your name: ")
# candies()


# def information():
#     if info_about == "yourself" or info_about == "mother" or info_about == "father":
#         print(f"Hello {name}, How you doin!")
#         print(f"So you were born in {year}")
#         age = 2026 - year
#         print(f"Your age is {age}")
#         if age > 25:
#             print("How does it feel to live with a dinosaur?")
#         else:
#             print(f"You are just {age}. You unc!")
#     else:
#         print("Invalid input!(Input should be(Yourself|mother|father))")
# info_about = input("For which person is this information (mother/father/yourself)? ").lower()
# name = input("Enter your name: ")
# year = input("Which year were you born in? ")
# if year.isdigit():
#     year = int(year)
# else:
#     print("Invalid input 'AGE' should only be a integer!!!")
    
# information()


# array = [34,34,23,45,67,24]
# def calculated_number(numbers):
#   total = 0
#   for x in numbers:
#      total = total + x
#   return total
# print(calculated_number(array))


Task = []
while True:
    print("\n-------------")
    print("Task Manager")
    print("-------------")
    print("1. Add a Task")
    print("2. Remove a Task")
    print("3. Replace a Task")
    print("4. Exit")
    choice = input("Enter your choice(1-4): ")
    def add_task():
        print("Current Tasks:", Task)
        Task_Add = input("Enter your Task: ")
        Task.append(Task_Add)
        print("Task added!", Task)
    def remove_task():
        print("Current Tasks:", Task)
        Task_remove = input("Enter the Task you want to remove: ")
        if Task_remove in Task:
            Task.remove(Task_remove)
            print("Task removed!", Task)
        else:
            print("Task not found!")
    def replace_task():
        print("Current Tasks:", Task)
        try:
            Task_replace = int(input("Enter the task number you want to replace: ")) - 1
            if 0 <= Task_replace < len(Task):
                input_replace = input("Enter the new text: ")
                Task[Task_replace] = input_replace
                print("Here is your updated list:", Task)
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= 4:
            if choice == 1:
                add_task()
            elif choice == 2:
                remove_task()
            elif choice == 3:
                replace_task()
            elif choice == 4:
                print("Goodbye!")
                break
        else:
            print(f"{choice} isn't in the Menu!")
    else:
        print(f"'{choice}' is not an integer!")
