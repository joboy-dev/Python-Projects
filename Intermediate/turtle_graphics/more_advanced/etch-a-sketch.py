from turtle import Turtle, Screen

t= Turtle()
screen = Screen()

t.shape('turtle')

def move_forwards():
    t.forward(10)

def move_backwards():
    t.back(10)
    
def move_right():
    t.right(10)
    
    # OR
    # heading = t.heading() + 10
    # t.setheading(heading)

def move_left():
    t.left(10)
    
    # OR
    # heading = t.heading() - 10
    # t.setheading(heading)
    
def clear_drawing():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    
screen.listen()
    
screen.onkeypress(key='Up', fun=move_forwards)
screen.onkeypress(key='Down', fun=move_backwards)
screen.onkeypress(key='Left', fun=move_left)
screen.onkeypress(key='Right', fun=move_right)
screen.onkey(key='c', fun=clear_drawing)

screen.exitonclick()