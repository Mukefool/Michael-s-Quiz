import threading
import tkinter
import socket
from tkinter import *
from tkinter import ttk, messagebox
from DataBase.Users import User
from Screen.Profile import Profile
from Screen.List_Of_Popular_Quizzes import List_Of_Popular_Quizzes
from Screen.Add_Quiz import Add_Quiz
from Screen.Quiz_Screen import Quiz_screen
from PIL import ImageTk


class Home(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x600')
        self.title('Home window')
        self.configure(bg="#008B8B")
        self.userdb = User()
        self.create_gui()
        Button(self, text='Close', command=self.close).pack(expand=True, side=BOTTOM)

    def create_gui(self):
        # phase 1 button
        # Label "Find quiz by id
        self.lbl_find_quiz_by_id = Label(self, width=10, text="Find quiz by id", background="#66CDAA")
        self.lbl_find_quiz_by_id.place(x=10, y=50)
        # Enrty for this
        self.enrty_find_quiz_by_id = Entry(self, width=20, background="#66CDAA")
        self.enrty_find_quiz_by_id.place(x=100, y=50)
        # Button to search it
        self.button_find_quiz_by_id = Button(self, text="Search", command=self.handle_add_user, width=20, background="#66CDAA")
        self.button_find_quiz_by_id.place(x=100, y=100)
        # Button Popular quizzes
        self.button_popular_quiz = Button(self, text="Popular quiz", command=self.handle_add_user, width=20, background="#66CDAA")
        self.button_popular_quiz.place(x=10, y=200)
        # Button List of Popular Quizzes
        self.button_list_of_popular_quizzes = Button(self, text="List of popular quizzes", command=self.open_list_of_popular_quiz, width=20, background="#66CDAA")
        self.button_list_of_popular_quizzes.place(x=150, y=200)
        # # Button Add Quiz
        self.button_add_quiz = Button(self, text="Add quiz", command=self.open_add_quiz, width=20, background="#66CDAA")
        self.button_add_quiz.place(x=10, y=250)
        # # Button Donation
        self.button_donation = Button(self, text="Donations", command=self.handle_add_user, width=20, background="#66CDAA")
        self.button_donation.place(x=150, y=250)
        # Button Profile
        self.button_profile = Button(self, text="Profile", command=self.open_profile, width=20, background="#66CDAA")
        self.button_profile.place(x=300, y=50)

    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.register_user, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def register_user(self):

        if len(self.email.get()) == 0:
            messagebox.showerror("please write normal email", "Error")
            return
        print("register")
        arr = ["register", self.email.get(), self.password.get(), self.firstname.get(), self.secondname.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.client_socket.send(str_insert.encode())
        data = self.parent.client_socket.recv(1024).decode()
        print(data)

    # def open_popular_quiz(self):
    #     window = Quiz_Window(self)
    #     window.grab_set()
    #     self.withdraw()

    def open_list_of_popular_quiz(self):
        window = List_Of_Popular_Quizzes(self)
        window.grab_set()
        self.withdraw()

    def open_add_quiz(self):
        window = Add_Quiz(self.parent)
        window.grab_set()
        self.withdraw()

    # def open_donation(self):
    #     window = Donation(self)
    #     window.grab_set()
    #     self.withdraw()

    def open_quiz_screen(self):
        quiz_id_to_server = str(self.enrty_find_quiz_by_id.get())
        arr1 = ["change_quiz_id_on_server", quiz_id_to_server]
        str_arr1 = ",".join(arr1)
        print(str_arr1)
        self.parent.client.sockect.send(str_arr1.encode())
        window = Quiz_screen(self.parent)
        window.grab_set()
        self.withdraw()

    def open_profile(self):
        window = Profile(self)
        window.grab_set()
        self.withdraw()

    def close(self):
        self.parent.deiconify()  # show parent
        self.destroy()  # close and destroy this screen
