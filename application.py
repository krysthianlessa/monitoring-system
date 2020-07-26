import tkinter as tk
from register_user import RegisterUser

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.container1 = tk.Frame(self)
        self.container1["pady"] = 15
        self.container1.pack()

        self.container2 = tk.Frame(self)
        self.container2["pady"] = 10
        self.container2.pack()

        self.container3 = tk.Frame(self)
        self.container3["pady"] = 10
        self.container3.pack()

        self.container4 = tk.Frame(self)
        self.container4["pady"] = 10
        self.container4.pack()

        self.title = tk.Label(self.container1)
        self.title["text"] = "Bem vindo ao SIMONI"
        self.title["font"] = ("Verdana", "14", "bold")
        self.title.pack()

        self.start = tk.Button(self.container2)
        self.start["text"] = "Iniciar o sistema"
        self.start["command"] = self.start_system
        self.start.pack()
        
        self.register = tk.Button(self.container3)
        self.register["text"] = "Cadastrar usuário"
        self.register["command"] = self.register_user
        self.register.pack()

        self.quit = tk.Button(self.container4, text="Sair", command=self.master.destroy)
        self.quit.pack()

    def start_system(self):
        print("Iniciando SIMONI ... ")
        self.newWindow = tk.Toplevel(self.master)
        self.app = StartSystem(self.newWindow)
    
    def register_user(self):
        print("Registrar usuário ... ")
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry("300x300")
        self.newWindow.resizable(False, False)
        self.krys = RegisterUser(self.newWindow)