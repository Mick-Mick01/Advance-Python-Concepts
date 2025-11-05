'''
# *args and **kwargs
# Name does not matter just the starts matters

#  We use *args to take variable number of arguments in a function
#  *args is of type tuple
#  Print(type(args))

#  **KWARGS IS OF TYPE DICTIONARY
'''

'''
        *ARGS
'''
def specialFunction(*args):
    print(type(args))
    for values in args:
        print(values)

specialFunction("harry", 56, 9900, 99.007, "hello")
print('\n')
specialFunction(45, "Dev", "Mohan", 556.404, "humans")

'''
        **KWARGS
'''

def specialFunction2(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

Dict1 = { "name":"harry", "age":24 }
Dict2 = { "name":"Dev", "age":20 }

specialFunction2(**Dict1)
print('\n')
specialFunction2(**Dict2)

