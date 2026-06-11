import customtkinter as ctk
from presentation.controllers.login_ctrl import LoginCtrl
from presentation.views.login_ui import LoginUi
from utils.screen.screen_utils import screen_size_factory
from utils.view.base_view import BaseView

class AppNavigator(ctk.CTk):
    def __init__(self):
        super().__init__()
        screen_size = screen_size_factory()
        
        self.geometry(screen_size.get_screen_size_string())
        self.title("TBD")

        self.current_frame = None

        # Add new routh
        self.app_routh = {
            "login": lambda **kwargs: LoginUi(login_ctrl=LoginCtrl(), app=self, **kwargs)
        }

        self._show_fist_page()

        self.mainloop()
       
    def _show_fist_page(self):

        self.show_new_page(view_path="login")

    def show_new_page(self, view_path: str, **kwargs):

        if self.current_frame != None:
            self.current_frame.destroy()

        view_builder = self.app_routh[view_path]

        self.current_frame = view_builder(**kwargs)
        self.current_frame.pack(fill="both", expand=True)
        

