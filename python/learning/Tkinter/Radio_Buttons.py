# radio button = similar to checkbox, but you can only select one from a group
from tkinter import *

food = ['Pizza','Hamburger','Hotdog']

def order():
    number = x.get()
    if number in range(0,3):
        print(f'You ordered a {food[number]}')
    else:
        print('huh?')

window = Tk()

x = IntVar()

pizzaImage = PhotoImage(file='python.png')
hamburgerImage = PhotoImage(file='icon.png')
hotdogImage = PhotoImage(file='test.png')
foodImages = [pizzaImage, hamburgerImage, hotdogImage]

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], # adds text to radio buttons
                              variable=x, # groups radiobuttons together if they share the same variable
                              value=index, # assigns each radio button a different value
                              padx=25, # adds padding on x-axis
                              font=('Courier',50), # font
                              image=foodImages[index], #add image to radio button
                              compound=LEFT, # adds image and text
                              indicatoron=0, # eliminate circle indicators
                              width= 375,
                              command=order
                              ).pack(anchor=W)
window.mainloop()