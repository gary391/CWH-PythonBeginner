# write a program to type numbers starting from 5 till 44

# i = 0 # initialize the value of i
# while (True):
#     if i + 1 < 5: #This condition will be true when i = 4
#         i = i + 1
#         continue # This will iterate till the condition is false, there by skipping 1-4 numbers
#     print(i + 1, end=" ")
#     if i == 44:
#         break # This will break the if condition.
#     i = i + 1

# Write a program that takes input from the user till the entered number is greater than 100.


while True:
    num = int(input("Enter a number: "))
    if num >= 100:
        break
    else:
        print("Please try one more type!")
print("Congratulations you have successfully guessed a number greater than or equal to 100!")