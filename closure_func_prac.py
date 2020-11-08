# function returning function (closure) practice
# first class function

# Write a function that returns a x^y where y can be any positive integer value.

def to_power(y):  # This is the power which is 2 for square, 3 for cube etc.
    def calc_power(x):
        return x**y
    return calc_power

cube = to_power(3)
print(cube(2))

square = to_power(2)
print(square(3))