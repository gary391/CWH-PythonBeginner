# Practice decorator function
from functools import wraps
def print_function_data(func):
    @wraps (func)
    def warpper_func(*args, **kwargs):
        print("output")
        print(f'you are calling {func.__name__} function')
        print(f'{func.__doc__}')
        return func(*args, **kwargs)
    return warpper_func


# @print_function_data
# def add(a,b):
#     '''This function takes two numbers as argument and returns their sum'''
#     return a+b
# print(add(4,5))

@print_function_data
def subtract(a,b):
    '''This function takes two numbers as argument and returns their difference'''
    return a-b
print(subtract(5,1))



# output
# you are calling add function
# This function takes two numbers as parameter and return their sum
# 9