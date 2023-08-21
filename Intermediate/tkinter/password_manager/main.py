from tkinter import *
from tkinter import messagebox
import random
import pyperclip

BG_COLOR = 'gray'
FG_COLOR = 'white'
FONT_SPECS = ('Arial', 10, 'bold')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    '''Function to generate random password'''
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= random.randint(8, 12)
    nr_symbols = random.randint(2, 5)
    nr_numbers = random.randint(2, 5)

    # using list compreension
    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    # make copy of existing list since shuffle method in random alters the original list
    shuffled_password_list = password_list.copy()
    random.shuffle(shuffled_password_list)

    password = ''.join(shuffled_password_list)
    
    if len(password_input.get()) > 0:
        password_input.delete(0, END)
        password_input.insert(0, password)
        
        # copy password to clipboard
        pyperclip.copy(password)
    else:
        password_input.insert(0, password)
        pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    '''Function to save password to a file'''
    
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    # check if user entered anything in the field
    if len(website) > 0 and len(email) > 0 and len(password) > 0:
        # ask confirmation
        confirmation = messagebox.askokcancel(title=website, message=f'These are the details entered:\nEmail: {email}\nPassword: {password}\n\nIs it okay to save?')
        
        if confirmation:
            with open('Intermediate/tkinter/password_manager/passwords.txt', 'a') as file:
                file.write(f'{website} | {email} | {password}\n')

            message_label.config(text='Password saved successfully!', fg='white', bg='green') 
            
            # messagebox.showinfo(title='Success', message='Password saved successfully')
            
            # clear fields
            website_input.delete(0, END)
            password_input.delete(0, END)
        
    else:
        messagebox.showwarning(title='Field(s) empty', message='Please do not leave any field empty')
        
        # message_label.config(text='No field must be left empty.', fg='white', bg='red') 


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(bg=BG_COLOR, padx=50, pady=50)

canvas = Canvas(width=200, height=200, background=BG_COLOR, borderwidth=0, highlightthickness=0)
image = PhotoImage(file='Intermediate/tkinter/password_manager/logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# -------------------- LABELS -------------------- #

# website label
website_label = Label(text='Website:', bg=BG_COLOR, fg=FG_COLOR, font=FONT_SPECS)
website_label.grid(row=1, column=0)

# email label
email_label = Label(text='Email or Username:', bg=BG_COLOR, fg=FG_COLOR, font=FONT_SPECS)
email_label.grid(row=2, column=0)

# password label
password_label = Label(text='Password:', bg=BG_COLOR, fg=FG_COLOR, font=FONT_SPECS)
password_label.grid(row=3, column=0)

# ----------------- INPUT FIELDS -------------------- #

# website input
website_input = Entry(bg='white', fg='black', width=40, border=1, borderwidth=0.5, highlightthickness=0, font=FONT_SPECS)
website_input.grid(row=1, column=1, pady=5, columnspan=2)
# immediately you open the app, you can start typing in this entry field
website_input.focus()

# email input
email_input = Entry(bg='white', fg='black', width=40, border=1, borderwidth=0.5, highlightthickness=0, font=FONT_SPECS)
email_input.grid(row=2, column=1, pady=5, columnspan=2)
# add pre-populated data into a field
email_input.insert(0, 'josephkorede36@gmail.com')

# password_input
password_input = Entry(bg='white', fg='black', width=27, border=1, borderwidth=0.5, highlightthickness=0, font=FONT_SPECS)
password_input.grid(row=3, column=1, pady=5)

# ------------------ BUTTONS ------------------------ #

# generate password button
generate_password_button = Button(text='Generate', command=generate_password, bg=BG_COLOR, fg=FG_COLOR, border=0, borderwidth=1, highlightthickness=0, width=12)
generate_password_button.grid(row=3, column=2, pady=5)

# add password button
add_password_button = Button(text='Add Password', command=save_password, bg=BG_COLOR, fg=FG_COLOR, border=2, borderwidth=1, highlightthickness=0, width=40)
add_password_button.grid(row=4, column=1, columnspan=2)

# message label
message_label = Label(bg=BG_COLOR, font=FONT_SPECS, pady=5, padx=10)
message_label.grid(row=5, column=1, pady=10)

window.mainloop()
