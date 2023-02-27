import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from DataBase.Users import User
from Screen.User_Quizzes import User_Quizzes
from PIL import ImageTk


class Profile(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x600')
        self.title('Profile window')
        self.configure(bg="#008B8B")
        self.userdb = User()

        self.create_gui()
        Button(self, text='Close', command=self.close).pack(expand=True, side=BOTTOM)

    def create_gui(self):
        # phase 1 button
        # Label "User Firstname"
        self.lbl_user_firstname = Label(self, width=10, text="User firstname", background="#66CDAA")
        self.lbl_user_firstname.place(relx=.3, rely=.2, anchor=E)
        # Label "User lastname"
        self.lbl_user_lastname = Label(self, width=10, text="User lastname", background="#66CDAA")
        self.lbl_user_lastname.place(relx=.3, rely=.3, anchor=E)
        # Label "User email"
        self.lbl_user_email = Label(self, width=10, text="User email", background="#66CDAA")
        self.lbl_user_email.place(relx=.3, rely=.4, anchor=E)
        # Button user_quizzes
        # self.button_user_quizzes = Button(self,text="Your quizzes", command=self.open_user_quizzes(), width=10, background="gray")
        # self.lbl_user_firstname.place(relx=.5, rely=.5, anchor=CENTER)
        # Label "Last 10 games"
        self.lbl_user_last_games = Label(self, width=10, text="Last 10 games", background="#66CDAA")
        self.lbl_user_last_games.place(relx=.5, rely=.2, anchor=W)

    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.open_user_quizzes, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def open_user_quizzes(self):
        window = User_Quizzes(self)
        window.grab_set()
        self.withdraw()

    # def open_donation(self):
    #     window = Donation(self)
    #     window.grab_set()
    #     self.withdraw()
    #
    # def open_quiz_by_id(self):
    #     window = Quiz_Screen(self)
    #     window.grab_set()
    #     self.withdraw()



    def close(self):
        self.parent.deiconify() #  show parent
        self.destroy() #  close and destroy this screen
