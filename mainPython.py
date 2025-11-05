# List and array stores same type of datatype
# Tuple stores any type of data into it. Multiple data type in one tuple
# We use array to store data in a contiguous manner and time complexity to find data in any index is O(1)
# When we use a list it stores data in a non-contiguous manner and time complexity to find data in any index is O(n) cause the list have to traverse through every index to find the memory address of next index. Every index in a list stores the memory address of element before and after that index.

# That is why it is impossible to change the size of an array after resising it. But we can use a vector, but that will give a problem if there are high space constraints.
# So if you can afford TC = O(n) but low on memory, you must use a list