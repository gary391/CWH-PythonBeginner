# Pattern printing problem
'''
Input Integer = n - Number of rows for the pattern.
Boolean - True or False

For Boolean = True
*
* *
* * *
* * * *

For Boolean = False

* * * *
* * *
* *
*

'''

rows = int(input("Enter the number of rows for the pattern:"))
while True:
    r_bool = (input("Preference: Type true for Pyramid style or false for inverted pyramid style pattern"))
    if r_bool.capitalize() == "True" or r_bool.capitalize() == "False":
        if r_bool.capitalize() == "True":
            for r in range(rows+1):
                print('* ' * r)
            break

        elif r_bool.capitalize() == "False":
            for r in range(rows,0,-1):
                print('* ' * r)
            break
    else:
        print("\nPlease re-enter your preference again!. Note it should be either true or false\n")
