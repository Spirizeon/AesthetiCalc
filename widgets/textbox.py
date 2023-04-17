import customtkinter

class textbar(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure(0,weight=1)
        self.textbar = customtkinter.CTkEntry(self,corner_radius=0,height=70,border_width=0,).grid(row=0, column=0,pady=(50,0),sticky="ew")

    def getTextbar(self):
        state = self.text_bar.get("state")
        return state