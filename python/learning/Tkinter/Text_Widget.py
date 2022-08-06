# text widget = functions like a text area, you can enter multiple lines of text
from tkinter import *

def submit():
    input = text.get('1.0',END)
    print(input)

window = Tk()
text = Text(window,
            bg='black',
            foreground='#00FF00',
            font=('Courier',16),
            height=8,
            width=20,
            padx=0,
            pady=0)
text.pack()
button = Button(window,text='Submit',command=submit).pack()
window.mainloop()