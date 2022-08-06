from tkinter import *
from tkinter import colorchooser #submodule

def click():
    color = colorchooser.askcolor()
    window.config(background=color[1])

window = Tk()
window.geometry('800x400')
button = Button(text='Click me',command=click)
button.pack()
window.mainloop()