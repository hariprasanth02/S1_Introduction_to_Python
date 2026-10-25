a= float(input("Enter value of a: "))
b= float(input("Enter value of b: "))
op = input("operator(+,-,*,/,%,//,**: )")

if op == "+" :
    result = a + b

elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        result=("Error:division by zero")
    else:
        result = a / b
elif op == "%":
    result =  a % b
elif op == " // ":
    result = a // b
elif op == "**":
    result = a ** b

else:
    print("operator is not defined")

print(f"{a} {op} {b} = {result}")