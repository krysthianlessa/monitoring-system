import tkinter as tk
import face_recognition
import cv2
import numpy as np

# from lab import Lab
from application import Application

def main():
    root = tk.Tk(className="Simoni")
    root.geometry("300x250")
    root.resizable(False, False)
    app = Application(master=root)
    app.mainloop()
    
    # led = Lab()

    # choice = -1

    # while (choice != 3):
    #     print("#### Bem vindo ao SIMONI ####")
    #     print()
    #     print("1. Iniciar SIMONI")
    #     print("2. Cadastrar Usuário")
    #     print("3. Sair")
    #     print()
    #     choice = int(input("Escolha: "))
    #     print()
    
    #     if (choice == 1):
    #         while True:
    #             led.authenticate()
    #             led.to_monitor()
    #     if (choice == 2):
    #         print("1. Professor")
    #         print("2. Aluno")
    #         choice = int(input("Escolha: "))
    #         print()

    #         if (choice == 1):
    #             name = input("Digite o nome: ")
    #             department = input("Digite o departamento: ")
    #             face_encodings = led.get_face_encodings()
    #             user = Teacher(name, department, face_encodings)
    #             led.register_user(user)
    #             print("Professor adicionado com sucesso!")
    #         if (choice == 2):
    #             name = input("Digite o nome: ")
    #             registration_number = input("Digite a matricula: ")
    #             major = input("Curso: ")
    #             face_encodings = led.get_face_encodings()
    #             user = Student(name, registration_number, major, face_encodings)
    #             led.register_user(user)
    #             print("Aluno adicionado com sucesso!")


if __name__ == "__main__":
    main()