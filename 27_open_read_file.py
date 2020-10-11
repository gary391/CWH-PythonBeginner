f = open("gary.txt", 'rt') # open return a file handle which is a text IO Wrapper.
print(type(f))
# content = f.read() # This will read the entire file in one go, so if you have read statement at the start of the
                     # program, and then you have other statements related to reading the file, then those will not work.

# print(type(content))
# content = f.read(1000)
# print("1", content)
# content = f.read(3)
# print("2", content)

# for line in content: # Here content is string, therefore it will print the character in the string.
#     print(line)

# Reading line by line using for loop
# for line in f: # f is the file handle
#     print(line, end="")

# # realine function
# print(f.readline(), end="")
# print(f.readline(), end="")

# Readlines functions - This will print the content of the file in a list.
print(f.readlines())

f.close() # Always close the file if you open a file.