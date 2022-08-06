# index operator [] = gives acces to a sequence's element (str,list,tuples)

# Normal string
name = 'Max Mustermann!'

# Check if index[0] = "M" is upper case or not
if(name[0].isupper()):
    print('The first letter in "name" is upper case')
else:
    name = name.capitalize() # That changes the first letter in "name" to upper case

# Get the first name "Max" from "name"
first_name = name[0:3] # The 0 is because we are starting in the beginning of "name" and 3 because we want the first 3 letters M,a,x. !!! You can write "" instead of a 0 to start in the beginning
print(first_name)

# Get the last name "Mustermann" from "name"
last_name = name[4:] # The 4 is because we are starting by the fourth letter and the "" because we want to get all letters all way to the last letter
print(last_name)

# Get the last character "!" from "name"
last_character = name[-1] # -1 is because we want the last character if we would write -2 it would print "n"
print(last_character)
