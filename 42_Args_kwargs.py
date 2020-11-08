# What are args and kwargs in python and how can we use them ?

#args

# def function_name_print (a, b, c, d, e):
#     print(a,d,c,d,e)
 # If we add another argument, it will throw an error as function only takes 4 argument

def funargs(normal, *args, **kwargs):
    # Convention always write/pass normal parameter/argument, *args, and then **kwargs in this sequence!!!!
    # args and kwags are optional
    # The arguments are always passed as a tuple in the function in case of *args
    # print(type(args))
    # print(args[0])
    # print(normal)
    # for item in args:
    #     print(item)
    for key, value in kwargs.items():
        print(f'{key} is {value} of the class')

# function_name_print("harry", "skillf", "hammad", "rohan", "ravi")

var1 = ["harry", "skillf", "hammad", "rohan", "ravi", "The programmer"]
var = "I am a normal argument"

kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor","The programer":"Coordinator"}

funargs(var, *var1, **kw) # * & ** are important here


#kwargs