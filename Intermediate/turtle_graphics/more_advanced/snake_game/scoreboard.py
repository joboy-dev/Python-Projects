from turtle import Turtle

ALIGNMENT = 'center'
FONT_SPECS = ('Courier', 20, 'bold')

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        
        # open a file holding the high score
        with open('Intermediate/turtle_graphics/more_advanced/snake_game/high_score.txt') as high_score_file:
            self.high_score = int(high_score_file.read())
            
        self.score = 0
        print(self.high_score)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(y=270, x=0)
        self.show_scoreboard()
    
    
    def show_scoreboard(self):
        '''Function to show scoreboard'''
        
        # clear turtle text
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT_SPECS)
        
        
    def update_score(self):
        '''Function to update score shown on scoreboard'''
        
        # increment score by 1
        self.score += 1
        self.show_scoreboard()
        
        
    def reset(self):
        '''Function to reset game'''
        
        # update highscore
        if self.score > self.high_score:
            self.high_score = self.score
            
            # open file in read/write mode
            with open('Intermediate/turtle_graphics/more_advanced/snake_game/high_score.txt', 'w') as high_score_file:
                high_score_file.write(f'{self.high_score}')
                    
        # reset score
        self.score = 0
        self.show_scoreboard()
        