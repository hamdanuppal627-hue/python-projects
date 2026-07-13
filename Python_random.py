# Even/odd checker

number = int(input("Enter a number: "))
if number % 2 == 0 :
    print("Your number is Even")
else:
    print("Your number is Odd")

#Grade calculator
score = int(input("Enter your marks between(0-100): "))
if score >= 90 and score <= 100:
    print("Your Grade is A")
elif score >=80 and score <=89:
    print("Your Grade is B")
elif score >= 70 and score <= 79:
    print("Your Grade is C")
elif score >= 60 and score <= 69:
    print("Your Grade is D")
elif score > 0 and score < 60:
    print("You failed!")
else:
    score < 0 or score > 100
    print("Invalid Score!")

#Calculator
Num1 = int(input("Enter your 1st Number: "))
Num2 = int(input("Enter your 2nd Number: "))
print("+, -, *, /")
operations = input("Which operation would you like to carry out?")
match operations:
    case "+":
        print(Num1 +  Num2)
    case "-":
        print(Num1 - Num2)
    case "*":
        print(Num1 * Num2)
    case "/":
        if Num2 != 0:
            print(Num1 / Num2)
        else:
            print("Number cannot be divided by 0")
    case _:
        print("Invalid Operation!!")

#while loop counting
total = 0
while total < 10:
    total +=1
    if total % 3 == 0:
        continue
    print(total)

# Triangle
n = int(input("Enter the dimension of the triangle: "))
for x in range(1, n+1):
    for j in range(1,n+1):
        if j <= n-x :
         print(" ", end = " ")
        else:
         print("*", end = " ")
    print()

#List
list =[]
for x in range(6):
    Num = int(input("Enter Your number: "))
    list.append(Num)
print(list)
print(list[0])
print(list[5])
total = 0
sum = 0
for x in range(6):
    total = list[x]
    sum = sum + total
print(sum)