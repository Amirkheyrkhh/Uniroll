from tkinter import ttk

class RoundedButton(ttk.Button):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.button_style = ttk.Style()
        self.button_style.configure("RoundedButton.TButton",
                                    background="#ffffff",
                                    foreground="#000000",
                                    bordercolor="#000000",
                                    focusthickness=3,
                                    focuscolor="none",
                                    relief="flat",
                                    font=("Helvetica", 12))

        self.button_style.map("RoundedButton.TButton",
                              background=[("active", "light blue")],
                              relief=[("pressed", "groove"), ("active", "ridge")])

        self.configure(style="RoundedButton.TButton")