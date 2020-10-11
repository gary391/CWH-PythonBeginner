# Write a program to guess a number using binary search ?

# no of guesses 9
# print no of guesses left
# no of guesses he took to finish
# gameover!

no_of_guess = 9
num = 18
count = 0
while (no_of_guess) > 0:
    if (no_of_guess == 1):
        print("\nThis is your last guess, guess wisely!")
    print("You have {} guesses remaining\n". format(no_of_guess))
    count = count + 1
    inpt = int(input("Guess a number: "))
    if(no_of_guess == 1) and (inpt > num):
        print("GameOver!")
        break
    elif (inpt > num):
        print("You have entered a bigger number, guess a smaller number\n")
    elif(no_of_guess == 1) and (inpt < num):
        print("GameOver!")
        break
    elif inpt < num:
        print("You have entered a smaller number, guess a larger number\n")
    else:
        print("Bingo! You guessed the exact number in {} guesses".format(count))
        break
    no_of_guess = no_of_guess - 1