from tkinter import *

# entry widget = textbox that accepts a single line of user input

def submit():
    text = entry.get()
    print('Hello {}'.format(text))
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

window.config(background='black')

entry = Entry(window,
              font=('Courier',50),
              fg='#00FF00',
              bg='black',
              show='*',
              disabledbackground='black',
              disabledforeground='#00FF00')
entry.pack(side=LEFT)
#entry.insert(0, 'Spongebob') inserts spongebob

delete_button = Button(window, text='Delete', command=delete).pack(side=RIGHT)
backspace_button = Button(window, text='Backspace', command=backspace).pack(side=RIGHT)
submit_button = Button(window, text='Submit', command=submit).pack(side=RIGHT)


window.mainloop()