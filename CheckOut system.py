total = 0
def shopping(total):
    for x in range(items):
        count = x + 1
        price = float(input(f"Enter the price of item {count}: "))
        total += price
    coupon = input("Do you have a coupon? (yes/no): ").lower()
    discount = 0
    tax = 0
    if coupon == "yes":
        rate_coupon = float(input("Enter the discount percentage: "))
        discount = total * rate_coupon / 100
    if total > 5000:
        print(f"Since your total is {total}, a 5% tax has been applied.")
        tax = total * 5 / 100
    final_amount = total - discount + tax
    print("\n---------------------------")
    print(f"Customer:{name}")
    print(f"Subtotal: {total}")
    if discount > 0:
        print(f"Discount: {discount}")
    else:
        print("Discount: None")
    if tax > 0:
        print(f"Tax: {tax}")
    else:
        print("Tax      : None")
    print(f"Final Bill: {final_amount}")
    print("---------------------------")
name = input("Enter your name: ")
items = int(input("Enter the number of items you are buying: "))
shopping(total)