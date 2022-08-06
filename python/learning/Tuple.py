# tuple = collection which is ordered and unchangeable
#         used to group together related data

# Normal tuple
tuple1 = ('Max',21,'Male')

# Print all values from tuple
for x in tuple1:
    print(x)

# Print how often a value is in a tuple
print(tuple1.count('Max')) # Output is 1

# Print on which index the value is
print(tuple1.index('Male')) # Output is 2 because 0 = Max, 1 = 21, 2 =

# Check if a value is in a tuple
if 'Max' in tuple1:
    print('Max is in the tuple')
