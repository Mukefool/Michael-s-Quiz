import sqlite3


class Quizzes(object):
    def __init__(self, tablename="Quizzes", quiz_id="Quiz_Id", quiz_name="Quiz_Name"):
        self.__tablename = tablename
        self.__quiz_id = quiz_id
        self.__quiz_name = quiz_name
        # self.__user_id = user_id
        # self.__popularity = popularity

        conn = sqlite3.connect('test1.db')
        print("Opened database successfully")

        str = f'CREATE TABLE IF NOT EXISTS {self.__tablename} ({self.__quiz_id} INTEGER PRIMARY KEY AUTOINCREMENT, '
        str += f'{self.__quiz_name} TEXT NOT NULL) '
        # str += " " + self.__popularity + " INTEGER    NOT NULL ,"

        conn.execute(str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def get_table_name(self):
        return self.__tablename

    def select_all_quizzes(self):
        try:
            conn = sqlite3.connect('test1.db')
            print("Opened database successfully")
            str1 = "select*from " + self.__tablename
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_users = []
            for row in rows:
                str_rows = str(row[0]) + " " + row[1] + " " + str(row[2]) + " " + str(row[3])
                arr_users.append(str_rows)
            print(arr_users)
            return arr_users
        except:
            return False

    def insert_quiz(self, quiz_name):
        try:
            conn = sqlite3.connect('test1.db')
            str_insert = "INSERT INTO " + self.__tablename + " (" + self.__quiz_name + ") VALUES ('" + quiz_name + "');"
            print(str_insert)
            conn.execute(str_insert)
            conn.commit()
            conn.close()
            print("Record created successfully")
            return True
        except:
            print("Failed to insert quiz")
            return False

    def delete_by_quiz_id(self, quiz_id):
        try:
            conn = sqlite3.connect('test1.db')
            str_delete = "DELETE  from " + self.__tablename + " where " + self.__quiz_id + "=" + "'" + str(
                quiz_id) + "'"
            print(str_delete)
            conn.execute(str_delete)
            conn.commit()
            conn.close()
            print("Record deleted successfully")
            return "Success"
        except:
            return "Failed to delete user"

    def return_quiz_by_quiz_id(self, quiz_id):
        try:
            conn = sqlite3.connect('test1.db')
            print("Opened database successfully")
            strsql = "SELECT * from " + self.__tablename + " where " + self.__quiz_id + "=" + "'" + str(quiz_id) + "'"
            print(strsql)
            cursor = conn.execute(strsql)
            row = cursor.fetchone()
            if row:
                return [row[0], row[1]]
            else:
                print("Failed to find quiz")
                return False
            conn.commit()
            conn.close()
        except:
            return False

    def return_quizid_by_quiz_name(self, quiz_name):
        try:
            conn = sqlite3.connect('test1.db')
            print("Opened database successfully")
            strsql = "SELECT * from " + self.__tablename + " where " + self.__quiz_name + "=" + "'" + quiz_name + "'"
            print(strsql)
            cursor = conn.execute(strsql)
            row = cursor.fetchone()
            if row:
                return row[0]

            else:
                print("Failed to find quiz")
                return False
            conn.commit()
            conn.close()
        except:
            return False

    def __str__(self):
        return "table  name is ", self.__tablename


Q = Quizzes()
# Q.insert_quiz("Lara1")
print(Q.return_quizid_by_quiz_name("Lara1"))
# u.insert_user("u@x.com", "oron", 'yaron')
# u.insert_user("v@y.com", "dvidi", 'davidi')
# u.insert_user("t@a.com", "aba", 'origin')
# u.select_all_users()
# u.check_user_by_username("Asaf")
# u.delete_username("Asaf")
# u.check_user_by_username("Asaf")
# user=u.return_user_by_email('u@x.com')
# print(user[0])
# print(user)