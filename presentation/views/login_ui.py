import customtkinter as ctk
from presentation.controllers.login_ctrl import LoginCtrl
from utils.view.base_view import BaseView

class LoginUi(BaseView):
    def __init__(self, login_ctrl: LoginCtrl, app: ctk.CTk):
        self.login_ctrl = login_ctrl
        self.app = app
        super().__init__(master=app)

    def show_view(self):
       
        title_label = ctk.CTkLabel(self, text="Login", font=("Helvetica", 20))

        form_frame = ctk.CTkFrame(self, fg_color="transparent")
        account_field_description_label = ctk.CTkLabel(form_frame, text="Account:", font=("Helvetica", 14))
        account_entry = ctk.CTkEntry(form_frame, placeholder_text="ACCOUNT", width=250)

        password_filed_description_label = ctk.CTkLabel(form_frame, text="Password:", font=("Helvetica", 14))
        password_entry = ctk.CTkEntry(form_frame, placeholder_text="PASSWORD", width=250)

        casual_button = ctk.CTkButton(
            form_frame, 
            text="Login", 
            fg_color="darkgreen",
            command=lambda: self.login_ctrl.login(username=account_entry.get(), password=password_entry.get())
        )

        title_label .pack(pady=(40, 24))
  
        form_frame.pack()
        account_field_description_label.pack(pady=(0, 4), anchor="w")
        account_entry.pack(pady=(0, 24))
        password_filed_description_label.pack(pady=(0, 4), anchor="w")
        password_entry.pack(pady=(0, 24))
        casual_button.pack()


