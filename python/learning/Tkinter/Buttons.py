from tkinter import *

# button = you click it, then it does stuff

count = 0
def click():
    global count
    count += 1
    print(count)

window = Tk()

photo = PhotoImage(file='icon.png')

button = Button(window,
                text='Click me!',
                command=click,
                font=('Comic Sans',30),
                fg='#00FF00',
                bg='black',
                activebackground='black',
                activeforeground='#00FF00',
                state=ACTIVE,
                image=photo,
                compound='bottom',)
button.pack()

window.mainloop()