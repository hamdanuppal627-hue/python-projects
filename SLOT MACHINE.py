import random
age = int(input("Enter your age: "))
if age < 18:
    print("Access Denied! You must be 18 or older to play.")
else:
    amount = int(input("Enter the amount you want to Deposit(100-5000$): "))
    if amount < 100 or amount > 5000:
        print("Invalid amount! | Amount should be between(100-5000$)")
    else:
        balance = amount  
        flag = True
        print("\n----------------")
        print("Welcome to Slots")
        print("----------------")
        print("| EACH SPIN IS WORTH 50$ |")
        while flag == True:
            print(f"\nYour Balance is {balance}$")
            choice = input("Do you want to play? (press Enter to play, or 'no' to quit): ").lower()
            if choice != "no":
                if balance < 50:
                    print("Low Balance! Game Over.")
                    flag = False
                    continue
                balance -= 50
                slot = ["🎰", "🪙", "🍒", "💎" , "🃏"]
                roll_1 = random.choice(slot)
                roll_2 = random.choice(slot)
                roll_3 = random.choice(slot)
                print(f"[ {roll_1} | {roll_2} | {roll_3} ]")
                if roll_1 == roll_2 == roll_3:
                    print("You Won! +50$")
                    balance += 100
                    print(f"Your New Balance is {balance}$")
                elif roll_1 == roll_2 or roll_2 == roll_3 or roll_1 == roll_3:
                    print("You Lost 10$")
                    balance += 40
                    print(f"Your New Balance is {balance}$")
                else:
                    print("You Lost 50$")
                    print(f"Your New Balance is {balance}$")
            else:
                print(f"Thank you for playing! You walked away with {balance}$.")
                print("We Are Available 24/7!")
                flag = False
