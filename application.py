import tkinter as tk
from lab import Lab
from home_page import HomePage

class Application():
    __lab = Lab()

    def run(self):
        root = tk.Tk(className="Simoni")
        root.geometry("300x250")
        root.resizable(False, False)
        home = HomePage(master=root)
        home.mainloop()