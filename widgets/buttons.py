import customtkinter

class buttons(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure((0,1,2,3),weight=1)
        self.rowconfigure((0,1,2,3,4,5),weight=1)

        self.button_1 = customtkinter.CTkButton(self, text="Button 1",corner_radius=0, command=self.button_click).grid(row=0, column=0, sticky="nsew")
        self.button_2 = customtkinter.CTkButton(self, text="Button 2",corner_radius=0, command=self.button_click).grid(row=0, column=1, sticky="nsew")
        self.button_3 = customtkinter.CTkButton(self, text="Button 3",corner_radius=0, command=self.button_click).grid(row=0, column=2, sticky="nsew")
        self.button_4 = customtkinter.CTkButton(self, text="Button 4",corner_radius=0, command=self.button_click).grid(row=0, column=3, sticky="nsew")

        self.button_5 = customtkinter.CTkButton(self, text="Button 1",corner_radius=0, command=self.button_click).grid(row=1, column=0, sticky="nsew")
        self.button_6 = customtkinter.CTkButton(self, text="Button 2",corner_radius=0, command=self.button_click).grid(row=1, column=1, sticky="nsew")
        self.button_7 = customtkinter.CTkButton(self, text="Button 3",corner_radius=0, command=self.button_click).grid(row=1, column=2, sticky="nsew")
        self.button_8 = customtkinter.CTkButton(self, text="Button 4",corner_radius=0, command=self.button_click).grid(row=1, column=3, sticky="nsew")

        self.button_9 = customtkinter.CTkButton(self, text="Button 1",corner_radius=0, command=self.button_click).grid(row=2, column=0, sticky="nsew")
        self.button_10 = customtkinter.CTkButton(self, text="Button 2",corner_radius=0, command=self.button_click).grid(row=2, column=1, sticky="nsew")
        self.button_11 = customtkinter.CTkButton(self, text="Button 3",corner_radius=0, command=self.button_click).grid(row=2, column=2, sticky="nsew")
        self.button_12 = customtkinter.CTkButton(self, text="Button 4",corner_radius=0, command=self.button_click).grid(row=2, column=3, sticky="nsew")

        self.button_13 = customtkinter.CTkButton(self, text="Button 1",corner_radius=0, command=self.button_click).grid(row=3, column=0, sticky="nsew")
        self.button_14 = customtkinter.CTkButton(self, text="Button 2",corner_radius=0, command=self.button_click).grid(row=3, column=1, sticky="nsew")
        self.button_15 = customtkinter.CTkButton(self, text="Button 3",corner_radius=0, command=self.button_click).grid(row=3, column=2, sticky="nsew")
        self.button_16 = customtkinter.CTkButton(self, text="Button 4",corner_radius=0, command=self.button_click).grid(row=3, column=3, sticky="nsew")

        self.button_17 = customtkinter.CTkButton(self, text="Button 1",corner_radius=0, command=self.button_click).grid(row=4, column=0, sticky="nsew")
        self.button_18 = customtkinter.CTkButton(self, text="Button 2",corner_radius=0, command=self.button_click).grid(row=4, column=1, sticky="nsew")
        self.button_19 = customtkinter.CTkButton(self, text="Button 3",corner_radius=0, command=self.button_click).grid(row=4, column=2, sticky="nsew")
        self.button_20 = customtkinter.CTkButton(self, text="Button 4",corner_radius=0, command=self.button_click).grid(row=4, column=3, sticky="nsew")

        self.button_21 = customtkinter.CTkButton(self, text="Button 1",corner_radius=0, command=self.button_click).grid(row=5, column=0, sticky="nsew")
        self.button_22 = customtkinter.CTkButton(self, text="Button 2",corner_radius=0, command=self.button_click).grid(row=5, column=1, sticky="nsew")
        self.button_23 = customtkinter.CTkButton(self, text="Button 3",corner_radius=0, command=self.button_click).grid(row=5, column=2, sticky="nsew")
        self.button_24 = customtkinter.CTkButton(self, text="Button 4",corner_radius=0, command=self.button_click).grid(row=5, column=3, sticky="nsew")

    def button_click(self):
        print("button click")