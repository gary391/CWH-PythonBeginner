# First class function or closures

def square(a):
    return a**2

# Here we are assigning as function to a variable.
print(square) # prints the memory location of the function
s = square  # Here we are mapping the memory location of square to a variable s
print(s)  # prints the memory location of the variable s
s = square(5) # Here we are calling the function s
print(s)

# Now we can use the variable just like a function.  
# Note even if we delete the original function.
# print(s(3))
# print(s.__name__)
# print(square.__name__)
#
# # Here s and square are pointing to the same memory location
# print(s)
# print(square)