# Dictionary
# Key value pair
# Keys will be always be an immutable
# value of dictionary can be a list or a dictionary.
# value of dictionary can be a list or a dictionary.
a = {'milk':1}
print(a)

d1 = {}
print(type(d1))

d2= {"Harry":"Burger", "Rohan":"Fish","SkillF":"Roti","Shubham":{"B":"Maggie", "L":"Roti","D":"Chicken"}}
# print(d2["Shubham"]["B"])

# How to add new value into the dictionary
d2["Ankit"] = "Junk Food"
d2["Veer"] = "yum yum rice"
# print(d2)

# How to remove elements from a dictionary
#
# del d2["Veer"]
# print(d2)

# Copy function

# d3 = d2
# del d3["Harry"]
# print(d2)  # Here even though we changed d3, elements in d2 got changed. In order to avoid this we should use copy fuction.
#
# d3 = d2.copy()
# del d3["Harry"]
# print(d2)
# print(d3)

# How to get a value in a dictionary
# print(d2.get("Harry"))

# How to update a dictionary
# d2.update({"leena":"Toffee"})
# print(d2)

# How to get the keys from a dictionary
# print(d2.keys())



# How to print all items in a dictionary
print((d2.items()))