import random
import turtle as t


color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]


tt = t.Turtle()

t.colormode(cmode=255)

# set pensize
tt.pensize(10)

tt.setheading(225)
tt.penup()
tt.forward(300)
tt.setheading(0)

def add_dots():
    for _ in range(10):        
        tt.pendown()
        tt.dot(20, random.choice(color_list))
        tt.penup()
        tt.forward(50)

for _ in range(10):
    add_dots()
    
    tt.setheading(90)
    tt.forward(50)
    tt.setheading(180)
    tt.forward(500)
    tt.setheading(0)
    

# OR
# number_of_dots = 100

# for dot_count in range(1, number_of_dots + 1):
#     tt.dot(20, random.choice(color_list))
#     tt.forward(50)

#     if dot_count % 10 == 0:
#         tt.setheading(90)
#         tt.forward(50)
#         tt.setheading(180)
#         tt.forward(500)
#         tt.setheading(0)

    
    

        
        




screen = t.Screen()
screen.exitonclick()