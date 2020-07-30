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
    

if __name__ == "__main__":
    main()