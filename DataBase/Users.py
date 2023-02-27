import sqlite3


class User(object):

    def __init__(self, tablename="User", user_id="User_Id", user_firstname="firstname", user_secondname="secondname", user_email="email", user_password="password"):
        self.__tablename = tablename
        self.__user_id = user_id
        self.__user_firstname = user_firstname
        self.__user_secondname = user_secondname
        self.__user_email = user_email
        self.__user_password = user_password

        conn = sqlite3.connect('test1.db')
        print("Opened database successfully")

        strsql = f'CREATE TABLE IF NOT EXISTS {self.__tablename} ({self.__user_id} INTEGER PRIMARY KEY AUTOINCREMENT, '
        strsql += f'{self.__user_firstname} TEXT NOT NULL, '
        strsql += f'{self.__user_secondname} TEXT NOT NULL, '
        strsql += f'{self.__user_email} TEXT NOT NULL, '
        strsql += f'{self.__user_password} TEXT NOT NULL) '


        # str = "CREATE TABLE IF NOT EXISTS " + self.__tablename + " (" + self.__user_id + " " + "INTEGER PRIMARY KEY AUTOINCREMENT, "
        # str += self.__user_firstname + " TEXT NOT NULL, "
        # str += self.__user_secondname + " TEXT NOT NULL, "
        # str += self.__user_email + " TEXT NOT NULL, "
        # str += self.__user_password + " TEXT NOT NULL)"

        conn.execute(strsql)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def get_table_name(self):
        return self.__tablename

    def select_all_users(self):
        try:
            conn = sqlite3.connect('test1.db')
            print("Opened database successfully")
            str1 = "select*from " + self.__tablename
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_users = []
            for row in rows:
                str_rows = str(row[0]) + " " + row[1] + " " + row[2] + " " + row[3] + " " + str(row[4])
                arr_users.append(str_rows)
            print(arr_users)
            return arr_users
        except:
            return False

    def insert_user(self, user_firstname, user_secondname, user_email, user_password):
        try:
            conn = sqlite3.connect('test1.db')
            str_insert = "INSERT INTO " + self.__tablename + " (" + self.__user_firstname + ","+ self.__user_secondname\
                         + "," + self.__user_email + ","\
                         + self.__user_password + ") VALUES (" + "'" + user_firstname + "'" + ","\
                         + "'" + user_secondname + "'" + "," + "'" + user_email + "'" + "," + "'" + user_password + "');"
            print(str_insert)
            conn.execute(str_insert)
            conn.commit()
            conn.close()
            print("Record created successfully")
            return True
        except:
            print("Failed to insert user")
            return False

    def isexist(self, user_email, user_password):
        try:
            conn = sqlite3.connect('test1.db')
            print("Opened database successfully")
            strsql = "SELECT * from " + self.__tablename + " where " + self.__user_email + "=" + "'" + str(user_email) + "'" + " and " + self.__user_password + "=" + "'" + str(user_password) + "'"
            print(strsql)
            cursor = conn.execute(strsql)
            row = cursor.fetchone()
            if row:
                print("User has found")
                return True
            else:
                print("Failed to find user")
                return False
            conn.commit()
            conn.close()
        except:
            return False

    def delete_by_user_id(self, user_id):
        try:
            conn = sqlite3.connect('test1.db')
            str_delete = "DELETE  from " + self.__tablename + " where " + self.__user_id + "=" + "'"+str(user_id)+"'"
            print(str_delete)
            conn.execute(str_delete)
            conn.commit()
            conn.close()
            print("Record deleted successfully")
            return "Success"
        except:
            return "Failed to delete user"

    def return_user_by_email(self, user_email):
        try:
            conn = sqlite3.connect('test1.db')
            print("Opened database successfully")
            strsql = "SELECT * from " + self.__tablename + " where " + self.__user_email + "=" + "'" + str(user_email) + "'"
            print(strsql)
            cursor = conn.execute(strsql)
            row = cursor.fetchone()
            if row:
                return [row[0], row[1], row[2]]
            else:
                print("Failed to find user")
                return False
            conn.commit()
            conn.close()
        except:
            return False

    def __str__(self):
        return "table  name is ", self.__tablename


u=User()
#u.insert_user("u@x.com", "oron", 'yaron')
#u.insert_user("v@y.com", "dvidi", 'davidi')
#u.insert_user("t@a.com", "aba", 'origin')
#u.select_all_users()
#u.check_user_by_username("Asaf")
#u.delete_username("Asaf")
#u.check_user_by_username("Asaf")
#user=u.return_user_by_email('u@x.com')
#print(user[0])
#print(user)