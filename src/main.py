# NAMA  : SAUL SAYERS
# NIM   : 13520094
# TASK 7 SELEKSI ASISTEN IRK

# FILE INI MERUPAKAN FILE UNTUK MENJALANKAN PROGRAM

import tkinter as tk
from mainpage import *

class App(tk.Tk):
    """Main application class

    Args:
        tk (_type_): class derived from tkinter's Tk class
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor for the class
        """
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(ConstantSize.WIDTH, ConstantSize.HEIGHT)
        self.maxsize(ConstantSize.WIDTH, ConstantSize.HEIGHT)
        self.title("13520094 - SAUL - NeedlesWunch Program")

        container = tk.Frame(self, bg = "white")
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        self.frames["MainPage"] = \
            MainPage(parent = container, controller = self, frames = self.frames)

        self.frames["MainPage"].grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame("MainPage")

    def show_frame(self, page_name):
        """Method to show a certain page

        Args:
            page_name (string): page name on the frames dictionary
        """
        frame = self.frames[page_name]
        frame.tkraise()


app = App()
app.mainloop()
