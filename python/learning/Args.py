# *args =   parameter that will pack all arguments into a tuple
#           useful so that a function can accept a carying amount of arguments

# Function that will add all numbers together given to *number (*args)
def add(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return  sum

# Change a value of a number
    numbers = list(stuff)
    numbers[0] = 0

print(add(1,2,3,4))
