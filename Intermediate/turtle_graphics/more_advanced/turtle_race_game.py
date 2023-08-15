from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
# set up width and height of the screen
screen.setup(height=400, width=500)
# bring up a popup
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color.').lower()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

for i in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    # set the coordinates you want the turtle to go to
    new_turtle.goto(x=-230, y=-100 + (i*30))
    
    # add each turtle to the list of turtles
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            
            # get the winning turtle pen color
            winning_color = turtle.pencolor()
            # check if pen color is the same as the color from the user's bet
            if winning_color == user_bet:
                print(f'You win. The {winning_color} turtle wins.')
                break
            else:
                print(f'You lose. The {winning_color} turtle wins.')
                break
            
                
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    


screen.exitonclick()