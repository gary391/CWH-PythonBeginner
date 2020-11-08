# decorator with arguments - Helps solve the problem of write separate decorators for different
# data types

from functools import wraps

def only_data_type_allow(data_type):
    def decorator_func(any_func):
        @wraps(any_func)
        def wrapper(*args, **kwargs):
            # Using list comprehension
            if all([type(arg) == data_type for arg in args]):
                return any_func(*args, **kwargs)
            else:
                return (f'Invalid argument')
        return wrapper
    return decorator_func

# @only_data_type_allow(int)
# def add_all(*args):
#     '''Add'''
#     total = 0
#     for i in args:
#         # total = total + i
#         total += i
#     return total
#
# print(add_all (1,2,3,4, "gaurav"))

@only_data_type_allow(str)
def string_join(*args):
    string = ''
    for char in args:
        string += char
    return string

print(string_join('gaurav', "yadav", 'a', 1))