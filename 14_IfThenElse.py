# : represents that you would like to enter in the if block.
# 4 space is default indentation

# var1 = 6
# var2 = 56
#
# var3 = int(input("Enter a number:"))
# if var3 > var2:
#     print("greater")
# elif var3 == var2:
#     print("equal")
# else:
#     print("lesser")
#
# print("I have reached at the end of the if block")

# list1 =[5,7,8,6]
# var = 6
# if var in list1:
#     print("Yes {} is in the list".format(var))

# list1 =[5,7,8,6]
# var = 15
# if var not in list1:
#     print("{} is not in the list".format(var))

# Write a program to identify if you can get a drives license or not

age = int(input("Please enter your age:"))
if age < 18:
    print("You are too young to drive!")
elif age == 18:
    print("Please come in for a practical exam!")
else:
    print("You can get a driver license!")