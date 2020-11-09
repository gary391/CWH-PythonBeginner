# How to count/print the number of instance being created

class Person:
    count_instance = 0
    def __init__(self):
        # Calling the class variable is using class.<variable_name>
        Person.count_instance = Person.count_instance + 1
        print("Constructor called!")



p1 = Person()
p1 = Person()
p1 = Person()
print(Person.count_instance)