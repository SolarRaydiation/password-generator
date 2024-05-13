import customtkinter
import math
from pwdgenerator import create_password

class PasswordGenerator(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # declare root window
        self.app = customtkinter.CTk()
        self.app.title("my app")
        self.app.geometry("600x500")
        self.app.minsize(600, 500)
        # prevents column from collapsing to the size of the widget inside.
        self.app.grid_columnconfigure(0, weight=1)

        # declare the StringVars
        # note: variables declared first or interpreter will complain
        self.use_digits = customtkinter.StringVar(value="on")
        self.use_uppercase = customtkinter.StringVar(value="on")
        self.use_lowercase = customtkinter.StringVar(value="on")
        self.use_sc = customtkinter.StringVar(value="on")
        self.char_length = 12 # default password length


        # declare the widgets for the window
        self.title = customtkinter.CTkLabel(
            master=self.app,
            text='PASSWORD GENERATOR',
            font=('Roboto', 30))
        self.subtitle = customtkinter.CTkLabel(
            master=self.app,
            font=('Roboto', 15),
            text='Generate a random and cryptographically secure password below!')
        self.subtitle.bind(
            '<Configure>',
            lambda e: self.subtitle.configure(wraplength=self.subtitle.winfo_width()))
        self.char_length_display = customtkinter.CTkLabel(
            master=self.app,
            text=f'{self.char_length} characters')
        self.slider = customtkinter.CTkSlider(
            master=self.app,
            from_=1, to=30,
            command=self._update_char_length_display) 
        self.password_field = customtkinter.CTkEntry(
            master=self.app,
            placeholder_text="Password goes here!")
        self.btn_copy = customtkinter.CTkButton(
            master=self.app,
            text='Copy',
            command=self._copy_to_clipboard)

        # delcare the checkboxes
        self.digit_checkbox = customtkinter.CTkCheckBox(
            self.app, text="Use digits?",
            command= self._generate_password,
            variable=self.use_digits,
            onvalue="on",
            offvalue="off")
        self.uppercase_checkbox = customtkinter.CTkCheckBox(
            self.app, text="Use uppercase letters?",
            command= self._generate_password,
            variable=self.use_uppercase,
            onvalue="on", offvalue="off")
        self.lowercase_checkbox = customtkinter.CTkCheckBox(
            self.app, text="Use lowercase letters?",
            command= self._generate_password,
            variable=self.use_lowercase,
            onvalue="on", offvalue="off")
        self.sc_checkbox = customtkinter.CTkCheckBox(
            self.app, text="Use special characters?",
            command= self._generate_password,
            variable=self.use_sc, onvalue="on", offvalue="off")

        # arrange the grid
        self.title.grid(row=0, column=0, padx=20, pady=20, stick='ew', columnspan=3)
        self.subtitle.grid(row=1, column=0, padx=20, pady=20, rowspan=2, stick='ew', columnspan=3)
        self.password_field.grid(row=3, column=0, padx=20, rowspan=2, stick='ew', columnspan=2)
        self.btn_copy.grid(row=3, column=2, padx=20, stick='ew')
        self.slider.grid(row=5, column=0, padx=20, pady=20, stick='ew', columnspan=2)
        self.char_length_display.grid(row=5, column=2, padx=40, pady=20, stick='ew')
        self.digit_checkbox.grid(row=6, column=0, padx=40, pady=20, stick='ew')
        self.uppercase_checkbox.grid(row=7, column=0, padx=40, pady=20, stick='ew')
        self.lowercase_checkbox.grid(row=8, column=0, padx=40, pady=20, stick='ew')
        self.sc_checkbox.grid(row=9, column=0, padx=40, pady=20, stick='ew')

        self.app.mainloop()
        self._generate_password()

    def _update_char_length_display(self, value):
        """ Updates the `char_lengt_display` widget to show the number of
        characters the generated password will produce.
        """
        self.char_length = math.floor(value)
        self.char_length_display.configure(text=f'{self.char_length} characters')
        self._generate_password()

    def _generate_password(self):
        """A wrapper function for `create_password()` in the `pwdgenerator.py` script.
        """
        try:
            generated_password = create_password(
                    self._parse_StringVar(self.use_lowercase.get()),
                    self._parse_StringVar(self.use_uppercase.get()),
                    self._parse_StringVar(self.use_digits.get()),
                    self._parse_StringVar(self.use_sc.get()),
                    self.char_length)
            print(generated_password)
            # the docs don't make it obvious but the delete()'s last index
            # arg is exclusive and not inclusive
            self.password_field.delete(0,len(self.password_field.get()))
            self.password_field.insert(0, generated_password)
        except:
            self.password_field.delete(0,len(self.password_field.get()))
            self.password_field.insert(0, "Ran into error while generating password!")
        
        print(self.char_length)
    
    def _copy_to_clipboard(self):
        # NOTE: arg is NOT needed and ignored
        self.app.clipboard_append(self.password_field.get())

    def _parse_StringVar(self, string: str) -> bool:
        """Converts StringVar instances to their boolean equivalent.
        """
        match(string):
            case 'on':
                return True
            case 'off':
                return False
            case _:
                raise Exception(f'Case {string} not found while parsing StringVar')

root = PasswordGenerator()