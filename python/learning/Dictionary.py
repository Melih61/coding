# dictionary = A changeable, unordered collection of unique key:value pairs
#			   Fast because they use hashing, allow us to acces a value quickly

#MADE BY MALEH

# Normal dictionary
capitals = {'USA':'Washington DC',
			'India':'New Dehli',
			'China':'Beijing',
			'Russia':'Moscow'}

# Prints key, value -> Example: Russia Moscow
for key,value in capitals.items():
	print(key, value)

# Create new key:value pair in a dictionary
capitals.update({'Germany':'Berlin'})

# Change the value of a key
capitals.update({'USA':'Las Vegas'})

# Remove key from dictionary
capitals.pop('China')

# Clear the dictionary
capitals.clear()

# Print the value of a key
print(capitals['Russia'])

# Get the value of a key
print(capitals.get('Japan')) # Output is None because there is no Japan as a key

# Print all keys from a dictionary
print(capitals.keys())

# Print all values from a dictionary
print(capitals.values())

# Print all keys and values from a dictionary
print(capitals.items()) # Prints keys and values
