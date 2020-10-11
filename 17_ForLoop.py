list1 = [["gaurav",1],["veer",2],["deepali",4],["minku",5],["renu",7]]

# This is how you unpack a list

# dict1 = dict(list1)
# print(dict1)
# for item, rank in list1:
#     print(item, "has this rank in world of warcrafts!", rank)

# for item, rank in dict1.items():
#     print(item, rank)
    # print(item, "has this rank in world of warcrafts!", rank)

# for item in dict1:
#     print(item)

# Write a program to only print numbers greater than 6 from a list
items = [int, float, "Gary", 4, 5, 7, 89, 90, 120, 1,2,3,4,6]
for i in items:
    if str(i).isnumeric() and i > 6:
        print(i)