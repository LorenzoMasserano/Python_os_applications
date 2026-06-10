import tkinter as tk

__root = tk.Tk()
__root.withdraw()

class ScreenSize():

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_screen_size_string(self) -> str:
        return f"{str(self.width)}x{str(self.height)}"
 
def screen_size_factory(width: int | None = None, height: int | None = None) -> ScreenSize:
    resulting_width = __root.winfo_screenwidth() if width == None else width
    resulting_height = __root.winfo_screenheight() if height == None else height
    
    return ScreenSize(width= resulting_width, height= resulting_height)


