from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(10)

# start listening for events
screen.listen()

# binding a keystroke to an event
# what this does now is, when the space key is pressed, the function is triggered
# NOTE: there is no need to add () to the function since it is being passed as an argument in another function 
screen.onkey(key='space', fun=move_forwards)

screen.exitonclick()