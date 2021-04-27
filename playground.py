# Use '*' to take an unlimited number of position arguments (dtype = tuple)
# Modify the add function to take an unlimited number of arguments.
def add(*args):
# # Use a loop to sum all the arguments inside the function
    total = 0
    for arg in args:
        total+=arg
    return total
# Test it out by calling add() to calculate sum of some arguments.
print(add(5, 2, 3))
