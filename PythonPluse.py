import random
import time
def show_loading():
    print("Loading: ", end="")
    for i in range(5):
        time.sleep(0.2)
        print("■", end="", flush=True)
    print(" Done!")
session_logins = []
while True:
    print("\n1. Register | 2. Login | 3. Logs | 4. Exit")
    choice = input("Choose an option: ")
    match choice:
        case "1":
            name = input("Enter Name: ").strip()
            age_input = input("Enter Age: ").rstrip()
            try:
                age = int(age_input)
                roll = random.randint(100, 999)
                with open("students.txt", "a") as file:
                    file.write(f"{roll},{name},{age}\n")
                show_loading()
                print(f"Registered! Roll Number: {roll}")
            except ValueError:
                print("Error: Age must be a number.")
        case "2":
            user_roll = input("Enter Roll Number: ")
            user_name = input("Enter Name: ")
            try:
                login_success = False
                with open("students.txt", "r") as file:
                 database = file.read()
                 if f"{user_roll},{user_name}" in database:
                  show_loading()
                  print(f"Welcome {user_name}!")
                  session_logins.append(user_name)
                  login_success = True

                if not login_success:
                    print("Login Failed.")
            except FileNotFoundError:
                print("No database found.")
        case "3":
            print("Current Session Logins:")
            for user in session_logins:
                print(f"- {user}")
        case "4":
            print("Goodbye!")
            break
        case _:
            print("Invalid choice.")
