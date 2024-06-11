import tkinter as tk
from tkinter import ttk

class PlaceholderEntry(ttk.Entry):
    def __init__(self, container, placeholder, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.placeholder = placeholder

        self.field_style = ttk.Style()
        self.field_style.configure("PE.TEntry",
                                   foreground="#616161",
                                   background="#ffffff",
                                   relief="flat")

        self.configure(style="PE.TEntry")
        self.insert(0, self.placeholder)
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)

    def _clear_placeholder(self, e):
        if self.get() == self.placeholder:
            self.delete(0, "end")

    def _add_placeholder(self, e):
        if self.get() == '':
            self.insert(0, self.placeholder)