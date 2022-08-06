# sort() method     = used with lists
# sort() function   = used with iterables

# Sort a list alphabetically
students = ['Squidward','Sandy','Patrick','Spongebob','Mr.Krabs']
students.sort() # If you want to reverse the sort so its from z-a change it to students.sort(reverse=True)
for i in students:
    print(i)

# Sort an other iterable like a tumple
students = ('Squidward','Sandy','Patrick','Spongebob','Mr.Krabs')
sorted_students = sorted(students) # Here you can also reverse sort the iterable using sorted(students, reverse=True)
for i in sorted_students:
    print(i)

# -------------------------------------------------------------------------
students = [('Squidward','F', 60),
            ('Sandy','A', 33),
            ('Patrick','D', 36),
            ('Spongebob','B', 20),
            ('Mr.Krabs','C', 78)]

grade = lambda grades:grades[1]
students.sort(key=grade)
for i in students:
    print(i)
# -------------------------------------------------------------------------
students = (('Squidward','F', 60),
            ('Sandy','A', 33),
            ('Patrick','D', 36),
            ('Spongebob','B', 20),
            ('Mr.Krabs','C', 78))

age = lambda ages:ages[2]
sorted_students = sorted(students,key=age)
for i in sorted_students:
    print(i)
