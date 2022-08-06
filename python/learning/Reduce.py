# reduce() = apply a function to an iterable and reduce it to be a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)
import functools

# Here we add each letter together until just one value (the whole word) exists
letters = ['H','E','L','L','O']
word = functools.reduce(lambda x,y,:x+y,letters)
print(word)

# Here we are multiplying the first two numbers so often that it only exist just one value
factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y:x * y,factorial)
print(result)