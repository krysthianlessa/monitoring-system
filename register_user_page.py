import tkinter as tk
import face_recognition
import cv2


class RegisterUserPage(tk.Frame):   
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.fonte = ("Verdana", "10")
        self.create_widgets()

    def create_widgets(self):
        self.container_title = tk.Frame(self)
        self.container_title["pady"] = 5
        self.container_title.pack()
        
        self.container_name = tk.Frame(self)
        self.container_name["pady"] = 5
        self.container_name.pack()

        self.container_last_name = tk.Frame(self)
        self.container_last_name["pady"] = 5
        self.container_last_name.pack()

        self.container_email = tk.Frame(self)
        self.container_email["pady"] = 5
        self.container_email.pack()

        self.container_photo = tk.Frame(self)
        self.container_photo["pady"] = 5
        self.container_photo.pack()

        self.container_buttons = tk.Frame(self)
        self.container_buttons["pady"] = 20
        self.container_buttons.pack()

        self.container_button_close = tk.Frame(self)
        self.container_button_close["pady"] = 10
        self.container_button_close.pack()

        self.title = tk.Label(self.container_title)
        self.title["text"] = "Cadastrar Usuário"
        self.title["font"] = ("Verdana", "14", "bold")
        self.title.pack()

        self.lbl_name = tk.Label(self.container_name, text="Nome:", font=self.fonte, width=10)
        self.lbl_name.pack(side=tk.LEFT)
    
        self.txt_name = tk.Entry(self.container_name)
        self.txt_name["width"] = 25
        self.txt_name["font"] = self.fonte
        self.txt_name.pack(side=tk.LEFT)

        self.lbl_last_name = tk.Label(self.container_last_name, text="Sobrenome:", font=self.fonte, width=10)
        self.lbl_last_name.pack(side=tk.LEFT)
    
        self.txt_last_name = tk.Entry(self.container_last_name)
        self.txt_last_name["width"] = 25
        self.txt_last_name["font"] = self.fonte
        self.txt_last_name.pack(side=tk.LEFT)

        self.lbl_email = tk.Label(self.container_email, text="E-mail:", font=self.fonte, width=10)
        self.lbl_email.pack(side=tk.LEFT)
    
        self.txt_email = tk.Entry(self.container_email)
        self.txt_email["width"] = 25
        self.txt_email["font"] = self.fonte
        self.txt_email.pack(side=tk.LEFT)

        self.lbl_photo = tk.Label(self.container_photo, text="Foto:", font=self.fonte, width=10)
        self.lbl_photo.pack(side=tk.LEFT)

        self.take_button = tk.Button(self.container_photo, text="Tirar", width=10, command=self.take_photo)
        self.take_button.pack(side=tk.LEFT)

        self.face_encodings = None

        self.insert_button = tk.Button(self.container_buttons, text="Inserir")
        self.insert_button.pack(side=tk.LEFT)

        self.change_button = tk.Button(self.container_buttons, text="Alterar")
        self.change_button.pack(side=tk.LEFT)

        self.delete_button = tk.Button(self.container_buttons, text="Excluir")
        self.delete_button.pack(side=tk.LEFT)

        self.close_button = tk.Button(self.container_button_close, text = 'Fechar', width = 25, command = self.master.withdraw)
        self.close_button.pack()

    
    def take_photo(self):
        camera = cv2.VideoCapture(0)

        while True:
            has_image, frame = camera.read()
            if has_image:
                cv2.imshow('Video', frame)
            else:
                print("No image!")
        
            if cv2.waitKey(1) & 0xFF == ord('q'):
                face_encodings = face_recognition.face_encodings(frame)[0]
                cv2.destroyAllWindows()
                break
        
        print(type(face_encodings))
    
    def insert(self):
        user = User(self.txt_name.get(), self.txt_last_name.get(), self.txt_email.get(), self.face_encodings)

    def change(self):
        pass

    def delete(self):
        pass
