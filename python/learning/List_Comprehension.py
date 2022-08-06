# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]

# Normal way of doing a loop that add values to a list
squares = []
for i in range(1,11):
    squares.append(i * i)
print(squares)

# Faster way with list comprehensions
squares = [i * i for i in range(1,11)]
print(squares)

# ----------------------------------------------------------------
students = [100,90,80,70,60,50,40,30,0]

# Normal way of creating a function that creates a list for the students that passed
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

# Faster way with a list comprehension
passed_students = [i for i in students if i >= 60]
print(passed_students)

# Fast way with strings (PASSED, FAILED)
passed_students = ['PASSED' if i >= 60 else 'FAILED' for i in students]
print(passed_students)
# ----------------------------------------------------------------
