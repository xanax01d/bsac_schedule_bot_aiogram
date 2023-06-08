import sqlite3
from configs.groups import dict1
class BotDB:
    #подключаем базу
    def __init__(self,base):
        self.con = sqlite3.connect(base)
        self.cur = self.con.cursor() 
    #создаем нужные базы в боте
    def create_bases(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users_group(
	        user_id INTEGER PRIMARY KEY NOT NULL,
	        user_group TEXT,
            username TEXT,
            user_fn TEXT
	    )""")
        self.con.commit()
    #обновляем расписание(в будущем)
    #добавляем пользователя
    def add_user(self,user_id,user_group,username,user_fn):
        self.cur.execute("INSERT or REPLACE INTO 'users_group' VALUES (?,?,?,?)",(user_id,user_group,username,user_fn))
        return self.con.commit()
    #получаем расписание
    def get_schedule(self,user_id,day):
        self.cur.execute("SELECT user_group FROM users_group WHERE user_id =  ?",(user_id,))
        group_row = self.cur.fetchall()
        group = '' + group_row[0][0]
        table = dict1.get(group)
        self.cur.execute(f"SELECT sc FROM {table} WHERE day = ?",(day,))
        return self.cur.fetchall()[0][0]
    def close(self):
        self.con.close()