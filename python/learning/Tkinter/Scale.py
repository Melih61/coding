from tkinter import *

def submit():
    print('Current temperature is: ' + str(scale.get()) + 'C°')

window = Tk()
window.config(background='black')
fire = PhotoImage(file='python.png')
fireLabel = Label(image=fire)
fireLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL, # orientation of scale (veritcal, horizental)
              font = ('Courier',20),
              tickinterval=10, # Shows numeric 10-step indicators
              showvalue=0, # hide/show current value
              resolution=5, # increment of slider
              troughcolor='#69EAFF', # color
              fg='#FF1C00',
              bg='#111111',
              )
scale.set(0) # Set where it starts. If you dont use this it start by "to="
scale.pack()

snow = PhotoImage(file='test.png')
snowLabel = Label(image=snow)
snowLabel.pack()

button = Button(window,text='Submit',command=submit)
button.pack()

window.mainloop()