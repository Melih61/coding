from tkinter import *
import time


WIDTH = 800
HEIGHT = 600
xVelocity = 8
yVelocity = 8

window = Tk()
window.geometry('800x600')
window.resizable(False, False)

canvas = Canvas(window,width=WIDTH,height=HEIGHT, background='#3f3f3f', bd=0)
canvas.pack()

window.config(background='black')

pythonPhoto = PhotoImage(file='python.png')
myImage = canvas.create_image(0,0,image=pythonPhoto,anchor=NW)

image_width = pythonPhoto.width()
image_height = pythonPhoto.height()

while True:
    coordinates = canvas.coords(myImage)
    #print(coordinates)
    if(coordinates[0]>=WIDTH-image_width or coordinates[0]<0):
        xVelocity = -xVelocity
    if(coordinates[1]>=HEIGHT-image_height or coordinates[1]<0):
        yVelocity = -yVelocity
    canvas.move(myImage,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
