# set - A set is a collection of well-defined objects and non-repetitive elements that is - a set with 1,2,3,4,3,4,5,2, 2, and 3 as its elements can be written as {1,2,3,4,5}
#
# No repetition of elements is allowed in sets.

# “A set is a data structure, having unordered, unique, and unindexed elements.”

'''
Sets are iterable(iterations can be performed using loops)
They are mutable (can be updated by adding or removing entries)
There is no duplication (two same entries do not occur)
'''

# Restriction

'''
Once a set is created, you can not change any of its items, although you can add new items or remove previous but 
updating an already existing item is not possible. There is no indexing in sets, so accessing an item in order or 
through a key is not possible, although we can ask the program if the specific keyword we are looking
for is present in the set by using “in” keyword or by looping through the set by using a for loop(we 
will cover for loops in tutorial # 16 and 17)

'''

s = set ()
s1 = {1,2,3,4,}
# print(s1)
# print(type(s1))
# s2 = [1,2,3,43,45,1,2,3]
# s3 =set(s2)
# print(s3)
# s3.add(11)
# s3.remove(43)
#
# print(s3)
#
# a = [1,2,3,4,5]
# b = [2,34,53,3,1,5,11]
# c = a + b
# print (set(c))

s4 = s1.intersection({1,2,3,5}) # This creates a intersection of s1 and {1,2,3,5}
print(s4)