# What are class methods?

class Employee:
    no_of_leaves = 8 # class variable

    # Class ke argument ko __init__ function will handle
    # Constructor, here self is the object of the class that is getting built (woo object jis ke baat ke ja rahi hai)
    def __init__(self, aname, asalary, arole):
        self.name = aname # name is instance variable, where as the aname is the argument
        self.salary = asalary
        self.role = arole

    # Method
    # What is self ?, woo object jis ke baat ke ja rahi hai
    def printdetails(self):
        return (f'Name is {self.name}. Salary is {self.salary} and the role is {self.role}')

    # Class method
    # Function to change the class variable without setting it.
    # Also, all methods in the class will automatically take the first argument as self which will pass the object
    # of the class into method

    @classmethod
    # here cls is that class whose instance is that object
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves




harry = Employee("Harry", 4500, "student") # object of the Employee class, these arguments are going to __init__ func
harry = Employee("Harry", 8000, "Monitor")

print(harry.__dict__)
harry.no_of_leaves = 34 #
print(harry.no_of_leaves)
print(harry.__dict__)
print(Employee.no_of_leaves)