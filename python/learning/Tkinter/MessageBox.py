import time
from tkinter import *
from tkinter import messagebox # import messagebox library

def click():
    #messagebox.showinfo(title='Info',message='You are a person')
    #messagebox.showwarning(title='Warning', message='You have a virus')
    #messagebox.showerror(title='Error', message='something went wrong')

    if messagebox.askokcancel(title='Windows Installer',message='Do you want to install Windows 11 Pro?'):
        pass
    else:
        print('You cancelled the installation')

    #if messagebox.askretrycancel(title='Windows Installer',message='Do you want to retry installing Windows 11 Pro?'):
    #    pass
    #else:
    #    print('You cancelled the installation')

    #if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):
    #    print('I like cake too')
    #else:
    #    print('Why do you not like cake?')

    #answer = messagebox.askquestion(title='ask question',message='Do you like pie?')
    #if answer == 'yes':
    #    print('I like pie too')
    #else:
    #    print('Why do you not like pie?')

    answer = messagebox.askyesnocancel(title='Test',message='Are you sure about that?',icon='error')
    if answer == True:
        print('You are sure about that')
    elif answer == False:
        print('You are not sure about that')
    else:
        print('You have dodged the question')
window = Tk()

button = Button(window,command=click,text='Click me').pack()

window.mainloop()