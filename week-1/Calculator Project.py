Num1 = float(input("Please Enter the First Number: "))   
Operator = input("Enter the operator(+, -, *, /, %)\n-> ")
Num2 = float(input("Please Enter the Second Number: "))

if Operator == "+":
    print(round(Num1 + Num2, 2))
elif Operator == "-":
    print(round(Num1 - Num2, 2))
elif Operator == "*":
    print(round(Num1 * Num2, 2))
elif Operator == "/":
    print(round(Num1 / Num2, 2))
elif Operator == "%":
    print(round(Num1 % Num2, 2))
else:
    print(f"{Operator} is not a valid operator")
