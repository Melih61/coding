import os

source = 'Move.txt'
destination = 'C:\\Users\\melih\\PythonProjects\\Projects\\Move.txt'

try:
    # Here we check if a file already exists
    if os.path.exists(destination):
        print('There is already a file there')
    else:
        # 0 = file to move, 1 = where to move
        os.replace(source, destination)
        print('Succesfully moved {} to {}'.format(source,destination))
except FileNotFoundError:
    print('File does not exist')
