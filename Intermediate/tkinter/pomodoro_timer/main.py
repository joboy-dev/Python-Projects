from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0
check_mark_string = ''


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    '''Function to reset timer'''
    
    window.after_cancel(timer)
    
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', foreground=GREEN)
    check_marks.config(text='')
    
    # to prevent transitioning from work to break after stopping the timer and starting again, set reps back to zero
    global reps
    reps = 0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    '''Function to start timer'''
    
    global reps
    # increase rep by 1
    reps += 1
    
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    
    
    #----------------------------- FORMAT -----------------------
    
    # Work - 25min
    # Short break - 5min
    # Work -25min
    # Short break - 5min
    # Work -25min
    # Short break - 5min
    # Work -25min
    # Long break - 20min
    
    # ----------------------------------------------------------- #
        
    if reps % 8 == 0:
        count_down(long_break_secs)
        title_label.config(text='Long Break', foreground=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        title_label.config(text='Short Break', foreground=PINK)
    else:
        count_down(work_secs)
        title_label.config(text='Work', foreground=GREEN)
    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    '''Function to implement countdown'''
        
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_sec == 0:
        count_sec = f'{count_sec}0'
    elif count_sec < 10:
        count_sec = f'0{count_sec}'
    
    # chamging canvas text
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        global reps, check_mark_string
        
        if reps % 2 == 0:
            check_mark_string += '✅'
            check_marks.config(text=check_mark_string)
            
        # once count down reaches zero, call the function to start timer again
        start_timer()
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Timer')
window.config(background=YELLOW, padx=100, pady=50)
# window.minsize(width=600, height=550)


# title label
title_label = Label(text='Timer', foreground=GREEN, background=YELLOW, font=(FONT_NAME, 50), justify='center')
title_label.grid(row=0, column=1)

# creating a canvas to place widgets
canvas = Canvas(background=YELLOW, width=200, height=224)
# working with images
tomato_img = PhotoImage(file='Intermediate/tkinter/pomodoro_timer/tomato.png')
# putting image on canvas
canvas.create_image(100, 112, image=tomato_img)
# putting text on canvas
timer_text = canvas.create_text(100, 138, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

# start button
start_button = Button(text='Start', font=(FONT_NAME, 12), foreground='blue', background=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

# reset button
reset_button = Button(text='Reset', font=(FONT_NAME, 12), foreground='blue', background=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(foreground=GREEN, background=YELLOW, font=(FONT_NAME, 20, 'bold'))
check_marks.grid(row=3, column=1)


window.mainloop()