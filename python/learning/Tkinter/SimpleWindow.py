from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window
window.geometry('800x400')
window.title('SimpleWindow')
icon = PhotoImage(file='../../../PycharmProjects/cs1.6/icon.png')
window.iconphoto(True, icon)
window.config(background='black')

window.mainloop() # place window on computer screen, listen for events