def add(num1,num2):
    sum = num1 + num2
    return sum
def sub(num1,num2):
    minus = num1 - num2
    return minus
def mult(num1,num2):
    multiply = num1 * num2
    return multiply
def div(num1,num2):
    divide = num1/num2
    return divide

flag = True
while flag == True: 
      num1 = float(input("Enter your 1st Number: "))
      num2 = float(input("Enter your 2nd Number: "))
      print("\n1. Addition""\n2. Subtract""\n3. Multiply""\n4. Division")
      operation = int(input("Enter your operation(1-4): "))
      choice = [1,2,3,4]
      if operation not in choice:
         print("Invalid operation pick(1-4)")
      else:
        flag = False
if operation == 1:
   print(f"Addition of {num1} and {num2} is:",add(num1,num2))

elif operation == 2:
    print(f"Subtraction of {num1} and {num2} is:",sub(num1,num2))

elif operation == 3:
    print(f"Mutiplication of {num1} and {num2} is:",mult(num1,num2))

elif operation == 4:
    if num2 == 0:
        print("Invalid operation number cannot be divided by 0!")
    else:
        print(f"divison of {num1} and {num2}  is:",div(num1,num2))