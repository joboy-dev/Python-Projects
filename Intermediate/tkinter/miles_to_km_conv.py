from tkinter import *

# ----------------------- CONSTANTS ---------------------------
LABEL_PADDING = 20
FONT_SPECS = ('Arial', 13, 'normal')


# ----------------------- FUNCTIONS ---------------------------
def convert_unit():
    '''Function to perform unit conversion'''
    # get input from entry widget
    miles = float(miles_input.get())
    km = miles * 1.60934
    # change text in widget
    converted_number_label.config(text=f'{km}')

# def create_error_label(text):
#     '''Function to add a new error label'''
#     error_label = Label(text=text, foreground='red', font=FONT_SPECS)
#     error_label.grid(row=4, column=2)
#     error_label.config(padx=LABEL_PADDING)


# ----------------------- MAIN CODE ---------------------------
window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)
window.minsize(width=400, height=200)

# entry widget
miles_input = Entry()
miles_input.grid(row=1, column=2)

# Miles
mile_label = Label(text='Miles', font=FONT_SPECS)
mile_label.grid(row=1, column=3)
mile_label.config(padx=LABEL_PADDING)

# is equal to
is_equal_to_label = Label(text='is equal to', font=FONT_SPECS)
is_equal_to_label.grid(row=2, column=1)
is_equal_to_label.config(padx=LABEL_PADDING)

# converted number
converted_number_label = Label(text='0', font=FONT_SPECS)
converted_number_label.grid(row=2, column=2)
converted_number_label.config(padx=LABEL_PADDING)

# km label
km_label = Label(text='Km', font=FONT_SPECS)
km_label.grid(row=2, column=3)
km_label.config(padx=LABEL_PADDING)

# calculate button
calculate_button  = Button(text='Calculate', command=convert_unit)
calculate_button.grid(row=3, column=2)
calculate_button.config(padx=LABEL_PADDING)


window.mainloop()