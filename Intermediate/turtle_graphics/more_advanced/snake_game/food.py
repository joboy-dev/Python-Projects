from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color('red')
        self.speed('fastest')
        self.refresh()
        
    def refresh(self):
        '''Function to move food to a new position on screen'''
        
        # set the food at a random position on screen
        self.goto(x=random.randint(-250, 250), y=random.randint(-250, 240))