# *args and **kwargs
# Name does not matter just the starts matters

#  We use *args to take variable number of arguments in a function
#  *args is of type tuple
#  Print(type(args))

def specialFunction(*args):
    for values in args:
        print(values)

specialFunction("harry", 56, 9900, 99.007, "hello")
print('\n')
specialFunction(45, "Dev", "Mohan", 556.404, "humans")

#NOW WE'LL START ABOUT **KWARGS