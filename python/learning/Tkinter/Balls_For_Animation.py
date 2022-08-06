# This file uses Multiple_Animations.py
from Learning.Tkinter import Multiple_Animations


class Ball:

    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)
        print(coordinates)
        ball_width = self.canvas.winfo_width()
        ball_height = self.canvas.winfo_height()
        if coordinates[2] >= ball_width or coordinates[0] < 0:
            self.xVelocity = -self.xVelocity
        if coordinates[3] >= ball_height or coordinates[0] < 0:
            self.yVelocity = -self.yVelocity
        self.canvas.move(self.image, self.xVelocity, self.yVelocity)
