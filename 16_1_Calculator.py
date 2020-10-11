# Write a program to create a basic calculator that perform operations on user inputed numbers
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
oper = input("What operation would you like on these numbers +,-, *, / ?")

if oper == '+':
    ans = int(num1 + num2)
elif  oper == '*':
    ans = int(num1 * num2)
elif  oper == '-':
    ans = int(num1 - num2)
else:
    ans = int(num1 / num2)

print(ans)