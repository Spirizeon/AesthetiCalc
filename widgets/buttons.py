import customtkinter

class buttons(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure((0,1,2,3),weight=1)
        self.rowconfigure((0,1,2,3,4,5),weight=1)
        radius = 4
        
        f_color = '#FFBDE4'
        h_color = '#FFD2D0'
        #self._valid_tk_frame_attributes('-transparent','#FFD2D0')

        BUTTON_FONT = customtkinter.CTkFont(family="Major Mono Display", size=32)
        self.button_1 = customtkinter.CTkButton(self, text="%",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=0, column=0, sticky="nsew")
        self.button_2 = customtkinter.CTkButton(self, text="CE",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=0, column=1, sticky="nsew")
        self.button_3 = customtkinter.CTkButton(self, text="C",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=0, column=2, sticky="nsew")
        self.button_4 = customtkinter.CTkButton(self, text="X",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=0, column=3, sticky="nsew")

        self.button_5 = customtkinter.CTkButton(self, text="?",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=1, column=0, sticky="nsew")
        self.button_6 = customtkinter.CTkButton(self, text="?",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=1, column=1, sticky="nsew")
        self.button_7 = customtkinter.CTkButton(self, text="?",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=1, column=2, sticky="nsew")
        self.button_8 = customtkinter.CTkButton(self, text="/",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=1, column=3, sticky="nsew")

        self.button_9 = customtkinter.CTkButton(self, text="7",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=2, column=0, sticky="nsew")
        self.button_10 = customtkinter.CTkButton(self, text="8",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=2, column=1, sticky="nsew")
        self.button_11 = customtkinter.CTkButton(self, text="9",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=2, column=2, sticky="nsew")
        self.button_12 = customtkinter.CTkButton(self, text="x",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=2, column=3, sticky="nsew")

        self.button_13 = customtkinter.CTkButton(self, text="4",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=3, column=0, sticky="nsew")
        self.button_14 = customtkinter.CTkButton(self, text="5",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=3, column=1, sticky="nsew")
        self.button_15 = customtkinter.CTkButton(self, text="6",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=3, column=2, sticky="nsew")
        self.button_16 = customtkinter.CTkButton(self, text="-",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=3, column=3, sticky="nsew")

        self.button_17 = customtkinter.CTkButton(self, text="1",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=4, column=0, sticky="nsew")
        self.button_18 = customtkinter.CTkButton(self, text="2",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=4, column=1, sticky="nsew")
        self.button_19 = customtkinter.CTkButton(self, text="3",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=4, column=2, sticky="nsew")
        self.button_20 = customtkinter.CTkButton(self, text="+",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=4, column=3, sticky="nsew")

        self.button_21 = customtkinter.CTkButton(self, text="+/-",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=5, column=0, sticky="nsew")
        self.button_22 = customtkinter.CTkButton(self, text="0",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=5, column=1, sticky="nsew")
        self.button_23 = customtkinter.CTkButton(self, text=".",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=5, column=2, sticky="nsew")
        self.button_24 = customtkinter.CTkButton(self, text="=",font=BUTTON_FONT,border_width=0,border_spacing=0, fg_color=f_color,hover_color=h_color,text_color="#000000",corner_radius=radius, command=self.button_click).grid(padx=(0,1),pady=(0,1), row=5, column=3, sticky="nsew")
        BUTTON_FONT.configure(family="Major Mono Display")  # changes apply to button_1 and button_2
    def button_click(self):
        print("button click")
