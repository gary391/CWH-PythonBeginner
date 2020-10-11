# What is seek and tell function in python ?
# Tell function identifies the present location of the file handle
# seek function takes you to that location.
f = open ("gary.txt")
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(10)  # Takes the file handle to the specific location mentioned in the parameter.
print(f.readline()) # This readline will start reading the file from the location of the file handle. which is 10 in this case 
print(f.tell()) # Presents the current location of the file handle.

f.close()