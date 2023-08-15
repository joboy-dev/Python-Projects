from turtle import Turtle

MOVE_DISTANCE = 20

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
        for i in range(3):
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            # move turtle object to a specific location on screen
            new_segment.goto(y=0, x=0 - (i*MOVE_DISTANCE))
            self.segments.append(new_segment)    
    
    def move(self):
        '''Function to move the snake'''
        
        for seg_no in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_no -1].xcor()
            new_y = self.segments[seg_no -1].ycor()
            
            # segment 2 will go to where segment 1 and segment 1 will go where segment 0(head of snake) is
            self.segments[seg_no].goto(x=new_x, y=new_y)
            
        self.head_of_snake.forward(MOVE_DISTANCE)
    
    
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
