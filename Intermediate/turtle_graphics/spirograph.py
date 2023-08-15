import random
import turtle
from turtle import Screen

# function to generate random r, g, b colors and return it as a tuple
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return (r, g, b)


t = turtle.Turtle()

# change colormode specifications
# first thing to do if you want to generate rgb colors
# you'll tap into the turtle package itself and not the turtle object
turtle.colormode(255)

# change speed of the turtle movement
t.speed('fastest')

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        # change color
        t.color(random_color())
        
        # get current heading
        current_heading = t.heading()
        
        # draw circle
        t.circle(100)
        
        # set new heading to current_heading + 10
        t.setheading(current_heading + size_of_gap)

draw_spirograph(2)
    

# for a screen to show up, do this
# it should always be at the end of ypur code
screen = Screen()
screen.exitonclick()