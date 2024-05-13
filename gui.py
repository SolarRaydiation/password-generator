"""
everything in tkinter is a widget
everything on kinter is a two step proces: you have to define the thing and then make it show up on the screen
pack - shoving it into TK

"""

import customtkinter
import math
from pwdgenerator import create_password

class PasswordGenerator(customtkinter.CTk):
    def __init__(self):
        # declare root window
        app = customtkinter.CTk()
        app.title("my app")
        app.geometry("600x500")
        app.minsize(600, 500)
        # prevents column from collapse to the size of the widget inside.
        app.grid_columnconfigure(0, weight=1)

        # declare the widgets for the window
        # TO-DO: clean up to be PEP8 compliant
        title = customtkinter.CTkLabel(app, text='PASSWORD GENERATOR', font=('Roboto', 30))
        subtitle = customtkinter.CTkLabel(app, font=('Roboto', 15), text='Generate a random and cryptographically secure password below!')
        subtitle.bind( '<Configure>', lambda e: subtitle.configure(wraplength=subtitle.winfo_width()))
        char_count = customtkinter.CTkLabel(app, text='6 characters')
        slider = customtkinter.CTkSlider(app, from_=0, to=30, command=lambda e: char_count.configure(text=f'{math.floor(e)} characters'))
        password_field = customtkinter.CTkEntry(app, placeholder_text="Password goes here!")
        btn_copy = customtkinter.CTkButton(app, text='Copy', command=lambda e: print('Copy!'))

        # declare the variables for the checkboxes below
        # note: variables declared first or interpreter will complain 
        use_digits = customtkinter.StringVar(value="on")
        use_uppercase = customtkinter.StringVar(value="on")
        use_lowercase = customtkinter.StringVar(value="on")
        use_sc = customtkinter.StringVar(value="on")
        char_length = 12 # default password length

        # delcare the checkboxes
        # TO-DO: clean up to be PEP8 compliant
        digit_checkbox = customtkinter.CTkCheckBox(app, text="Use digits?", command=None,
                                            variable=use_digits, onvalue="on", offvalue="off")
        uppercase_checkbox = customtkinter.CTkCheckBox(app, text="Use uppercase letters?", command=None,
                                            variable=use_uppercase, onvalue="on", offvalue="off")
        lowercase_checkbox = customtkinter.CTkCheckBox(app, text="Use lowercase letters?", command=None,
                                            variable=use_lowercase, onvalue="on", offvalue="off")

        sc_checkbox = customtkinter.CTkCheckBox(app, text="Use special characters?", command=None,
                                            variable=use_sc, onvalue="on", offvalue="off")

        # arrange the grid
        title.grid(row=0, column=0, padx=20, pady=20, stick='ew', columnspan=3)
        subtitle.grid(row=1, column=0, padx=20, pady=20, rowspan=2, stick='ew', columnspan=3)
        password_field.grid(row=3, column=0, padx=20, rowspan=2, stick='ew', columnspan=2)
        btn_copy.grid(row=3, column=2, padx=20, stick='ew')
        slider.grid(row=5, column=0, padx=20, pady=20, stick='ew', columnspan=2)
        char_count.grid(row=5, column=2, padx=40, pady=20, stick='ew')
        digit_checkbox.grid(row=6, column=0, padx=40, pady=20, stick='ew')
        uppercase_checkbox.grid(row=7, column=0, padx=40, pady=20, stick='ew')
        lowercase_checkbox.grid(row=8, column=0, padx=40, pady=20, stick='ew')
        sc_checkbox.grid(row=9, column=0, padx=40, pady=20, stick='ew')

        app.mainloop()
    
    def set_password():
        pass

    def copy_to_clipboard():
        pass

root = PasswordGenerator()