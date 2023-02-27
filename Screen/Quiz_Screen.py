import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from DataBase.Users import User
from DataBase.Quizzes import Quizzes
from DataBase.Questions import Questions


class Quiz_screen(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x600')
        self.title('Quiz window')
        self.configure(bg="#008B8B")
        self.userdb = User()
        self.quizdb = Quizzes()

        self.quizid = 0
        self.handle_add_user()

        Button(self, text='Close', command=self.close).pack(expand=True, side=BOTTOM)

    def create_gui(self):
        # phase 1 button
        # Label "Quiz name"
        self.lbl_name_of_quiz = Label(self, width=20, text="Name of quiz", background="#66CDAA")
        self.lbl_name_of_quiz.place(x=10, y=50)
        # Button "Submit"
        self.btn_submit = Button(self, command=self.handle_add_user, width=25, background="#66CDAA", text="Submit")
        self.btn_submit.place(x=10, y=150)

    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.making_a_quiz_window, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def making_a_quiz_window(self):
        request_to_the_server = "please_give_me_questions"
        self.parent.client.socket.send(request_to_the_server.encode())

        self.lbl_question = Label(self, width=20, text =)







    # def open_user_quizzes(self):
    #     window = User_Quizzes(self)
    #     window.grab_set()
    #     self.withdraw()


    def close(self):
        self.parent.deiconify() #  show parent
        self.destroy() #  close and destroy this screen
