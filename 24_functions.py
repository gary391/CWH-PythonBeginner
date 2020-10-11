# User defined function


def func2(a,b):
    """
    num, num -> num
    returns average of two numbers.
    >>> funcs(6,6)
    >>> 6.0
    """
    average = (a + b)/ 2
    return average


v = func2(6,6) # Here function returned a value which we assign it to v - variable
print(v)

print(func2.__doc__)