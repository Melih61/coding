
# Remove spaces in string
my_string = '   Hello World     '
my_string = my_string.strip()
print(my_string)

# See how often a character or word is in a string
my_string = 'Hello World'
print(my_string.find('l'))

# Convert a list into a string
list1 = ['Hello','World']
new_string = ' '.join(list1)
print(new_string)

# Create a string from a list
my_list = ['a'] * 6
my_string = ''

# BAD PYTHON CODE FOR THAT
for i in my_list:
    my_string += i
print(my_string)

# GOOD PYTHON CODE FOR THAT
my_string = ''.join(my_list)
print(my_string)
