import subprocess
from tkinter import *
import os

# label = an area widget that holds text and/or an image within a window

window = Tk()
window.resizable(False, False)
window.geometry('512x800')
window.config(background='black')

photo = PhotoImage(file='C:\\Users\\melih\\PycharmProjects\\icon.png')
window.iconphoto(True, photo)

label = Label(window,
                  text='Welcome to Counter-Strike 1.6', # Text to show
                  font=('Courier',18), # 'Arial' = FontType , 40 = Size of text
                  fg='white', # foreground color (text color)
                  bg='black', # background color
                  relief=SUNKEN, # border type
                  bd=10, # border size
                  padx=20, # distance between the text and the x-borders
                  pady=20, # distance between the text the and y-borders
                  image=photo, # Image name
                  compound='top') # Where to locate the image to the text like "bottom"
label.pack()

window.mainloop()