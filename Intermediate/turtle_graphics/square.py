from turtle import Turtle, Screen

new_turtle = Turtle()

# change shape
new_turtle.shape('turtle')
# change color
new_turtle.color('blue', 'black')


# use for loop
for _ in range(4):
    new_turtle.forward(100)
    new_turtle.right(90)



# for a screen to show up, do this
# it should always be at the end of ypur code
screen = Screen()
screen.exitonclick()