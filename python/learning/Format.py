# str.format() =    optional method that gives users
#                   more control when displaying output

animal = 'cow'
item = 'moon'

# Normal method to use both string in a text
print('The ' + animal + ' jumped over the ' + item)

# str.format() method in a text
print('The {} jumped over the {}'.format(animal, item))

# Using str.format() with numbers -> The number is the value of the string (0 = cow, 1 = moon)
print('The {0} jumped over the {1}'.format(animal, item))

# We can also use str.format() using keyword arguments
print('The {animal} jumped over the {item}'.format(animal=animal,item=item))

# We can also use "f" before the string
print(f'The {animal} jumped over the {item}')


# We can also enter the values when we want to print the string like this
text = 'The {} jumped over the {}'
print(text.format(animal,item))

# Automaticly add commas at number like 100 thousand, 5 million and so on
number = 1000000000
print('Number: {:,}'.format(number)) # Output will be 100,000,000,000

# How to convert a number into a binary number
number = 1000
print('Binary: {:b}'.format(number)) # Output will be 1111101000
