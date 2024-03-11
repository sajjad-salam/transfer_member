import os,sqlite3
class database:
    def __init__(self) :
        if not os.path.isfile("database/data.db"):
            with sqlite3.connect("database/data.db") as connection:
                cursor = connection.cursor()	
                cursor.execute("CREATE TABLE IF NOT EXISTS vip (id TEXT)")
                cursor.execute("CREATE TABLE IF NOT EXISTS accounts (ses TEXT,number TEXT,id TEXT)")
                connection.commit()
    def AddAcount(self,ses,numbers,id):
        with sqlite3.connect("database/data.db") as connection:
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO accounts VALUES ('{ses}','{numbers}','{id}')")
            connection.commit()
    def accounts(self):
        list = []
        with sqlite3.connect("database/data.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM accounts")	
            entry = cursor.fetchall()
            for i in entry:
                list.append(i[0])
        return list
    def AddVip(self):
        pass