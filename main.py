import customtkinter as ctk
from utils.screen.screen_utils import screen_size_factory

app = ctk.CTk()

def change_text(welcome_label: ctk.CTkLabel, name_entry: ctk.CTkEntry):
    user_text = name_entry.get()
    
    if user_text.strip() == "":
        welcome_label.configure(text="Please type something first!")
    else:
        welcome_label.configure(text=f"Hello, {user_text}! It works!")

def customize_window(title: str, window_size: str):
    app.title(title)
    app.geometry(window_size)
    
def customize_ui():

    welcome_label = ctk.CTkLabel(
        app, 
        text="Type your name below:", 
       font=("Helvetica", 18)
    )

    name_entry = ctk.CTkEntry(
        app, 
        placeholder_text="Enter your name here...", 
        width=250
    )

    submit_button = ctk.CTkButton(
        app, 
        text="Click Me", 
        command=lambda: change_text(welcome_label=welcome_label, name_entry=name_entry)
    )
    
    welcome_label.pack(pady= 40, padx= 20)
    name_entry.pack(pady= 40, padx= 20)
    submit_button.pack(pady= 40, padx= 20) 

def main():
    max_screen_size = screen_size_factory()
    resulution_string = max_screen_size.get_screen_size_string()

    customize_window(title= "Test", window_size= resulution_string) 
    customize_ui()

    app.mainloop()

main()


