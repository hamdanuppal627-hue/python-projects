status = input(" Are you a Member input Yes or No: " ).lower()
if status == "yes":
    amount = int(input("Enter you purchase amount: "))
    if amount >= 50:
        print("|You get a discount of 20%|")
    else: 
        print("|You get a discount of 10%|")
else:
    print("|No discount available. Join our membership for savings!|")