# python calculator

operator = input("Enter an operator(+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# print(num1 + num2)

if operator == "+":
   result = num1 + num2
   print(result)
elif operator == "-":
   result = num1 - num2
   print(result)
elif operator == "*":
   result = num1 * num2
   print(result)
elif operator == "/":
   result = num1 / num2
   print(round(result,2))
else:
   print(f"Incorrect Parameters")