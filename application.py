import tkinter as tk
from lab import Lab
from home_page import HomePage

class Application():

    __slots__ = ['_lab']
    
    def __init__(self):
        self._lab = Lab()

    def run(self):
        root = tk.Tk(className="Simoni")
        root.geometry("300x250")
        root.resizable(False, False)
        home = HomePage(master=root, lab=self._lab)
        home.mainloop()