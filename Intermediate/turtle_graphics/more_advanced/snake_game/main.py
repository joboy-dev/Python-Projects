from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import ScoreBoard

program = True

# while program:
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
# create new food object
food = Food()
# create nee scoreboard object
scoreboard = ScoreBoard()

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
    
    # detect collission with food
    if snake.head_of_snake.distance(food) < 15:
        # move food to a new location on screen
        food.refresh()
        # increase snake length
        snake.extend_snake()
        scoreboard.update_score()
        print(scoreboard.score)
    
    # detect collision with wall
    x = snake.head_of_snake.xcor()
    y = snake.head_of_snake.ycor()
    if x == 300 or x == -300 or y == 300 or y == -300:
        scoreboard.reset()
        snake.reset()
        
    # detect collision with snake body
    for segment in snake.segments[1:]:
        if snake.head_of_snake.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    
screen.exitonclick()
    