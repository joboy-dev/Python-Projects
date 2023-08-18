import pandas as pd
import turtle
import time

def create_turtle(x_pos, y_pos):
    '''Function to create a new turtle object'''
    
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x=x_pos, y=y_pos)
    t.write(arg=answer_state, align='center', font=('Courier', 8, 'bold'))

def create_feedback_turtle(x_pos, y_pos, text, colour):
    '''Function to create a new turtle object for displaying feed back messages'''
    
    tt = turtle.Turtle()
    tt.hideturtle()
    tt.penup()
    tt.goto(x=x_pos, y=y_pos)
    tt.color(colour)
    tt.clear()
    tt.write(arg=text, align='center', font=('Courier', 15, 'bold'))
    
    time.sleep(3.0)
    tt.clear()

# open csv file
data = pd.read_csv('Intermediate/pandas/US_states_game(with turtle)/50_states.csv')

screen = turtle.Screen()
screen.title('U.S. States Game')
screen.setup(width=750, height=700)

# working with images
image = 'Intermediate/pandas/US_states_game(with turtle)/blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

state_list = data.state.to_list()
guessed_states = []

game_on = True
score = 0
 
while game_on:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 states correct.', prompt="What's another state name?").capitalize()

    if answer_state == 'Exit':
        # store states that have not been guessed in a csv file
        # for state in state_list:
        #     if state not in guessed_states:
        #         unguessed_states.append(state)
        
        # list comprehension
        unguessed_states = [state for state in state_list if state not in guessed_states]
        
        unguessed_states_dict = {
            'Unguessed States': unguessed_states
        }
        df = pd.DataFrame(unguessed_states_dict)
        
        df.to_csv('Intermediate/pandas/US_states_game(with turtle)/unguessed_states.csv')
        
        break
    
    # check if user answer is in the list of states and is not a state the user has previously entered
    if (answer_state in state_list) and answer_state not in guessed_states:
        score += 1
        
        # add state to already listed states
        guessed_states.append(answer_state)
        
        # get x and y coordinates for the state entered
        x = data[data.state == answer_state].x.to_list()[0]
        y = data[data.state == answer_state].y.to_list()[0]  
        
        create_turtle(x_pos=x, y_pos=y)
    
    elif (answer_state in state_list) and answer_state in guessed_states:    
        create_feedback_turtle(x_pos=0, y_pos=310, text=f'{answer_state} has been listed.', colour='red')
    
    elif answer_state not in state_list:
        create_feedback_turtle(x_pos=0, y_pos=310, text=f'{answer_state} not an American state.', colour='red')
        
    elif score == 50:
        create_feedback_turtle(x_pos=0, y_pos=310, text='You win', colour='green')
    
    
        
# -----------------------------------------------------------------
# -----------------------------------------------------------------
 
# keep the screen open even if it is clicked on
# turtle.mainloop()

# def get_mouse_click_coor(x, y):
#     print(x, y)

# # get the position where a click event happens on screen
# turtle.onscreenclick(get_mouse_click_coor)
