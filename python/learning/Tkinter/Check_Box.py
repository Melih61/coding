from tkinter import *

def display():
    if(x.get()==1):
        print('You agree!')
    else:
        print('You dont agree :(')

window = Tk()
window.config(background='black')
x = IntVar()

photo = PhotoImage(file='python.png')

Checkbutton(window,
            text='I aggree to something',
            variable=x,
            onvalue=1,
            offvalue=0,
            command=display,
            font=('Arial', 20),
            fg='#00FF00',
            bg='black',
            activeforeground='#00FF00',
            activebackground='black',
            padx=25,
            pady=10,
            image=photo,
            compound='left').pack()

window.mainloop()