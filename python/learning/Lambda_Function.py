# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

# Normal way of multiplying a number by 2
def double(x):
    return x * 2
print(double(5))

# Faster way with lambda function
double = lambda x:x * 2
print(double(5))


multiply = lambda x,y: x * y
print(multiply(5,5))

# Simple age check with lambda
age_check = lambda age:True if age >= 18 else False
print(age_check(18))