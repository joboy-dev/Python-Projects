from tkinter import *
import pandas as pd
import time
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    # Converting csv data into dictionary
    data = pd.read_csv('Intermediate/tkinter/flash_card/data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('Intermediate/tkinter/flash_card/data/french_words.csv')
finally:
    to_learn =data.to_dict(orient='records')
    # print(to_learn)


def next_card():
    '''Function to move to the next card'''
    
    global current_card, flip_timer
    # to prevent flipping of the card after moving to a new card
    window.after_cancel(flip_timer)
    
    current_card = random.choice(to_learn)
    # print(current_card)
    
    # french word
    french_word = current_card['French']
    
    card_canvas.itemconfig(card_image, image=front_image)
    card_canvas.itemconfig(card_title, text='French', fill='black')
    card_canvas.itemconfig(card_word, text=french_word, fill='black')
    
    # after 3 seconds flip the card
    flip_timer= window.after(3000, func=flip_card)
    

def is_known():
    '''Function that removes the word that the user knows from the list of words'''
    
    to_learn.remove(current_card)
    words_to_learn_data = pd.DataFrame(to_learn)
    # to avoid adding an index to the csv file
    words_to_learn_data.to_csv('Intermediate/tkinter/flash_card/data/words_to_learn.csv', index=False)
    
    next_card()
    

def flip_card():
    '''Function to flip the card'''
    
    # english word
    english_word = current_card['English']
    
    card_canvas.itemconfig(card_image, image=back_image)
    card_canvas.itemconfig(card_title, text='English', fill='white')
    card_canvas.itemconfig(card_word, text=english_word, fill='white')

# --------------------------------------------------------- #
# --------------------------------------------------------- #

window = Tk()
window.title('French-English Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# after 3 seconds flip the card
flip_timer = window.after(3000, func=flip_card)

# card canvas
card_canvas = Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)

# card images
front_image = PhotoImage(file='Intermediate/tkinter/flash_card/images/card_front.png')
back_image = PhotoImage(file='Intermediate/tkinter/flash_card/images/card_back.png')

card_image = card_canvas.create_image(400, 275, image=front_image)
card_canvas.grid(row=0, column=0, columnspan=3)

# canvas text
card_title = card_canvas.create_text(400, 140, text='', font=('Arial', 40, 'italic'))
card_word = card_canvas.create_text(400, 270, text='', font=('Arial', 60, 'bold'))

# button images
cancel_image = PhotoImage(file='Intermediate/tkinter/flash_card/images/wrong.png')
check_image = PhotoImage(file='Intermediate/tkinter/flash_card/images/right.png')

# Buttons
cancel_button = Button(image=cancel_image, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0, command=next_card)
cancel_button.grid(row=1, column=0)

check_button = Button(image=check_image, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=2)

next_card()

window.mainloop()
