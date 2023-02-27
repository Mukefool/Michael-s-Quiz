import sqlite3


class History(object):
    def __init__(self, tablename="Questions", history_id="History Id", quiz_id="quiz id", score="score",
                 time_of_the_game="Time of the game", user_id="user_id"):
        self.__tablename = tablename
        self.__history_id = history_id
        self.__quiz_id = quiz_id
        self.__score = score
        self.__time_of_the_game = time_of_the_game
        self.__user_id = user_id


        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.__tablename + "(" + self.__history_id + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.__quiz_id + " INTEGER    NOT NULL) "
        str += " " + self.__score + " INTEGER    NOT NULL) "
        str += " " + self.__time_of_the_game + " INTEGER    NOT NULL ,"
        str += " " + self.__user_id + " INTEGER    NOT NULL, "

        conn.execute(str)
        print("Table created successfully");
        conn.commit()
        conn.close()

    def get_table_name(self):
        return self.__tablename

    def select_all_historys(self):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully");
            str1 = "select*from " + self.__tablename
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_users = []
            for row in rows:
                str_rows = str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4])
                arr_users.append(str_rows)
            print(arr_users)
            return arr_users
        except:
            return False

    def insert_insert_history(self, quiz_id, score, time_of_the_game, user_id):
        try:
            conn = sqlite3.connect('test.db')
            str_insert = "INSERT INTO " + self.__tablename + " (" + self.__quiz_id + "," + self.__score + "," + self.__time_of_the_game + "," + self.__user_id + ") VALUES (" + "'" + quiz_id + "'" + "," + "'" + score + "'" + "," + "'" + time_of_the_game + "'" + "," + "'" + user_id + "');"
            print(str_insert)
            conn.execute(str_insert)
            conn.commit()
            conn.close()
            print("Record created successfully");
            return True
        except:
            print("Failed to insert user")
            return False


    def delete_history_by_id(self, history_id):
        try:
            conn = sqlite3.connect('test.db')
            str_delete = "DELETE  from " + self.__tablename + " where " + self.__history_id + "=" + "'" + str(
                history_id) + "'"
            print(str_delete)
            conn.execute(str_delete)
            conn.commit()
            conn.close()
            print("Record deleted successfully")
            return "Success"
        except:
            return "Failed to delete user"

    def return_history_by_id(self, history_id):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            strsql = "SELECT * from " + self.__tablename + " where " + self.__history_id + "=" + "'" + str(history_id) + "'"
            print(strsql)
            cursor = conn.execute(strsql)
            row = cursor.fetchone()
            if row:
                return [row[0], row[1], row[2], row[3]]
            else:
                print("Failed to find user")
                return False
            conn.commit()
            conn.close()
        except:
            return False

    def __str__(self):
        return "table  name is ", self.__tablename

# u=User()
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