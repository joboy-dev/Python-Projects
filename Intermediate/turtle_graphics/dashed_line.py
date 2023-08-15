from turtle import Turtle, Screen

t = Turtle()

# change shape
t.shape('turtle')
# change color
t.color('blue', 'black')


# use for loop
for _ in range(50):
    # put pen down
    t.pendown()
    # draw
    t.forward(10)
    # take the pen up
    t.penup()
    # draw again
    t.forward(10)



# for a screen to show up, do this
# it should always be at the end of ypur code
screen = Screen()
screen.exitonclick()