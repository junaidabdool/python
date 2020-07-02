num1 = float(input("Enter num1 please :\n"))
op = input("Enter the Operation :\n")
num2 = float(input("Enter num2 please :\n"))

if op == "+":
     print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("ERROR PLEASE ENTER A PROPER OPERATION")