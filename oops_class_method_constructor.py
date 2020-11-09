# Class Method as constructor
# For creating an object, we call the constructor
# For creating an object, using a custom constructor which can take string as in input - We use class method


class Person:
    count_instance = 0 # class variable/class attribute
    def __init__(self, first_name, last_name, age):
        Person.count_instance = Person.count_instance + 1
        self.fname = first_name
        self.lname = last_name
        self.age = age

    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(',')
        # create an object
        return cls(first, last, int(age))


    @classmethod
    def count_instances(cls):
        return f'You have created {cls.count_instance} instances of {cls.__name__} class'

    # Instance method, self represents object
    def full_name(self):
        return f'{self.fname} {self.lname}'

    def is_above_18(self):
        return self.age > 18



p1 = Person("Harry", "Jackson", 10)
p2 = Person("Larry", "Jacklin", 35)
p3 = Person("Tom", "Jerry", 55)
p4 = Person.from_string("Tom,Jerry,55")
print(p4.is_above_18())
print(p4.full_name())

# Class method
#"You have created 4 instances of person class"
# print(Person.count_instances())

# Here p1 will also work, since python will search this in instance method first and then search in class method
# print(p1.count_instances())