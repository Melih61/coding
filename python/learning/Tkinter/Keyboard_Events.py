from tkinter import *

def doSomething(event):
    #print('You pressed: ' + event.keysym)
    label.config(text=event.keysym)

window = Tk()

# Enter = <Return> | Every key = <Key>
window.bind('<Key>',doSomething)

label = Label(window,font=('Courier',100))
label.pack()

window.mainloop()