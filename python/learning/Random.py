import random

# Generate a random number between two numbers (start_number = 1, end_number = 6)
x = random.randint(1,6)
print(x)

# Generate a random number between 0 and 1
y = random.random()
print(y)

# Pick a random value of a list
myList = ['rock','paper','scissors']
z = random.choice(myList)
print(z)

# Here you see how you can shuffle a list
cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
random.shuffle(cards)
print(cards)
