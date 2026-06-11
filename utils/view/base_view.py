import customtkinter as ctk 

class BaseView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.show_view()

    def show_view(self):
        pass
