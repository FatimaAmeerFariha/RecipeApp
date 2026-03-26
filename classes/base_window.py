import customtkinter as ctk

class BaseWindow(ctk.CTk):
    def __init__(self, title="Recipe App"):
        super().__init__()
        self.title(title)
        self.geometry("650x500")