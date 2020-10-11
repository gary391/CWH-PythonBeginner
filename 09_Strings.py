mystr = "harry is a good boy"
print(len(mystr))
# print(mystr[0:78])

# Advance slicing
'''
[::]
First resolve the first colon i.e 
    Default value  - start with 0 and ends with the length of the string

Second resolve the second colon, i.e.very character by default  
    Default value - 1, which is pick 1 character starting from the first position
    Note: If we change it to 2, than it will select second character starting with first character in the string.   
    
    example" mystr[0:19:1] = mystr[::] = [:19:1] = [::1]


'''


# print(mystr[0::2]) # Every alternate character
# print(mystr[0::3]) # Skip two characters starting with the first characters.
# print(mystr[::5559]) # This will only match the first character.
# print(mystr[::-1]) # Reverses the string
# print(mystr[-1:-20:-1]) #

print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith('bdoy'))
print(mystr.count('o'))
print(mystr.find('is')) # prints the index where the specific letter is present in the string
print(mystr.capitalize())
print(mystr.replace('is', 'are'))
print(dir(mystr))