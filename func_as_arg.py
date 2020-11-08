# Function that take another function as an argument

# map function

def square(a):
    return a**2

l = [1,2,3,4]

# Here map function takes the first argument as another function
# print(list(map(square, l)))
# Using map function returns a map object.

# print(list(map(lambda a: a**2, l)))

# Defining a regular function to get the map functionality
#
def my_map(func, l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list
#
# print(my_map(square, l))

# Using Lambda function, we are creating the function of square and passing it to th my_map function as an argument
# print(my_map(lambda a: a**2, l))

# Using list comprehension, the function returns a iterable after applying function.

# def my_map_2(func, l):
#     return [func(item) for item in l]
#
# print(my_map_2(square, l))