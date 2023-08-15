from turtle import Turtle, Screen
import random

t = Turtle()

turtle_colors = [
    "red", "orange", "yellow", "green", "blue", "purple",
    "pink", "brown", "cyan", "magenta", "lime", "indigo",
    "teal", "gold", "silver"
]


# change shape
t.shape('turtle')
t.speed(3)

# define a function to draw the shape
def draw_shape(sides):
    for _ in range(sides):
        angle = 360 / sides
        t.forward(100)
        t.right(angle)

# run a for loop to handle assigning of sides to the function
for i in range(3, 11):
    t.color(random.choice(turtle_colors))
    draw_shape(i)

# for a screen to show up, do this
# it should always be at the end of ypur code
screen = Screen()
screen.exitonclick()