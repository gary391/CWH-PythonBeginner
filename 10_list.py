# List

grocery = ["harpic", "atta", "dal", "rice", "fruits", "veggies", "maggi", 56]
# print(grocery)

numbers = [1,2,3,4,54,5,6]
# print(len(numbers))
# numbers.sort() # This will modify the original list
# numbers.reverse() This will modify the original list
# print(numbers.sort()) # number.sort() return none type but will do an in place action, so when we print (numbers.sort()) we get none


# List indexing and slicing
# print(numbers[:5]) # This is a new list
# print(numbers) # This is the original list

# Extended slice

print(numbers[::])
# print(numbers[::1]) Default value for steps is 1, recommended to keep -1 or positive values for steps
print(numbers[::2]) # this will skip one element
print(numbers[::3]) # this will skip two elements

# Adding elements in a list at the end
numbers.append(11)
numbers.append(21)
numbers.append(31)
print(numbers)


# Insert function inserts elements in a list at a specific index

numbers.insert(1,67)
print(numbers)

# Remove function removes elements from the list

numbers.remove(67)
print(numbers)

# pop function, removes last element in a list

numbers.pop()
print(numbers)