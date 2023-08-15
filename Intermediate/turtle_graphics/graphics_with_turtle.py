from turtle import Turtle, Screen

new_turtle = Turtle()

# change shape
new_turtle.shape('turtle')
# change color
new_turtle.color('blue', 'green')

# movement
new_turtle.forward(100)
new_turtle.right(60)
# new_turtle.up
new_turtle.forward(100)
# new_turtle.down
new_turtle.right(60)
new_turtle.forward(100)






# for a screen to show up, do this
# it should always be at the end of ypur code
screen = Screen()
screen.exitonclick()