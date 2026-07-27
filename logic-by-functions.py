# # This program grades student based on their marks

def grade(marks):
    if marks >= 90 and marks <= 100:
        print(f"You got a A*!")
    elif marks >= 80 and marks <= 89:
        print(f"You got a A!")
    elif marks >=70 and marks <=79:
        print(f"You got a B!")
    elif marks >= 60 and marks <=69:
        print(f"You got a C!")
    elif marks >=50 and marks <= 59:
        print(f"You got a D!")
    elif marks < 0 or marks > 100:
        print("Invalid Input!")
    else:
        print("You Failed!!")
flag = True
count = 1
while flag == True:
    marks = float(input(f"Enter the marks for the {count} student: "))
    count += 1
    grade(marks)
    choice = input("Do you want to know the marks for another student? (yes-no)").lower()
    if choice == "yes":
        print("Moving on!")
    elif choice == "no":
        print("Thanks for choosing our grading system")
        flag = False
    else:
        print("Invalid Input!")
        flag = False

# This program Calculates the applied tax on your shopping amount

amount = float(input("Enter your total amount: "))
def tax_calculator(amount):
    tax_rate = 0.10
    print("Tax rate is 10%")
    total = amount + (amount * tax_rate)
    return total
while True:
    choice = input("Do you want to checkout?(yes-no): ").lower()
    if choice == "yes":
        print("Your total incl tax is:",tax_calculator(amount))
    elif choice == 'no':
        print("Thanks for choosing our service!")
        break
    else:
        print("Invalid Input!(yes-no" )
        break

# This program calculates the sum-avg-subject passed for a student

def marks_analyzer(subject):
    subject_passed = 0
    total = 0
    for x in range(subject):
        subject_number = x + 1
        while True:
            score = float(input(f"Enter the marks of the {subject_number} subject: "))
            if score < 0 or score > 100:
                print("Invalid Input!")
            else:
                break
        total += score
        if score >= 50:
            subject_passed += 1
    avg = total / subject
    return total, avg, subject_passed
subject = int(input("Enter the Number of Subjects you have: "))
total, avg, subject_passed = marks_analyzer(subject)
print("Sum Marks of all the Subjects is:", total)
print("Average Marks of the Subjects is:", avg)
print("You passed in", subject_passed, "subjects")


# This program performs transcation in you account

def bank_system(balance, transactions):
    deposits = 0
    withdrawals = 0
    for transaction in transactions:
        if transaction > 0:
            balance += transaction
            deposits += 1
        elif transaction < 0:
            if balance + transaction >= 0:
                balance += transaction
                withdrawals += 1
            else:
                print("Insufficient funds for withdrawal:", abs(transaction))
    return balance, deposits, withdrawals
balance = float(input("Enter starting balance: "))
while balance < 0:
    print("Invalid balance!")
    balance = float(input("Enter starting balance: "))
number_transactions = int(input("How many transactions do you want to make? "))
transactions = []
for x in range(number_transactions):
    transaction_number = x + 1
    amount = float(input(f"Enter transaction {transaction_number} (+deposit, -withdrawal): "))
    transactions.append(amount)
final_balance, deposits, withdrawals = bank_system(balance, transactions)
print("Final Balance:", final_balance)
print("Number of Deposits:", deposits)
print("Number of Withdrawals:", withdrawals)
    





        
