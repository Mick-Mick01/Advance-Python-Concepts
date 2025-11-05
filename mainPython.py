#Everything is python is an object no matter what it is !!

# In C++, you control how data is passed:
    # Pass By value → a copy is made.
    # Pass By reference (using &) → no copy, just an alias.
    # Arrays decay into pointers, so they behave like references by default.

# In Python, it’s simpler but trickier to describe precisely:
    # Everything is an object, and variables are references to those objects.
    # When you pass something to a function, the reference is copied (so the function gets another reference to the same object).
    # If the object is mutable (like lists, dicts, NumPy arrays), modifications inside the function are visible outside.
    # If it’s immutable (like ints, strings, tuples), reassignments inside the function don’t affect the caller.

# So in short:
    # C++: You choose pass-by-value or pass-by-reference.
    # Python: Always passes object references, but the mutability of the object (variable, data str, object) determines whether changes persist.