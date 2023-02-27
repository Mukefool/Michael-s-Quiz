import sqlite3


class Questions(object):
    def __init__(self, tablename="Questions", question_id="Question_Id", question="question", answer="answer", quiz_id="Quiz_Id"):
        self.__tablename = tablename
        self.__question_id = question_id
        self.__question = question
        self.__answer = answer
        self.__quiz_id = quiz_id
        conn = sqlite3.connect('test1.db')
        print("Opened database successfully")
        str = f'CREATE TABLE IF NOT EXISTS {self.__tablename} ({self.__question_id} INTEGER PRIMARY KEY AUTOINCREMENT, '
        str += f'{self.__question} TEXT NOT NULL, '
        str += f'{self.__answer} TEXT NOT NULL, '
        str += f'{self.__quiz_id} INTEGER NOT NULL) '


        conn.execute(str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def get_table_name(self):
        return self.__tablename

    def select_all_answers(self):
        try:
            conn = sqlite3.connect('test1.db')
            print("Opened database successfully")
            str1 = "select*from " + self.__tablename
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_users = []
            for row in rows:
                str_rows = str(row[0]) + " " + row[1] + " " + row[2] + " " + str(row[3]) + " " + str(row[4])
                arr_users.append(str_rows)
            print(arr_users)
            return arr_users
        except:
            return False

    def insert_answer(self, question, answer, quiz_id):
        try:
            conn = sqlite3.connect('test1.db')
            str_insert = "INSERT INTO " + self.__tablename + " (" + self.__question + "," + self.__answer +\
                          "," + self.__quiz_id + ") VALUES (" + "'" + question + "'" + "," + "'" + answer + "'" + " , " + "'" + quiz_id + "'" + ");"
            print(str_insert)
            conn.execute(str_insert)
            conn.commit()
            conn.close()
            print("Record created successfully")
            return True
        except Exception as e:
            print(e)
            return False

    def delete_question_by_id(self, question_id):
        try:
            conn = sqlite3.connect('test1.db')
            str_delete = "DELETE  from " + self.__tablename + " where " + self.__question_id + "=" + "'" + str(
                question_id) + "'"
            print(str_delete)
            conn.execute(str_delete)
            conn.commit()
            conn.close()
            print("Record deleted successfully")
            return "Success"
        except:
            return "Failed to delete user"

    def return_question_by_quiz_id(self, quiz_id):
        try:
            conn = sqlite3.connect('test1.db')
            print("Opened database successfully")
            strsql = "SELECT * from " + self.__tablename + " where " + self.__quiz_id + "=" + "'" + str(quiz_id) + "'"
            print(strsql)
            cursor = conn.execute(strsql)
            row = cursor.fetchall()
            arr_questions = []

            if row:
                print("aa")
                for row in row:
                    str_row = row[1] + "," + row[2]
                    arr_questions.append(str_row)
                    print(arr_questions)
                    return arr_questions
            else:
                print("Failed to find question")
                return False
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
            return False


Q=Questions()
# Q.insert_answer("Aboba?", "Baboby", "2")
# Q.return_question_by_quiz_id("2")
#Q.insert_answer("lopa", "sdsds")
# u.insert_user("u@x.com", "oron", 'yaron')
# u.select_all_users()
# u.check_user_by_username("Asaf")
# u.delete_username("Asaf")
# u.check_user_by_username("Asaf")
# user=u.return_user_by_email('u@x.com')
# print(user[0])
# print(user)