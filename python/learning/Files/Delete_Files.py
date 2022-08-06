import os
import shutil

# With os.remove() you can't delete empty folders
# With os.rmdir() you can delete empty folders but only empty folders not folders with items in it
# With shutil.rmtree() you can delete folders with items in it

path = 'Delete.txt'

try:
    os.remove(path)     # Delete a file
    os.rmdir(path)      # Delete an empty directory
    shutil.rmtree(path) # Delete a directory containing files
except FileNotFoundError:
    print('That file was not found')
except PermissionError:
    print('You dont have permission to do that')
except OSError:
    print('You can not delete that using that function')
else:
    print(path+' was deleted')