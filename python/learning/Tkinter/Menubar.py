from tkinter import *
from tkinter import filedialog
import os

path = None

def saveFile():
    file = filedialog.asksaveasfile(filetypes=[('Python Files','.py'),('All files', '.*')])
    if file == None:
        return
    filetext = str(text_field.get(1.0,END))
    file.write(filetext)
    file.close()
def openFile():
    global path
    path = filedialog.askopenfilename(filetypes=[('Python Files','.py')])
    if path == None:
        return
    file = open(path, 'r')
    file_name = os.path.basename(path)
    window.title(file_name + ' - Python Editor 1.0')
    text_field.insert(1.0, file.read())
def cut():
    print('You cut some text')
    run_code()
def copy():
    print('You copied some text')
def paste():
    print('You pasted some text')
def run_code():
    var = os.popen('python '+path).read()
    console.config(text=var)

window = Tk()
window.config(background='#464646')
window.title('Python Editor 1.0')
window.geometry('1280x960')
menubar = Menu(window)
text_field = Text(window, bg='grey',fg='black', font=('Consolas',15))
text_field.pack()
console = Label(window, bg='white',fg='black', width=960, height=360, font=('Courier',20))
console.pack()
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=('Consolas',10), bg='#464646',fg='white')
menubar.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='Open',command=openFile)
fileMenu.add_command(label='Save',command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=quit)

editMenu = Menu(menubar,tearoff=0, font=('Consolas',10),bg='#464646',fg='white')
menubar.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(label='Copy',command=copy)
editMenu.add_command(label='Paste',command=paste)
editMenu.add_command(label='Cut',command=cut)


window.mainloop()