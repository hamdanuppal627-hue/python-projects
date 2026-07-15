print("Welcome to Apex crest Bank")
user_input = input("Do you Want to Take a Loan?: ").lower()
if user_input == "yes":
    print("\nWe provide Studying Loan, for Buying properties, and personal Loans")
    reason = ["studying", "personal", "properties"]
    why = input("Why do you want to take a Loan?: ").lower()   
    if why not in reason:
        print("Sorry we don't provide loan for", why)
    elif why == "studying":
        amount_studying = int(input("For How much amount do you want to take the Loan for?: "))
        if amount_studying > 10000:
            print("An interest of 10% will be applied annually")
            time_studying = int(input("For how much time do you want to take the loan for in year?: "))
            if time_studying > 20:
                print("We only provide Loan payment time of 20 years")
            else:
                total_rate = time_studying * 0.10
                total_amount_studying = total_rate * amount_studying
                final_amount_studying = total_amount_studying + amount_studying
                print("Total Amount to Repay:", final_amount_studying)
        else:
            print("An interest of 5% will be applied annually")
            time_studying_less = int(input("For how much time do you want to take the loan for in years?: "))
            if time_studying_less > 20:
                print("We only provide loan payment times up to 20 years")
            else:
                total_rate_less = time_studying_less * 0.05
                total_amount_studying = total_rate_less * amount_studying
                final_amount_studying_less = total_amount_studying + amount_studying
                print("Total Amount to Repay:", final_amount_studying_less)
    elif why == "properties":
        amount_properties = int(input("For How much amount do you want to take the Property Loan for?: "))  
        if amount_properties > 200000:
            print("An interest of 20% will be applied annually")
            time_properties = int(input("For how much time do you want to take the loan for in years?: "))
            if time_properties > 20:
                print("We only provide loan payment times up to 20 years")
            else:
                total_rate = time_properties * 0.20
                total_amount_properties = total_rate * amount_properties
                final_amount_properties = total_amount_properties + amount_properties
                print("Total Amount to Repay:", final_amount_properties)
        else:
            print("An interest of 10% will be applied annually")
            time_properties_less = int(input("For how much time do you want to take the loan for in years?: "))
            if time_properties_less > 20:
                print("We only provide loan payment times up to 20 years")
            else:
                total_rate_less = time_properties_less * 0.10
                total_amount_properties = total_rate_less * amount_properties
                final_amount_properties_less = total_amount_properties + amount_properties
                print("Total Amount to Repay:", final_amount_properties_less)
    elif why == "personal":
        personal_purpose = input("What is the purpose of this personal loan? (e.g., medical, travel, wedding): ")
        amount_personal = int(input("For How much amount do you want to take the Personal Loan for?: "))
        if amount_personal > 30000:
            print("An interest of 20% will be applied annually")
            time_personal = int(input("For how much time do you want to take the loan for in years?: "))
            if time_personal > 20:
                print("We only provide loan payment times up to 20 years")
            else:
                total_rate = time_personal * 0.20
                total_amount_personal = total_rate * amount_personal
                final_amount_personal = total_amount_personal + amount_personal
                print("Total Amount to Repay:", final_amount_personal)    
        else:
            print("An interest of 15% will be applied annually")
            time_personal_less = int(input("For how much time do you want to take the loan for in years?: "))
            if time_personal_less > 20:
                print("We only provide loan payment times up to 20 years")
            else:
                total_rate_less = time_personal_less * 0.15
                total_amount_personal = total_rate_less * amount_personal
                final_amount_personal_less = total_amount_personal + amount_personal
                print("Total Amount to Repay:", final_amount_personal_less)
else:
    print("We are available 24/7 for any loan services")
