# keyword arguments =   arguments preceded by an identifier when we pass them to a function
#                       The order of the arguments doesnt matter, unlike positional arguments
#                       Python knows the names of the arguments that our function receives

# Normal function
def hello(first,middle,last):
    print('Hello ' + first + ' ' + middle + ' ' + last)

# Here we enter the variable and the value of the variable
hello(first='Max',middle='Maximilian',last='Mustermann')
