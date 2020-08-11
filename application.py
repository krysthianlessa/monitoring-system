import tkinter as tk
from lab import Lab
from home_page import HomePage
from data_base import DataBase

class Application():

    __slots__ = ['_lab']
    
    def __init__(self):
        self._lab = Lab()

    def run(self):
        data_base = DataBase()
        print(data_base.create_table())
        root = tk.Tk(className="Simoni")
        root.geometry("300x250")
        root.resizable(False, False)
        home = HomePage(master=root, lab=self._lab)
        home.mainloop()