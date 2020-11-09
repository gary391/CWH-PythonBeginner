# What is instance variable and class variable ?
# instance variable is property of the object
# You can't change class variable from the instances. 
class Employee: # Name of the class should start with a captial letter.
    no_of_leaves = 8 # this is common to all the objects of this class. Class variable!
    pass

# harry/larry is derived from the class and its object, it should have variables from the class
harry = Employee()
larry = Employee()

# These are variables for these instances/object and not related to the class
harry.name = "Harry"
harry.salary = 4500
harry.role = "student"
larry.name = "Larry"
larry.salary = 8500
larry.role = "instructor"

print(harry.salary)
# Here we are accessing a class variable using an object derived from the class.
# print(harry.no_of_leaves)
# print(larry.no_of_leaves)
# print(Employee.no_of_leaves) # Accessing via class itself
Employee.no_of_leaves = 9
# print(harry.__dict__)
harry.no_of_leaves = 7  # This creates a instance variable of harry object.
# print(harry.__dict__)
print(Employee.no_of_leaves) # Accessing via class itself
print(harry.no_of_leaves)

