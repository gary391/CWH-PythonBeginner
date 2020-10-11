# This is program is to write a snake, water & gun Game.
'''
Rules:
1. number of attempts = 10
    Winning logic:
        a. snake or water winner is snake
        b. snake or gun winner is gun
        c. gun or water winner is water
2. Manitain scores
3. Using While loop
4. First Input is from the user
5. Use random choice function from the random module.

'''
import random
lst = ['snake', 'water', 'gun']
computer_score = 0
user_score = 0
attempt = 0
while attempt <= 10:
    user_input = input("Enter snake, water and gun: ")
    choice = random.choice(lst)
    if ((user_input == 'snake') and (choice == 'water')):
        print(f"Computer entered - {choice}")
        user_score = user_score + 1
        print(f'Current Score computer:{computer_score}  and user:{user_score}')
    elif ((user_input == 'snake') and (choice == 'gun')):
        print(f"Computer entered - {choice}")
        computer_score = computer_score + 1
        print(f'Current Score computer:{computer_score} and user:{user_score}')
    elif ((user_input == 'gun') and (choice == 'snake')):
        print(f"Computer entered - {choice}")
        user_score = user_score + 1
        print(f'Current Score computer:{computer_score} and user:{user_score}')
    elif ((user_input == 'gun') and (choice == 'water')):
        print(f"Computer entered - {choice}")
        computer_score = computer_score + 1
        print(f'Current Score computer:{computer_score} and user:{user_score}')
    elif ((user_input == 'water') and (choice == 'gun')):
        print(f"Computer entered - {choice}")
        user_score = user_score + 1
        print(f'Current Score computer:{computer_score} and user:{user_score}')
    elif ((user_input == 'water') and (choice == 'snake')):
        print(f"Computer entered - {choice}")
        computer_score = computer_score + 1
        print(f'Current Score computer:{computer_score} and user:{user_score}')
    else:
        print(f"Computer entered - {choice}")
        print("you both entered the same option existing!\n")
        print(f'The Final Score is  - computer:{computer_score} and user:{user_score}')
        break
    attempt = attempt + 1
# else:
#     print("Game Over!")
if computer_score > user_score:
    print('\nThe Winner is Might Computer!')
elif computer_score < user_score:
    print('You are a lucky User!')
else:
    print(f"This is a Draw!")





