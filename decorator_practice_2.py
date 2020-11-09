# Write a program to use decorators to create a sum of list of numbers, and return invalid argument
# if the number is not an integer.

from functools import wraps
def decorator_func(any_func):
    @wraps (any_func)
    def wrapper(*args, **kwargs):
        # '''
        # This is a function to get sum of intergers.
        # '''
        # print(f'This is a {add_all.__doc__} function')
        # data_types = []
        # for i in args:
        #     data_types.append(type(i) == int)
        # if all(data_types):
        #     return any_func(*args, **kwargs)
        # else:
        #     return (f'Invalid argument') # In case of invalid argument, it returns this statement

        # Using list comprehension

        if all ([type(arg)== int for arg in args]):
            return any_func (*args, **kwargs)
        else:
            return (f'Invalid argument')
    return wrapper


@decorator_func
def add_all(*args):
    '''Add'''
    total = 0
    for i in args:
        # total = total + i
        total += i
    return total

print(add_all (1,2,3,4, {"gaurav":"The programmer"}))