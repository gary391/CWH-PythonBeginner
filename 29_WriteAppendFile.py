# How to write and append in a file.
# write function - For the first attempt, it will create a file.
# # After that, write function will overwrite over what is there in the file.
# f = open("gary.txt", "wt") # here f is the file handle
# # f.write("Hello world here I am! now111\n")
#
# # Number of characters written in a file. (f.write function)
# a = f.write("Hello world here I am! now\n")
# print(a)

# Handles read and write both at the same time, using r+
# Here the write is actually appending to the file.y
f = open("gary.txt", "r+")
print(f.read())
# content = f.read()
# print(content)
f.write('Thanks!\n')



f.close()