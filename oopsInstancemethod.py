# instance method
# instance and object are same
# All functions defined inside a class are called method
# instance variable is unique for each object
class Person:

    def __init__(self, first_name, last_name, age):
        self.fname = first_name
        self.lname = last_name
        self.age = age

    def full_name(self):
        return f'{self.fname} {self.lname}'

    def is_above_18(self):
        return self.age > 18

p1 = Person("Harry", "Jackson", 10)
p2 = Person("Larry", "Jacklin", 35)
# print(p2.full_name()) # Here we will have to call the funtion using ()
# print(Person.full_name(p1))
# print(p1.is_above_18())
print(Person.is_above_18(p1))


# l1 = [1,2,3,4]
# clear, pop
# print(l1)
# l1.clear()
# print(l1)

## This is how python uses instance method for a class
# list.clear(l1)
# print(l1)
