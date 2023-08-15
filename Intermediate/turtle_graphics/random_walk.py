import turtle
from turtle import Screen
import random

t = turtle.Turtle()

# change colormode specifications
# first thing to do if you want to generate rgb colors
# you'll tap into the turtle package itself and not the turtle object
turtle.colormode(255)

# turtle_colors = [
#     "red", "orange", "yellow", "green", "blue", "purple",
#     "pink", "brown", "cyan", "magenta", "lime", "indigo",
#     "teal", "gold", "silver"
# ]

# 0 facing right
# 90 facing up
# 180 facing left
# 270 facing down
directions = [0, 90, 180, 270]

# change shape
t.shape('turtle')
# change speed of the turtle movement
t.speed('fastest')
# change the thickness of the pen
t.pensize(10)

# function to generate random r, g, b colors and return it as a tuple
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return (r, g, b)

for _ in range(200):
    # change color
    t.color(random_color())
    
    t.forward(25)
    # t.right(random.choice(directions))
    # OR
    t.setheading(random.choice(directions))
    

# for a screen to show up, do this
# it should always be at the end of ypur code
screen = Screen()
screen.exitonclick()