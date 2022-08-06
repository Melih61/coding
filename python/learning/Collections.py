from collections import Counter

# Print how often a character is in a string
a = 'aaaaaabbbbbbbbbcccccccc'
my_counter = Counter(a)
print(my_counter.items())

# Print the values of a string
a = 'aaabbbccc'
my_counter = Counter(a)
print(my_counter.values())

# Print the most common character from a string
a = 'aaaaabbccc'
my_counter = Counter(a)
print(my_counter.most_common(1))
