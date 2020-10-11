# Excercise 2 - Faulty Calculator
# 45 *3 = 555, 56+9 = 77, 56/6 = 4

oper = input("What operation would you like on these numbers +,-, *, / ?\n")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))


if oper == '*':
    if (num1 == 43) and (num2 == 3):
        ans = int(555)
    else:
        ans = int(num1 * num2)
elif oper == '+':
    if num1 == 56 and num2 == 9:
        ans = int(77)
    else:
        ans = int(num1 + num2)
elif oper == '/':
    if num1 == 56 and num2 == 6:
        ans = int(4)
    else:
        ans = int(num1 / num2)
else:
    ans = int(num1 - num2)

print(ans)