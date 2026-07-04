import random

Num = random.randint(1, 10)
choice = 5
Flag = True

print("|Welcome to Number Guessing Game|")
print("|You get 5 choices|")

while Flag:

    user_choice = int(input("Enter a guess number: "))

    if user_choice < 1 or user_choice > 10:
        print("Invalid Input")
        continue

    choice -= 1

    if Num > user_choice:
        print("Your guess is too small!")

    elif Num < user_choice:
        print("Your guess is too large!")

    else:
        print("You won!")
        Flag = False

    if choice == 0 and Flag:
        print("Out of Choices!")
        print("The number was", Num)
        Flag = False

    elif Flag:
        print("Choices left:", choice)