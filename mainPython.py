'''
My Ques: Just like we know everything in python is an object like the variables, data structures, etc. Is this the same for other OOP languages like in C++ ?
'''

# In Python, everything truly is an object: numbers, functions, classes, even modules. Every variable is just a reference to an object on the heap. There’s no distinction between “primitive” and “object” types.

# In C++ and most other statically typed OOP languages, things are more divided:
    # Primitive types (int, char, double, bool, etc.) are not objects. They live on the stack, and you can’t call methods on them.
    # Objects (instances of class or struct) live in memory you manage — on the stack or heap — and they can have methods, constructors, destructors, etc.
    # References and pointers are ways to refer to objects, and are not objects themselves.

# So, while Python treats everything uniformly as an object reference, C++ draws a hard line between:
    # Values (raw data, like int x = 5;)
    # Objects (instances of classes)
    # References/pointers (aliases to those values or objects)

# You could say:
    # Python is “object-all-the-way-down.”
    # C++ is “object-oriented, but not object-everything.”