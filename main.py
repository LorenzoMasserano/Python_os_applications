import customtkinter as ctk
from utils.screen.screen_utils import screen_size_factory

app = ctk.CTk()

def customize_window(title: str, window_size: str):
    app.title(title)
    app.geometry(window_size)

def main():
    max_screen_size = screen_size_factory()
    resulution_string = max_screen_size.get_screen_size_string()

    customize_window(title= "Test", window_size= resulution_string) 

    app.mainloop()

main()


