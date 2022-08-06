# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (files creation and modification times

import shutil

#                Source     Where to copy
shutil.copyfile('Copy.txt','Copy_of_Copy.txt') #src.dst