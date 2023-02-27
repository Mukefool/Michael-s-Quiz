import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from DataBase.Users import User


class User_Quizzes(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x600')
        self.title('User Quizzes window')
        self.userdb = User()

        self.create_gui()
        Button(self, text='Close', command=self.close).pack(expand=True, side = BOTTOM)

    def create_gui(self):
        # phase 1 button
        # Label "User Firstname"
        self.lbl_user_firstname = Label(self, width=10, text="text 1")
        self.lbl_user_firstname.place(x=10, y=50)
        # Label "User lastname"
        self.lbl_user_lastname = Label(self, width=10, text="text 2")
        self.lbl_user_lastname.place(x=10, y=100)
        # Label "User email"
        self.lbl_user_email = Label(self, width=10, text="text 3")
        self.lbl_user_email.place(x=10, y=150)
        # Button user_quizzes
        # self.button_user_quizzes = Button(self, command=self.handle_add_user(), text="Your quizzes")
        # self.lbl_user_firstname.place(x=100, y=200)
        # Label "Last 10 games"


    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.open_user_quizzes, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def open_user_quizzes(self):
        window = User_Quizzes(self)
        window.grab_set()
        self.withdraw()

    # def open_popular_quiz(self):
    #     window = Quiz_Window(self)
    #     window.grab_set()
    #     self.withdraw()
    #
    # def open_list_of_popular_quiz(self):
    #     window = List_Of_Popular_Quizzes(self)
    #     window.grab_set()
    #     self.withdraw()
    #
    # def open_add_quiz(self):
    #     window = Add_Quiz(self)
    #     window.grab_set()
    #     self.withdraw()
    #
    # def open_donation(self):
    #     window = Donation(self)
    #     window.grab_set()
    #     self.withdraw()
    #
    # def open_quiz_by_id(self):
    #     window = Quiz_Screen(self)
    #     window.grab_set()
    #     self.withdraw()
    # def open_profile(self):
    #     window = Profile(self)
    #     window.grab_set()
    #     self.withdraw()

    def close(self):
        self.parent.deiconify() #  show parent
        self.destroy() #  close and destroy this screen
