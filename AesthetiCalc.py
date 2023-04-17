import customtkinter
from widgets.buttons import *
from widgets.textbox import *

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("350x550")
        self.title("calculator")
        # create 4x6 grid system
        self.grid_columnconfigure((0),weight=1)
        self.grid_rowconfigure((1),weight=1)
        
        

        self.entry = textbar(self).grid(row=0, column=0,padx=0, pady=0,sticky="nsew")

        self.btn = buttons(self).grid(row=1, column=0,padx=0, pady=0,sticky="nsew")

        
    


if __name__ == "__main__":
    app = App()
    app.mainloop()