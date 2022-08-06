# listbox = A listing of selectable text items within its own container

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print(f'You have ordered: ')
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())


from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Courier',35),
                  width=12,
                  selectbackground='#f7ffde',
                  selectmode=MULTIPLE # select mode
                  )
listbox.pack()

listbox.insert(1,'pizza')
listbox.insert(2,'pasta')
listbox.insert(3,'garlic bread')
listbox.insert(4,'soup')
listbox.insert(5,'salad')

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text='Submit',command=submit).pack()

addButton = Button(window,text='Add',command=add).pack()

deleteButton = Button(window,text='Delete',command=delete).pack()

window.mainloop()