# function returning function

# def square (a):
#     return a ** 2

# def outer_func():
#     def inner_func():
#         print("Inside inner func")
#     return inner_func # the outer_func is returning inner_func
#
# var = outer_func() # Here we are assigning the outer_function to a variable.
# var() # Here we are calling the function/executing the function var
# print(type(var))

def outer_func2(msg):
    def inner_func2():
        print(f"message is {msg}")
    return inner_func2

# function is being assigned to a variable.
var2 = outer_func2("Hi there!")
# The variable has become a function and can be called as a regular function.
var2()
