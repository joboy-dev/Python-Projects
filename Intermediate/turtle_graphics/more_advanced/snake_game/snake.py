from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    '''Class to handle all snake functionality'''
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head_of_snake = self.segments[0]
        self.head_of_snake.color('grey')
        
    
    def create_snake(self):
        '''Function to create the snake'''
        
        # since 3 squares are needed, use a for loop to add turtle objects to the segments
        for position in STARTING_POSITIONS:
            self.add_segment(position)   
    
    
    def add_segment(self, position):
        '''Function to add a new segment to the list of segments'''
        new_segment = Turtle(shape='circle')
        new_segment.color('white')
        new_segment.penup()
        # move turtle object to a specific location on screen
        new_segment.goto(position)
        self.segments.append(new_segment) 
    
    
    def extend_snake(self):
        '''Function to increase length of snake'''
        
        # add new segment to the position of the last snake segment
        self.add_segment(self.segments[-1].position())
    
    
    def move(self):
        '''Function to move the snake'''
        
        # connect all segments together
        for seg_no in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_no -1].xcor()
            new_y = self.segments[seg_no -1].ycor()
            
            # segment 2 will go to where segment 1 and segment 1 will go where segment 0(head of snake) is
            self.segments[seg_no].goto(x=new_x, y=new_y)
            
        self.head_of_snake.forward(MOVE_DISTANCE)
    
    def reset(self):
        '''Function to rest the snake'''
        
        # to clear the snake segments still on screen after game is over, send those segments off the screen to a different location
        for seg in self.segments:
            seg.goto(x=3000, y=3000)
        
        self.segments.clear()
        # create new snake
        self.create_snake()
        self.head_of_snake = self.segments[0]
        self.head_of_snake.color('grey')
        
        
    def up(self):
        '''Function to move snake up'''
        
        # perform check to ensure that the snake does not go in the opposite direction
        if self.head_of_snake.heading() != DOWN:
            self.head_of_snake.setheading(UP)

    
    def down(self):
        '''Function to move snake down'''
        
        # perform check to ensure that the snake does not go in the opposite direction
        if self.head_of_snake.heading() != UP:
            self.head_of_snake.setheading(DOWN)
        
    
    def left(self):
        '''Function to move snake left'''
        
        # perform check to ensure that the snake does not go in the opposite direction
        if self.head_of_snake.heading() != RIGHT:
            self.head_of_snake.setheading(LEFT)
        
            
    def right(self):
        '''Function to move snake right'''
        
        # perform check to ensure that the snake does not go in the opposite direction
        if self.head_of_snake.heading() != LEFT:
            self.head_of_snake.setheading(RIGHT)
