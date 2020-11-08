##############################################
#------------------------MAP-----------------#
##############################################
'''

"A map function executes certain instructions or functionality provided to it on every item of an iterable."

A map function takes two parameters:

- First one is the function through which we want to pass the items/values of the iterable
- The second one is the iterable itself

The iterable could be a list, tuple, set, etc. It is worth noting that the output in the case of the map is also an
iterable i.e., a list
'''

# If you are using Map, and want to return a list, then use list(map

# How can you type cast a list of elements ?
# numbers = ["3", "343", "23"]

# Using for loop
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# Using map function

#map(int, numbers) # this returns an object.
# numbers = list(map(int, numbers))
#
#
# numbers[1] = numbers[1] - 300
# print(numbers[1])

# How to square elements of a list using lambda & map function
# num = [1,2,3,4,5,6,7,8,9]
# square = list(map(sq, num)) # Here sq can be function defined separately
# square = list(map(lambda x:x*x, num))
# print(square)

# Write a program to create a list of lists that contains sqaure and cube of numbers using map

#1. Square function
# def sq(a):
#     return a*a
# #2. Cube Function
# def cube(a):
#     return a*a*a
# #3. List
# func1 = [sq, cube]
#
# for i in range(5):
#     val = list(map(lambda x:x(i), func1 ))
#     print(val)


#--------------------FILTER------------------#

# Filter function

# A filter function in Python tests a specific user-defined condition for a function and returns an iterable for the
# elements and values that satisfy the condition or, in other words, return true.
# Ex:It can help create a list from an existing list that contains items that returns a true value for a given condition

'''
It also takes two parameters:

- First one is the function for which the condition should satisfy
- The second one is the iterable
'''

# list1 = [1,2,3,4,5,6,76,7,8,9]
#
# def is_greater_5(num):
#     return num > 5 # returns true or false if the number is greater than 5
#
# gr_than_5 = list(filter(is_greater_5, list1)) # Here type casting this to list is important
# print(gr_than_5)

#--------------------REDUCE-------------------#
# Reduce is part of functools module
# As the name suggest, it reduces a give list sums up all elements in the list.
# It accepts an iterator to process, but it is not an iterator itself. It returns a single result.

from functools import reduce

list1 = [1,2,3,4]

# Using for loop produce the sum of all elements in the list.

# num = 0
# for i in list1:
#     num = num + i
# print(num)

# using reduce function
print(reduce(lambda x,y:x+y, list1))
# num = reduce(lambda x,y:x+y, list1)
# print(num)

