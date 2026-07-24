


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
