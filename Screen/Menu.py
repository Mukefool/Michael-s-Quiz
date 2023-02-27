import threading
import tkinter
import socket
from tkinter import *
from Screen.Register import Register
from Screen.Login import Login
from tkinter import ttk
from PIL import ImageTk


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('606x600')
        self.title('Main Window')
        self.configure(bg="#008B8B")
        canvas = Canvas(width=400, height=400, bg='#008B8B')
        canvas.pack(expand=YES, fill=BOTH)
        image = ImageTk.PhotoImage(file="school_theme3.jpg")
        canvas.create_image(0, 0, image=image, anchor=NW)
        # place a button on the root window
        self.btn_register = Button(self, text='Register', command=self.open_register, background="#66CDAA")
        self.btn_register.place(x=50, y=50)

        self.loginbutton = Button(self, text='Login', command=self.open_login, background="#66CDAA")
        self.loginbutton.place(x=50, y=100)


        self.handle_thread_socket()

    def open_register(self):
        window = Register(self)
        window.grab_set()
        self.withdraw()

    def open_login(self):
        window = Login(self)
        window.grab_set()
        self.withdraw()

    def handle_thread_socket(self):
        client_handler = threading.Thread(target=self.create_socket, args=())
        client_handler.daemon = True
        client_handler.start()

    def create_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 4568))
        data = self.client_socket.recv(1024).decode()
        # print("data"+data)
        # print("hi", self.client_socket)


if __name__ == "__main__":
    app = App()
    app.mainloop()