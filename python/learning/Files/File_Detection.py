import os
#                  NAME
path = 'C:\\Users\\melih\\PythonProjects\\Learning\\Everything_With_Files\\test.txt'

# Check if path exists
if os.path.exists(path):
    print('That location exists!')
    # Check if path is a file
    if os.path.isfile(path):
        print('That is a file')
    # Check if path is a directory (folder)
    elif os.path.isdir(path):
        print('That is a directory')
else:
    print('That location doesnt exist')
