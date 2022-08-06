from tkinter import *

def doSomething(event):
    print('Mouse coordinates: ' + str(event.x)+','+ str(event.y))

window = Tk()

window.bind('<Button-1>',doSomething) # left mouse click
window.bind('<Button-2>',doSomething) # scroll wheel click
window.bind("<Button-3>",doSomething) # right mouse click
window.bind("<ButtonRelease>",doSomething) # button release
window.bind("<Enter>",doSomething) # when entering window
window.bind("<Leave>",doSomething) # when leaving window
window.bind('<Motion>',doSomething) # Where the mouse move

window.mainloop()