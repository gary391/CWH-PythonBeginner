# create a laptop class with attributes like brand name, model name and price
# create two object/instance of your laptop class
# Discount method
class Laptop:

    def __init__(self, brand_name, model_number, price_value):
        print("Constructor called!")
        # instance variable (Note we can use existing attributes to create new instances as laptop_name)
        self.bname = brand_name
        self.model = model_number
        self.price = price_value
        self.laptop_name = brand_name +"-"+model_number

    def apply_discount(self, value):
        return ((self.price) * (100-value)/100)

l1 = Laptop("Acer", "*uck_2000",500)
l2 = Laptop("Apple", "Mac2000", 1200)
print(l2.apply_discount(10))