# Understanding parameter and argument in python: Both refer to the information passed into a function.
# A parameter is the variable listed inside the parentheses in the function definition.
# example - def average(num1, num2): where num1 and num2 are parameter that function average takes.
# An argument is the value that are sent to the function when it is called.
# Example - average(10,20), where value 10,20 are arguments

'''
What are decorators in python
- Function that modified the functionality of a function



link:
https://dbader.org/blog/python-first-class-functions
https://www.youtube.com/watch?v=7pgo4gV38fE&ab_channel=Harshitvashisth
https://www.youtube.com/watch?v=_zTyBMFD4yY
'''

# KEY POINTS:

## Function can be assigned to variable to make new functions.

# def func1():
#     print("This is me!")
'''
It takes the function object referenced by func1 and creates a second name 
pointing to it, func2. You could now also execute the same underlying function object by calling func2:
'''


# func2 = func1 # Here we assigned func1 to func2 to make new functions i.e. func2
# print(type(func2))
# del func1 # Even though we deleted the function func1 we have already assigned this to func2
# func2() # Because of the assignment operation we can call func2 to get the same answer as func1

## Function can return another function

# def funcret(num):
#     if num==0:
#         return print  # print is a built in function
#     if num ==1:
#         return sum  # sum is a built in function
# a = funcret(1)
# print(a) # Here 'a' returns print or sum which are built in functions.

## Function can be given to another function as an argument.


# def executor(func):
#     func("Hello world Here I am!")
#
# executor(print)

# -----------------DECORATORS---------------------#
# DECORATORS (funtion) are a way to enhance functionality of an other/existing function with re-reading it again.
# @ use of decorator
# Example: You have two function that work great, but now you would like to add warning message as well
# when these are executed

# NEW LINE: WARNING: This function only prints and doesn't return anything!

#  WARNING: This function only prints and doesn't return anything!
# def func1():
#     print("This is func1")
#
#
# # WARNING: This function only prints and doesn't return anything!
# def func2():
#     print("This is func2")


# func1()
# func2()

# def dectorator_function(any_function): # takes a function as an argument which will be modified
#     def wapper_function ():
#         print("WARNING: This function only prints and doesn't return anything!")
#         any_function()
#     return wapper_function

# print(type(dectorator_function(func1)))
# var = (dectorator_function(func1)) # this is how a function is being assigned to a variable var.
# var() # now var becomes a function and can be called as function var()

# func1 = (dectorator_function(func1))
# func1()

# ----------------Decorators USING @ SYMBOL-------------#

# @dectorator_function # shortcut
# def func1():
#     print("This is func1")
#
#
# @dectorator_function # shortcut
# def func2():
#     print("This is func2")
#
# func1()
# func2()

# ----------------Decorators Some Pit falls-------------#
from functools import wraps
def decorator_function(any_function):  # takes a function as an argument which will be modified
    @wraps(any_function)
    def wapper_function(*args, **kwargs):
        '''
        This is wrapper function
        '''
        print("WARNING: This function only prints and doesn't return anything!")
        return any_function(*args, **kwargs) # This should always return, if you don't write return it will not work for function returning values

    return wapper_function

@decorator_function
def func(a):
    print(f'This is func with argument {a}')

func(7)
@decorator_function
def add(a,b):
    '''
    This is an add function
    '''
    return a+b

print(add(2,3))

print(add.__doc__)
print(add.__name__)
