# set = Collection which is unordered, unindexed. No duplicate values

#MADE BY MALEH

# Normal sets
set1 = {'fork','spoon','knife'}
set2 = {'bowl','plate','cup'}
# !!! When there are multiple values of one word in a set it will only print one. Example when set1 were {'fork','knife','knife'} it will only print one knife

# Print values from a set
for x in set1:
    print(x)

# Add a value to a set
set1.add('napkin')

# Remove a value from a set
set1.remove('fork')

# Clear a set
set1.clear()

# Combine sets together
set1.update(set2)

# Create a new set by combining sets
set3 = set1.union(set2)

# Print the difference between sets
print(set1.difference(set2))

# Print which values sets have together
print(set1.intersection(set2))
