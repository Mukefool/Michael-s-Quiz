import socket
import threading

from DataBase.Users import User
from DataBase.Quizzes import Quizzes
from DataBase.Questions import Questions


class Server(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.count = 0
        self.quiz_id_for_questions = 0
        self.running = True
        self.userDb = User()
        self.quizDb = Quizzes()
        self.questionsDb = Questions()

    def start(self):
        try:
            print('server starting up on ip %s port %s' % (self.ip, self.port))
            # Create a TCP/IP socket
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((self.ip, self.port))
            self.sock.listen(3)

            while True:
                print('waiting for a new client')
                clientSocket, client_addresses = self.sock.accept()
                print('new client entered')
                clientSocket.send('Hello this is server'.encode())
                self.count += 1
                print(self.count)
                # implement here your main logic
                self.handleClient(clientSocket, self.count)

        except socket.error as e:
            print(e)

    def handleClient(self, clientSock, current):
        client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock, current))
          client_handler.start()

    def handle_client_connection(self, client_socket, current):
        not_crash = True
        print(not_crash)
        while self.running:

            while not_crash:
                try:
                    server_data = client_socket.recv(1024).decode('utf-8')
                    arr = server_data.split(",")
                    print(server_data)
                    #  Register
                    if arr[0] == "register" and len(arr) == 5:
                        print("register user")
                        print(arr)

                        server_data = self.userDb.insert_user(arr[1], arr[2], arr[3], arr[4])
                        print("server data:", server_data)

                        if server_data:
                            client_socket.send("success register".encode())

                        elif server_data:
                            client_socket.send("failed register".encode())
                    #  Login
                    elif arr[0] == "login" and len(arr) == 3:
                        print("login user")
                        print(arr)
                        server_data = self.userDb.isexist(arr[1], arr[2])
                        print("server data: ", server_data)
                        if server_data:
                            client_socket.send("True".encode())
                        elif not server_data:
                            client_socket.send("False".encode())
                    #  Inserting quiz from Add_Quiz
                    elif arr[0] == "insert_quiz" and len(arr) == 2:
                        print("inserting quiz")
                        print(arr)
                        server_data = self.quizDb.insert_quiz(arr[1])
                        print("server data", server_data)
                        if server_data:
                            client_socket.send("success inserting".encode())
                        elif server_data:
                            client_socket.send("falied inserting".encode())
                    #  Finding the quiz id by his name
                    elif arr[0] == "quiz_name":
                        print("searching quiz")
                        print(arr)
                        server_data = self.quizDb.return_quizid_by_quiz_name(arr[1])
                        print("server data now is : ", server_data)
                        if server_data:
                            print("checking")
                            client_socket.send(str(server_data).encode())
                        elif server_data:
                            print("Kabum")
                    #  Inserting questions from Add_Quiz
                    elif arr[0] == "insert_question":  # and len(arr) == 3:
                        print("inserting question")
                        print(arr)
                        server_data = self.questionsDb.insert_answer(arr[1], arr[2], arr[3])
                        print("server data", server_data)
                        if server_data:
                            client_socket.send("success inserting".encode())
                        elif server_data:
                            client_socket.send("falied inserting".encode())
                    #   Changing the quiz id
                    elif arr[0] == "change_quiz_id_on_server":
                        print("writing a new quiz id for questions")
                        print(arr)
                        self.quiz_id_for_questions = arr[1]
                        print("Now quiz id is: "+self.quiz_id_for_questions)
                        if self.quiz_id_for_questions == 0:
                            print("Quiz id still 0")
                        elif server_data:
                            print("Quiz id not a 0")
                    #   Receiving questions
                    elif arr[0] == "please_give_me_questions":
                        print("Giving the questions with answers")
                        server_data = self.questionsDb.return_question_by_quiz_id(self.quiz_id_for_questions)
                        print("server data is: ", server_data)
                        if server_data:
                            client_socket.send(server_data.encode())
                        elif server_data:
                            print("Failed giving")






                    # elif arr[0] == "get_all_users" and len(arr) == 1:
                    #     print("get_all_users")
                    #     server_data = self.userDb.select_all_users()
                    #     server_data = ",".join(server_data) # convert data to string
                    else:
                        server_data = "False"
                        print(server_data)
                except Exception as e:
                    print(e)
                    not_crash = False
                    break


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 4568
    s = Server(ip, port)
    s.start()
