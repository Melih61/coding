# nested functions calls =  function calls inside other function calls
#                           innermost function calls are resolved first
#                           returned value is used as argument for the next outer function

# This is a function that convert a float number like 3.85 to a whole number like 4
number = input('Enter a whole positive number: ')
number = float(number)
number = abs(number)
number = round(number)
print(number)

# But we can do the same code in just one line
print(round(abs(float(input('Enter a whole positive number: ')))))
