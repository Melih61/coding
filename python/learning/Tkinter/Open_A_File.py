from tkinter import *
from tkinter import filedialog

def openFile():
    path = filedialog.askopenfilename(initialdir='C:\\Users\\melih\\PythonProjects',
                                      title='Open file okay?',
                                      filetypes=(('Python files','*.py'),('All files','*.*')))
    file = open(path,'r') # rb rt
    print(file.read())
    file.close()

window = Tk()
button = Button(window,text='Open file',command=openFile)
button.pack()
window.mainloop()