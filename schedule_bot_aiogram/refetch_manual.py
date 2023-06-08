


#			█████████████████████████████████████████████████████████████████████████████   █
#			█████████████████████████████████████████████████████████   ██████   ████████   █
#			█   ███   ████   █████   █   ██████   █████   ███   ███   ██   ████   ███████   █
#			███  █   ███   ██   ███   ██   ██   ██   ████  █   ██   █████   ███   ███   █   █
#			████  █████   ███   ███   ██   █   ███   █████  █████   ██████   ██   ██  ███   █
#			██  ██   ██   ███   ███   ██   █   ███   ███  ██   ███   ████   ███   ██  ███   █
#			█   ███   ███   █    █    ██   ███   █    █   ███   █████    █████     ██   █   █
#			█████████████████████████████████████████████████████████████████████████████████



import sqlite3
import gspread
import week
from time import sleep
import os
from configs.groups import *
from week import cur_week
from configs.cfg import base, gst
os.system('cls')  #чистим консоль
print('.▄▄ ·  ▄▄·  ▄ .▄▄▄▄ .·▄▄▄▄  ▄• ▄▌▄▄▌  ▄▄▄ .  ▄• ▄▌ ▄▄▄··▄▄▄▄   ▄▄▄· ▄▄▄▄▄▄▄▄ .▄▄▄  ')
print('▐█ ▀. ▐█ ▌▪██▪▐█▀▄.▀·██· ██ █▪██▌██•  ▀▄.▀·  █▪██▌▐█ ▄███· ██ ▐█ ▀█ •██  ▀▄.▀·▀▄ █·')
print('▄▀▀▀█▄██ ▄▄██▀▀█▐▀▀▪▄▐█▪ ▐█▌█▌▐█▌██ ▪ ▐▀▀▪▄  █▌▐█▌ ██▀·▐█▪ ▐█▌▄█▀▀█  ▐█.▪▐▀▀▪▄▐▀▀▄ ')
print('▐█▄▪▐█▐███▌██▌▐▀▐█▄▄▌██. ██ ▐█▄█▌▐█▌ ▄▐█▄▄▌  ▐█▄█▌▐█▪·•██. ██ ▐█▪ ▐▌ ▐█▌·▐█▄▄▌▐█•█▌')
print(' ▀▀▀▀ ·▀▀▀ ▀▀▀ · ▀▀▀ ▀▀▀▀▀•  ▀▀▀ .▀▀▀  ▀▀▀    ▀▀▀ .▀   ▀▀▀▀▀•  ▀  ▀  ▀▀▀  ▀▀▀ .▀  ▀')
weekn = cur_week()
week = ''
dict2 = dict(zip(table_list , shs))
#ПРАВИТЬ СПИСКИ И ТАБЛИЦЫ ГРУПП В ФАЙЛЕ groups.py
gc = gspread.service_account(filename = gst) #токен для подключения библиотеки к созданному приложению
base = sqlite3.connect(base ,check_same_thread = False) #подключаем базу
cursor = base.cursor()
base.commit()
week = f'{weekn} неделя'

def deleting():
	for i in range(len(table_list)):
		tablename = table_list[i]
		cursor.execute(f'DROP TABLE IF EXISTS {tablename};')
		base.commit();
def create():
	for i in range(len(table_list)):
		tablename = table_list[i]
		cursor.execute(f'CREATE TABLE IF NOT EXISTS {tablename}('
					'day TEXT NOT NULL,'
					'sc TEXT'
					')')
		base.commit();
def save(gr,day,sc):
	if gr in gr_list:
		s = dict1.get(gr)
		cursor.execute(f"SELECT sc FROM {s} WHERE day = '{day}'")
		cursor.execute(f"INSERT INTO {s} VALUES (?,?);",(day,sc))
		base.commit();
def refetch():
	global sc
	for i in range(len(gr_list)):
		gr = gr_list[i]
		s = dict1.get(gr)
		sd = dict2.get(s)
		for i in range(len(days)):
			day = days[i];
			sh = gc.open_by_key(sd)
			cursor.execute(f"SELECT sc FROM {s} WHERE day = '{day}'")
			base.commit()
			data_row = cursor.fetchone()
			if data_row is None:
				if day == 'Понедельник':
					wc = 'C3:D8'
				elif day == 'Вторник':
					wc = 'C10:D15'
				elif day == 'Среда':
					wc = 'C17:D22'
				elif day == 'Четверг':
					wc = 'C24:D29'
				elif day == 'Пятница':
					wc = 'C31:D36'
				elif day == 'Суббота':
					wc = 'C38:D43'
				worksheet = sh.worksheet(f"{week}")
				d = worksheet.get(wc)
				p11 = d[0][0]
				p12 = d[0][1]
				p21 = d[1][0]
				p22 = d[1][1]
				p31 = d[2][0]
				p32 = d[2][1]
				p41 = d[3][0]
				p42 = d[3][1]
				p51 = d[4][0]
				p52 = d[4][1]
				p61 = d[5][0]
				p62 = d[5][1]
				if p11 == '!':
					p11 = 'Окно'
				if p12 == '!':
					p12 = 'Окно'
				if p21 == '!':
					p21 = 'Окно'
				if p22 == '!':
					p22 = 'Окно'
				if p31 == '!':
					p31 = 'Окно'
				if p32 == '!':
					p32 = 'Окно'
				if p41 == '!':
					p41 = 'Окно'
				if p42 == '!':
					p42 = 'Окно'
				if p51 == '!':
					p51 = 'Окно'
				if p52 == '!':
					p52 = 'Окно'
				if p61 == '!':
					p61 = 'Окно'
				if p62 == '!':
					p62 = 'Окно'
				s1 = f'1 пара (8:00 - 9:40)'
				s2 = f'2 пара (9:55 - 11:35)'
				s3 = f'3 пара (12:15 - 13:55)'
				s4 = f'4 пара (14:10 - 15:50)'
				s5 = f'5 пара (16:20 - 18:00)'
				s6 = f'6 пара (18:15 - 19:55)'
				if p11 == p12:
					if p11 == "Окно":
						s1 = ''
					else:
						s1 = f'{s1}\n{p11}\n'
				else:
					s1 = f'{s1}\n{p11} | {p12}\n'
				if p21 == p22:
					if p21 == "Окно":
						s2 = ''
					else:
						s2 = f'{s2}\n{p21}\n'
				else:
					s2 = f'{s2}\n{p21} | {p22}\n'
				if p31 == p32:
					if p31 == "Окно":
						s3 = ''
					else:
						s3 = f'{s3}\n{p31}\n'
				else:
					s3 = f'{s3}\n{p31} | {p32}\n'
				if p41 == p42:
					if p41 == "Окно":
						s4 = ''
					else:
						s4 = f'{s4}\n{p41}\n'
				else:
					s4 = f'{s4}\n{p41} | {p42}\n'
				if p51 == p52:
					if p51 == "Окно":
						s5 = ''
					else:
						s5 = f'{s5}\n{p51}\n'
				else:
					s5 = f'{s5}\n{p51} | {p52}\n'
				if p61 == p62:
					if p61 == "Окно":
						s6 = ''
					else:
						s6 = f'{s6}\n{p61}\n'
				else:
					s6 = f'{s6}\n{p61} | {p62}\n'
				sc = f'{s1}\n{s2}\n{s3}\n{s4}\n{s5}\n{s6}'
				if sc == '\n\n\n\n\n':
					sc = 'Пар нет'
				save(gr,day,sc)
				d.clear()
				sleep (5)
		print('The weekly schedule is saved for the group: ',gr)
		sleep(10)
deleting()
create()
refetch()