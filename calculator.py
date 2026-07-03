num_1 = int(input("Enter your 1st number: "))
num_2 = int(input("Enter your 2nd number: "))

print("|For addition type 1|")
print("|For subtraction type 2|")
print("|For division type 3|")
print("|For multiplication type 4|")

choice = int(input("Enter your choice: "))

if choice == 1:
    add = num_1 + num_2
    print("Answer =", add)

elif choice == 2:
    sub = num_1 - num_2
    print("Answer =", sub)

elif choice == 3:
    if num_2 != 0:
        div = num_1 / num_2
        print("Answer =", div)
    else:
        print("Error: Cannot divide by zero.")

elif choice == 4:
    mult = num_1 * num_2
    print("Answer =", mult)

else:
    print("Invalid choice!")