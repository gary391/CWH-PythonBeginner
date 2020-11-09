# Classes - Template
# Objects are derived from the class/template
# Example of leave letter template, where you have to add details
# Object is instance of the class (letter obtained after entering the details in the leave letter template)
# DRY concept - Don't repeat yourself
# Restrict access for some function

class Student:
    pass

harry = Student() # These are two objects derived from this class
larry = Student()

# print(harry, larry)

# Instance variable - Adding variable for harry and larry
harry.name = "Harry" # This is how we assign values to a instance variable (harry.name)
harry.section = 1
harry.std = 12

larry.name = "Larry" # This is how we assign values to a instance variable (harry.name)
larry.section = 2
larry.std = 9
larry.subjects =["english","physics"]

print(harry.name, harry.std, harry.section)
print(larry.name, larry.std, larry.section, larry.subjects)