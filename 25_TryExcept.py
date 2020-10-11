num1 = input ("Enter first number:")
num2 = input ("Enter second number:")
try:
    print(int(num1)+int(num2))
except Exception as e:
    print(e)
print("This line is very important")


