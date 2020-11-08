# Classes - Template
# Example of leave letter template, where you have to add details
# Object is instance of the class (letter obtained after entering the details in the leave letter template)
# DRY concept - Don't repeat yourself

class Student:
    pass

harry = Student() # These are two objects derived from this class
larry = Student()

harry.name = "Harry" # This is how we assign values to a instance variable (harry.name)
harry.section = 1
harry.std = 12

larry.name = "Larry" # This is how we assign values to a instance variable (harry.name)
larry.section = 2
larry.std = 9
larry.subjects =["english","hindi"]
# print(harry, larry)
print(harry.name, harry.std, harry.section)
print(larry.name, larry.std, larry.section, larry.subjects)