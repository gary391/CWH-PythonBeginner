# First class
# How to make your own class
# How to make your own object from this class
# What is init method

class Person:
    # This constructor method is called each time we make an object of the class
    # There we are defining the attribute for our object
    # self key word is convention, but you can write your own variable, in that case we will have replace self everywhere
    def __init__(self, first_name, last_name, roll_number):
        # instance variable
        print("Constructor get called!")
        self.fname = first_name  # fname is the instance variable
        self.lname = last_name  # lname is the instance variable
        self.rollnumber = roll_number

p1 = Person("harry", "jackson", 45000)
p2 = Person("Sumit", "Arora", 55000)
p3 = Person("Amit", "Arora",65000)
print(p3.fname)
# print(p2.lname)
# print(p2.rollnumber)
