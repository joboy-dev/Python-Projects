from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
# set screen background color
screen.bgcolor('black')
# set title of program
screen.title('Snakezy')
# turn off tracer
screen.tracer(0)

# create a new snake object
snake = Snake()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)
    
game_on = True
while game_on:
    # refresh the screen to show new updates. this is for state management
    screen.update()
    # this is needed to allow time for the graphics to show on the screen, or else nothing will show
    time.sleep(0.1)
    
    # call function to move snake
    snake.move()
        

screen.exitonclick()

    