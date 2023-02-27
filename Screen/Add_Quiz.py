import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from DataBase.Users import User
from DataBase.Quizzes import Quizzes
from DataBase.Questions import Questions


class Add_Quiz(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x600')
        self.title('Add quiz window')
        self.configure(bg="#008B8B")
        self.userdb = User()
        self.quizdb = Quizzes()
        self.quizid = 0

        self.create_gui()
        Button(self, text='Close', command=self.close).pack(expand=True, side=BOTTOM)

    def create_gui(self):
        # phase 1 button
        # Label "Quiz name"
        self.lbl_name_of_quiz = Label(self, width=20, text="Name of quiz", background="#66CDAA")
        self.lbl_name_of_quiz.place(x=10, y=50)
        # Entry "Name of quiz"
        self.entry_quiz_name = Entry(self, width=15, background="#66CDAA")
        self.entry_quiz_name.place(x=200, y=50)
        # Label "Amount of questions"
        self.lbl_amount_of_questions = Label(self, width=20, text="Amount of questions", background="#66CDAA")
        self.lbl_amount_of_questions.place(x=10, y=100)
        # Entry "Amount of questions"
        self.entry_amount_of_questions = Entry(self, width=15, background="#66CDAA")
        self.entry_amount_of_questions.place(x=200, y=100)
        # Button "Submit"
        self.btn_submit = Button(self, command=self.handle_add_user, width=25, background="#66CDAA", text="Submit")
        self.btn_submit.place(x=10, y=150)

        # self.btn_submit1 = Button(self, command=self.insert_questions(), width=25, background="#66CDAA",
        #                          text="Submit question")
        # self.btn_submit.place(x=10, y=250)


        # Button user_quizzes
        # self.button_user_quizzes = Button(self, command=self.handle_add_user(), text="Your quizzes")
        # self.lbl_user_firstname.place(x=100, y=200)
        # Label "Last 10 games"


    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.insert_quiz1(), args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def insert_quiz1(self):

        if len(self.entry_quiz_name.get()) == 0:
            messagebox.showerror("Please write a normal quiz name")
            return
        print("insert_quiz")
        arr = ["insert_quiz", self.entry_quiz_name.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.client_socket.send(str_insert.encode())
        data = self.parent.client_socket.recv(1024).decode()
        print(data)
        if data == "success inserting":
            arr1 = ["quiz_name", self.entry_quiz_name.get()]
            str_insert1 = ",".join(arr1)
            print(str_insert1)
            self.parent.client_socket.send(str_insert1.encode())
            data = self.parent.client_socket.recv(1024).decode()
            print(data)
            self.quizid = int(data)
            messagebox.showinfo(title="Success", message="Successful inserted")
            self.btn_submit.destroy()
            self.lbl_name_of_quiz.config(text="Question")
            self.lbl_amount_of_questions.config(text="Answer")
            self.entry_quiz_name.delete(0, END)
            self.entry_amount_of_questions.delete(0, END)
            self.btn_submit10 = Button(self, command=self.insert_questions, width=25, background="#66CDAA", text="Submit question")
            self.btn_submit10.place(x=10, y=150)

        else:
            messagebox.showinfo(title="Failed", message="Fail inserted")

    def insert_questions(self):
        print("working")
        if len(self.entry_quiz_name.get()) == 0:
            messagebox.showerror("Please write a normal question")
            return
        print("insert_question")
        arr = ["insert_question", self.entry_quiz_name.get(), self.entry_amount_of_questions.get(), self.quizid]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.client_socket.send(str_insert.encode())
        data = self.parent.client_socket.recv(1024).decode()
        print(data)
        self.entry_quiz_name.delete(0, END)
        self.entry_amount_of_questions.delete(0, END)


    # def open_user_quizzes(self):
    #     window = User_Quizzes(self)
    #     window.grab_set()
    #     self.withdraw()


    def close(self):
        self.parent.deiconify() #  show parent
        self.destroy() #  close and destroy this screen
