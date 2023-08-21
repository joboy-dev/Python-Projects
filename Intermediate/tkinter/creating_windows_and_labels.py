import tkinter as tk


def clicked():
    label.config(text=input.get())


# creating a window
window = tk.Tk()
# adding a title
window.title('Windows and Labels')
# changing minimum size
window.minsize(width=500, height=300)
# changing padding around window
window.config(padx=20, pady=20)

# creating a label
label = tk.Label(text='A new label.', font=('Arial', 24, 'bold'))
# label.pack() # automatically centers label on screen
# label.place(x=20, y=0) # for precise positoning
label.grid(column=0, row=0)
# adding padding
label.config(padx=10, pady=20)

# changing text in a label(component)
# label['text'] = 'Changed text'
# OR
# label.config(text='Changed text config')

# creating a button
button = tk.Button(text='Click Me', background='black', foreground='white', command=clicked)
# button.pack()
button.grid(column=1, row=1)

# creating a button
button1 = tk.Button(text='Click Me', background='black', foreground='white', command=clicked)
# button.pack()
button1.grid(column=2, row=0)


# entry component(Input)
input = tk.Entry(width=20)
# input.pack()
input.grid(column=3, row=4)
# getting the text entered in the input field
value = input.get()
print(value)




window.mainloop()