import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from DataBase.Users import User
from PIL import ImageTk


class Register(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x600')
        self.title('add user/register')
        self.configure(bg="#008B8B")
        self.userdb = User()

        self.create_gui()
        Button(self, text='Close', command=self.close).pack(expand=True, side=BOTTOM)

    def create_gui(self):
        # phase 1 button
        self.lbl_email = Label(self, width=10, text="email :", background="#66CDAA")
        self.lbl_email.place(x=10, y=50)
        self.email = Entry(self, width=20)
        self.email.place(x=100, y=50)

        self.lbl_password = Label(self, width=10, text="password :", background="#66CDAA")
        self.lbl_password.place(x=10, y=100)
        self.password = Entry(self, width=20)
        self.password.place(x=100, y=100)

        self.lbl_firstname = Label(self, width=10, text="firstname :", background="#66CDAA")
        self.lbl_firstname.place(x=10, y=150)
        self.firstname = Entry(self, width=20)
        self.firstname.place(x=100, y=150)

        self.lbl_secondname = Label(self, width=10, text="secondname :", background="#66CDAA")
        self.lbl_secondname.place(x=10, y=200)
        self.secondname = Entry(self, width=20)
        self.secondname.place(x=100, y=200)

        self.buttonPlus = Button(self, text="register", command=self.handle_add_user, width=20, background="#66CDAA")
        self.buttonPlus.place(x=10, y=250)

    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.register_user, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def register_user(self):

        if len(self.email.get()) == 0:
            messagebox.showerror("please write normal email", "Error")
            return
        print("register")
        arr = ["register", self.firstname.get(), self.secondname.get(), self.email.get(), self.password.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.client_socket.send(str_insert.encode())
        data = self.parent.client_socket.recv(1024).decode()
        print(data)

    def close(self):
        self.parent.deiconify() #  show parent
        self.destroy() #  close and destroy this screen
