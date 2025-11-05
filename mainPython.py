'''
HOW TO PASS ALL THREE TYPES OF PARAMETERS IN A FUNCTION IN PYTHON
Always write normal parameters first(as keyword/positional arguments), then write *args & then write **kwargs. This order should be followed
'''

name = "Harry"

def myFunc(name, *args, **kwargs):
    print(name)
    
    for parameter in args:
        print(parameter)
    
    for key, value in kwargs.items():
        print(key,':', value)

myFunc("harry", *["hi", "oh"], **{"user_name":"dev", "age":20})
