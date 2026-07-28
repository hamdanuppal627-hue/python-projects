import random
guess = random.randint(1, 10)
choice = 5
def num_guess(number):
    global choice
    global guess
    if 1 <= number <= 10:
        if number == guess:
            print(f"Correct! The number was {number}.\n")
            return True
        elif number > guess:
            print("Too high!")
            choice -= 1
        else:
            print("Too low!")
            choice -= 1
        print(f"You have {choice} choices left.\n")
    else:
        print("Invalid Input! Please enter a number between 1 and 10.\n")
    return False
flag = True
while flag and choice > 0:
    user_number = int(input("Enter your Number (1-10): "))
    game_won = num_guess(user_number)
    if game_won or choice == 0:
        if choice == 0 and not game_won:
            print(f"Game over! The correct number was {guess}.\n")
        user_choice = input("Do you want to play again? (yes/no): ").lower()
        if user_choice == 'yes':
            guess = random.randint(1, 10)
            choice = 5
            print("Starting a new game!\n")
        elif user_choice == 'no':
            flag = False
            print("Thanks for playing!")
        else:
            print("Invalid Input. Exiting game.")
            flag = False
