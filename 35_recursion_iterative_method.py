# recursion and iteration in python
# Write a program to calculate factorial of a number:

# Iterative approach
'''
n = 5
5 * 4 * 3 * 2 * 1
n! = n * n-1 * n-2 * n-3 ...* 1
n! = n * n-1!
'''
# def iterative_fact(a):
#     '''
#     :param a: Is a positive interger value
#     :return: Factorial of a
#     # >>> iterative_fact(5)
#     # >>> 120
#     '''
#     fact = 1
#     for i in range(a,0,-1):
#         # print(i)
#         fact = fact * i
#     return fact
#
# print(iterative_fact(5))

# Recursive approach
# def recursive_fact(a):
#     '''
#     :param a: Is a positive interger value
#     :return: Factorial of a
#     >>> recursive_fact(5)
#     120
#     '''
#     fact = 1
#     if a == 0 or a == 1:
#         return fact
#     else:
#         fact = a * recursive_fact(a-1)
#         return fact
#
# print(recursive_fact(4))

# Write a function to calculate nth number in a fibonacci series

'''
0 1 1 2 3 5 8 13 21

1. Starting element is Ist_ele 
2. Next element is 0 + 1 = IInd_ele
3. Third_ele = IInd_ele + Ist+ele

'''
def fibona(a):
    '''

    :param a: Is an positive interger value, which represents the index of the fibonacci series
    :return: Value at the particular index
    # >>> fibona(5)
    # 5
    # >>> fibona(6)
    # 8
    # >>> fibona(7)
    # 13
    # >>> fibona(8)
    # 21
    '''

    zero_element = 0
    first_element = 1
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        return 1
    else:
        return (fibona(a-1) + fibona(a-2))
print(fibona(5))


