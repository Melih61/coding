from tkinter import *
from Balls_For_Animation import *
import time

from Learning.Tkinter import Balls_For_Animation

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Balls_For_Animation.Ball(canvas,0,0,100,1,1,'white')
tennis_ball = Balls_For_Animation.Ball(canvas,0,0,50,4,3,'yellow')
basket_ball = Balls_For_Animation.Ball(canvas,0,0,125,8,7,'orange')

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()