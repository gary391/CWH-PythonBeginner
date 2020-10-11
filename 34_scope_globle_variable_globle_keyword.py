# What is scope, global variable, global keyword in python ?
# l = 10 # Global variable all function with in this program can use this variable
# def func1(a):
#     # l = 5 # local
#     global l # Using a global keyword we can use global variable inside local scope and modify it.
#     l = l + 45
#     m = 10 # local
#     print(l, m) # First check in local scope, than check in the global scope
#     print(a, "this is me!")
#
# print(func1("gary"))
# print(l) # which is only checking for the global scope value, which has now been updated.

# If you have a variable defined with in a function, first it will check for the local scope i.e. with in the function it self
# if it doesn't find it there it will search in the global scope.

# How can I change the value of the global variable ?

def gary():
    x = 20
    def rohan():
        global x # Variable in the global scope
        x = 88 # This will update the value of x
    print("Before calling rohan()", x)
    rohan()
    print("After calling rohan()", x)

gary()
print(x)