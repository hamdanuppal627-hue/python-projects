choice = input("Welcome to python course, Would you like to register or login? | ").lower()

username = "python"
password = "pythonisfun"

if choice != "register" and choice != "login":
    print("Please choose either register or login.")

elif choice == "login":
    username_input = input("Enter your username: ").lower()
    username_password = input("Enter your password: ")

    if username_input == username and username_password == password:
        print("Login successful ✅")
    else:
        print("Your credentials are not found! | ^_^")

elif choice == "register":
    username_register = input("Enter your username: ").lower()
    password_register = input("Enter your password: ")

    if username_register == "python" and password_register == "pythonisfun":
        print("Username and Password are already registered! Try logging in.")
    else:
        username = username_register
        password = password_register

        print("You have been registered successfully ✅")
        print("Your Username and Password are:")
        print(username + " " + password)