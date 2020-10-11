# What are lambda functions in python ?
#
# def minus(a,b):
#     return a-b
# print(minus(9,5))

# minus = lambda x, y: x - y
# print(minus(10,8))

# How is sort function used with lambda function ?

# Using a regular function
# def first_element(a):
#     '''
#     :param a: List
#     :return: First element of a list
#     '''
#     return a[1]
#
# a = [[23,12], [221,11], [212,43], [1,22],[2,24]]
# a.sort(key=first_element)
# # print(a.sort())
# print(a)

# Using lambda function:

a = [[23,12], [221,11], [212,43], [1,22], [2,24]]
a.sort(key=lambda x: x[0])
# print(a.sort())
print(a)