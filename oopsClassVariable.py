# Class variable are also called class attributes
# Circle
# area
# circum

class Circle:
    # class variable
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def calc_circum(self):
        return (2*Circle.pi*self.radius)

c = Circle(4)
c1 = Circle(5)

print(c.calc_circum())


class Laptop:
    # Class variable, can be applied to all instances/objects
    discount_percent = 10
    def __init__(self, brand_name, model_number, price_value):
        print("Constructor called!")
        # instance variable (Note we can use existing attributes to create new instances as laptop_name)
        self.bname = brand_name
        self.model = model_number
        self.price = price_value
        self.laptop_name = brand_name +"-"+model_number

    def apply_discount(self):
        return ((self.price) * (100-Laptop.discount_percent)/100)

Laptop.discount_percent = 0
l1 = Laptop("Acer", "*uck_2000",500)
l2 = Laptop("Apple", "Mac2000", 1200)

print(l1.__dict__)