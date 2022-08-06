from tkinter import *

def create_window():
    new_window = Tk() # Toplevel() = new window 'on top' of other windows. If you close the window with the button this window closes too
                      # Tk() = new independent window. If you close the window with the button this window will still be there
    old_window.destroy() # Close old_window
old_window = Tk()

button = Button(old_window, text='Create new window', command=create_window).pack()

old_window.mainloop()