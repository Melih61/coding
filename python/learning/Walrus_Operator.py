# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# Normal way of printing a variable
happy = True
print(happy)

# Faster way with the walrus operator
print(happy := True)

# --------------------------------------------------
# Normal way of making a favorite food adder
foods = list()
while True:
    food = input('What food do you like?: ')
    if food == 'quit':
        break
    foods.append(food)

# Faster way with the walrus operator
foods = list()
while food := input('What food do you like?: ') != 'quit':
    foods.append(food)