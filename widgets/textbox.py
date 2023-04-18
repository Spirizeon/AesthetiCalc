from tkinter import *
import customtkinter


ENTRY_FONT=("Anonymous Pro",64)
class textbar(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.grid_columnconfigure(0,weight=1)
        self.textbar = customtkinter.CTkEntry(self,corner_radius=0,height=120,border_width=0,fg_color="#FFF3B0",font=ENTRY_FONT,text_color="#000000",justify="right").grid(row=0, column=0,pady=(60,0),sticky="ew")
        
        
    def getTextbar(self):
        state = self.text_bar.get("state")
        return state
