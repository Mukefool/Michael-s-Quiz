import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from DataBase.Users import User
from Screen.Home import Home
from PIL import ImageTk
# from Screen.Menu import Menu


class Login(tkinter.Toplevel):
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
        # Email
        self.lbl_email = Label(self, width=10, text="email :", background="#66CDAA")
        self.lbl_email.place(x=10, y=50)

        self.email = Entry(self, width=20, background="#66CDAA")
        self.email.place(x=100, y=50)

        # Password
        self.lbl_password = Label(self, width=10, text="password :", background="#66CDAA")
        self.lbl_password.place(x=10, y=100)

        self.password = Entry(self, width=20, background="#66CDAA")
        self.password.place(x=100, y=100)

        # Login button
        self.loginbutton = Button(self, text='Login', command=self.handle_add_user, background="#66CDAA")
        self.loginbutton.place(x=10, y=200)

        # LoginWelcomeLabel
        self.welcomeloginlabel = Label(self, width=40, text="Please login", background="#66CDAA")
        self.welcomeloginlabel.place(x=10, y=250)





    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.loginuser, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def loginuser(self):
        if len(self.email.get()) == 0:
            messagebox.showerror("Error", "Please write something")
            return

        print("login")
        arr = ["login", self.email.get(), self.password.get()]
        str_insert = ",".join(arr)
        print(str_insert)

        self.parent.client_socket.send(str_insert.encode())
        data = self.parent.client_socket.recv(1024).decode()

        if data == "True":
            self.open_home()

        elif data == "False":
            self.welcomeloginlabel.config(text="Wrong password or email")
            print("False and works")

        print(data)

    def open_home(self):
        window = Home(self.parent)
        window.grab_set()
        self.destroy()


    def close(self):
        self.parent.deiconify()
        self.destroy()


# self.welcomeloginlabel.config(text="Hello user")
# print("True, and works")