from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir='C:\\Users',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ('Text file','.txt'),
                                        ('Python File','.py'),
                                        ('All files','.*')
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()

window = Tk()
window.geometry('1920x1080')
window.resizable(False, False)
button = Button(text='Save',command=saveFile)
button.pack()
text = Text(window, bg='black',fg='#00FF00', font=('Courier',18), height=1920, width=1080)
text.pack()
window.mainloop()
