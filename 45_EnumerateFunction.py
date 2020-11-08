# Enumerate function in python - Provides index and value at the same time for iterables
# Indexing starts from 0

lst1 = ["Bindi", "Chopstick", "Milk", "Bread", "Eggs", "Sugar"]

# How to select alternate items in the list starting with the first element using regular for loop. ?
# for i in range(len(lst1)):
#     print(i)
#     if (i%2) == 0:
#         print(lst1[i])

# How to select alternate items in the list starting with the first element using enumerate function. ?

for index, value in enumerate(lst1):
    # print(index, value)
    if index %2 ==0: # Here we don't have to identify the specific values in the list as in rgular for loop i.e. lst1[i]
        # print(f"Alexa please bring {value} with you on your way back to home!")
        print(f"ALex please bring item {index}, i.e. {value} from the list")
