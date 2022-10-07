#lib for BPFD
import os
import time
import colorama
from colorama import Back, Style, Fore
import sqlite3


debug_mode=False
show_token=False
show_all_information=False

if os.path.isfile("data.db"):
	conn=sqlite3.connect("data.db")
	cur=conn.cursor()
else:
	conn=sqlite3.connect("data.db")
	cur=conn.cursor()
	cur.execute("""CREATE TABLE "user" (
	"token" TEXT,
	"prefix" TEXT,
	"ready_text" TEXT,
	"help_text" TEXT,
	"id" INT,
	"debug_mode" TEXT,
	"show_token" TEXT,
	"show_all_information" TEXT
) """)


if show_token == True:
		cur.execute(f'SELECT token FROM user WHERE id=1')
		print(cur.fetchone())
		time.sleep(2)
if show_all_information == True:
		cur.execute(f'SELECT token, prefix, ready_text, help_text FROM user WHERE id=1')
		print(cur.fetchone())
		time.sleep(2)

def clear():
	os.system("clear||cls")

version="1.0"
dmp="DMP"
dmp0="Discord Management Panel"

black=Fore.BLACK + Style.BRIGHT
warning=f"{Fore.YELLOW}[!]{Style.RESET_ALL}"
question=f"{Fore.RED}{Style.DIM}[?]{Style.RESET_ALL}"
error=f"{Fore.RED}[×]{Style.RESET_ALL}"
success=f"{Fore.GREEN}[✓]{Style.RESET_ALL}"
unkown_error="Неизвестная ошибка"
file_bot_not_exists="Файл bot.py не существует, создайте его в папке с этой программой"

main_menu=black + f"{dmp} | Version: {version}\n\n1. Создать нового бота\n2. Редактировать существующего бота\n3. Настройки\n4. Помощь\n: "
name_input=black + "Введите название бота...\n: "
prefix_input=black + "Введите префикс бота...\n: "
text_on_ready_input=black + "Введите текст при старте бота...\n: "
text_help_input=black + "Введите текст команды help...\n: "
token_input=black + "Введите токен бота...\n: "
what_else_can_be_done_input=black + "Что можно сделать ещё:\n1. Добавить новую команду\n0. Пропустить\n: "

my_command_input=black + "Введите название вашей команды...\n: "

why_edit_input=black + "Что редактировать?\n1. Текст команды help\n2. Текст при запуске бота\n3. Префикс бота\n4. Токен бота\n5. Добавить новую команду\n0. Назад\n: "
help_new_text_input=black + "Введите новый текст команды help...\n: "
text_on_ready_new_input=black + "Введите новый текст при запуске бота...\n: "
prefix_new_input=black + "Введите новый префикс бота...\n: "
token_new_input=black + "Введите новый токен бота...\n: "
settings_input=black + "1. Режим разработчика\n2. Показывать токен бота при запуске\n3. Показывать все данные бота при запуске\n0. Назад\n: "
setting_debug_input=black + f"Статус: {debug_mode}\n1. Вкл\n2. Выкл\n0. Назад\n: "
setting_show_token_input=black + f"Статус: {show_token}\n1. Вкл\n2. Выкл\n0. Назад\n: "
setting_show_all_information_input=black + f"Статус: {show_all_information}\n1. Вкл\n2. Выкл\n0. Назад\n: "

saving=warning + f"{black} Сохранение..."
successful=success + f"{black} Успешно"
command_name_input=black + "Введите название команды...\n: "
command_actions_input=black + "Добавьте действия к команде:\n1. Бан\n2. Отправить сообщение\n3. Рандомизировать число и отправить его\n4. Случайный выбор\n5. Отправить embed сообщение\n0. Отмена\n: "




def main():
	menu=input(main_menu)
	if menu =="1":
		try:
			clear()
			name=input(name_input)
			clear()
			prefix=input(prefix_input)
			clear()
			text_on_ready=input(text_on_ready_input)
			clear()
			text_help=input(text_help_input)
			clear()
			token=input(token_input)
			clear()
			print(saving)
			time.sleep(0.5)
			cur.execute(f"INSERT INTO user VALUES ('{token}', '{prefix}', '{text_on_ready}', '{text_help}', 1, 'False', 'False', 'False')")
			conn.commit()
			with open("bot.py", "+r") as f:
				f.write(f"""
import discord#импорт модуля discord.py
from discord.ext import commands#импорт команд discord py
import random#импортируем модуль random для рандомизации

client = commands.Bot(command_prefix="{prefix}", intents=discord.Intents.all(), help_command=None)#префикс бота, и отключение стандартной команды help от discord py

@client.event#сообщаем о том, что внизу будет событие
async def on_ready():#если бот готов
	print("{text_on_ready}")#текст при запуске бота

@client.command()#сообщаем что внизу будет команда
async def help(ctx):#при команде {prefix}help
	await ctx.reply("{text_help}")#отправляем сообщение

#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36

client.run("{token}")#запускаем бота с токеном...""")
		except:
			raise
		clear()
		print(successful)
	elif menu =="2":
		clear()
		if not os.path.exists("bot.py"):
			print(error + f" {file_bot_not_exists}")
		else:
			menu=input(why_edit_input)
			if menu =="1":
				clear()
				help_new_text=input(help_new_text_input)
				clear()
				with open('bot.py', 'r') as file:
					filedata = file.read()
				for row in cur.execute("SELECT help_text FROM user WHERE id=1"):
					help_text=f"{row[0]}"
				filedata = filedata.replace(f'await ctx.reply("{help_text}")', f'await ctx.reply("{help_new_text}")')
				with open('bot.py', 'w') as file:
					file.write(filedata)
				cur.execute(f"UPDATE user SET help_text='{help_new_text}'")
				conn.commit()
				print(saving)
				time.sleep(1)
				clear()
				print(successful)
			elif menu =="2":
				text_on_ready_new=input(text_on_ready_new_input)
				clear()
				with open('bot.py', 'r') as file:
					filedata = file.read()
				for row in cur.execute("SELECT ready_text FROM user WHERE id=1"):
					ready_text=f"{row[0]}"
				filedata = filedata.replace(f'print("{ready_text}")', f'print("{text_on_ready_new}")')
				with open('bot.py', 'w') as file:
					file.write(filedata)
				cur.execute(f"UPDATE user SET ready_text='{text_on_ready_new}'")
				conn.commit()
				print(saving)
				time.sleep(1)
				clear()
				print(successful)
			elif menu =="3":
				clear()
				prefix_new=input(prefix_new_input)
				clear()
				with open('bot.py', 'r') as file:
					filedata = file.read()
				for row in cur.execute(f"SELECT prefix FROM user WHERE id=1"):
					prefix=f"{row[0]}"
				filedata = filedata.replace(f'client = commands.Bot(command_prefix="{prefix}", intents=discord.Intents.all(), help_command=None)', f'client = commands.Bot(command_prefix="{prefix_new}", intents=discord.Intents.all(), help_command=None)')
				with open('bot.py', 'w') as file:
					file.write(filedata)
				cur.execute(f"UPDATE user SET prefix='{prefix_new}' WHERE id=1")
				conn.commit()
				print(saving)
				time.sleep(1)
				clear()
				print(successful)
			elif menu =="4":
				clear()
				token_new=input(prefix_new_input)
				clear()
				with open('bot.py', 'r') as file:
					filedata = file.read()
				for row in cur.execute(f"SELECT token FROM user WHERE id=1"):
					token=f"{row[0]}"
				filedata = filedata.replace(f'client.run("{token}")', f'client.run("{token_new}")')
				with open('bot.py', 'w') as file:
					file.write(filedata)
				cur.execute(f"UPDATE user SET token='{token_new}' WHERE id=1")
				conn.commit()
				print(saving)
				time.sleep(1)
				clear()
				print(successful)
			elif menu =="5":
				clear()
				command_name=input(command_name_input)
				clear()
				print(saving)
				time.sleep(1)
				with open('bot.py', 'r') as f:
					filedata = f.read()
				filedata = filedata.replace('#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36', f'''
@client.command()
async def {command_name}(ctx):
				#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''')
				with open('bot.py', 'w') as f:
					f.write(filedata)
				clear()
				def command_creator():
					command_actions=input(command_actions_input)
					clear()
					if command_actions =="1":
						print(saving)
						with open('bot.py', 'r') as f:
						#"Добавьте действия к команде:\n1. Бан\n2. Кик\n3. Отправить сообщение\n4. Рандомизировать число и отправить его\n5. Случайный выбор\n6. Embed сообщение\n: "
							filedata=f.read()
						filedata=filedata.replace(f'''
@client.command()
async def {command_name}(ctx):''', f'''
@client.command()
async def {command_name}(ctx, member: discord.Member):
	await member.ban(reason="Ban")
	''')
						with open('bot.py', 'w') as f:
							f.write(filedata)
						time.sleep(1)
						clear()
						print(successful)
					elif command_actions =="2":
						text=input(black + "Введите текст, который нужно отправить...\n: ")
						print(saving)
						with open('bot.py', 'r') as f:
						#"Добавьте действия к команде:\n1. Бан\n2. Кик\n3. Отправить сообщение\n4. Рандомизировать число и отправить его\n5. Случайный выбор\n6. Embed сообщение\n: "
							filedata=f.read()
						filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	await ctx.send('{text}')
	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
						with open('bot.py', 'w') as f:
							f.write(filedata)
						time.sleep(1)
						clear()
						print(successful)
					
					elif command_actions =="3":
						value1=input(black + "Введите минимальное число...\n: ")
						value2=input(black + "Введите максимальное число...\n: ")
						print(saving)
						with open('bot.py', 'r') as f:
						#"Добавьте действия к команде:\n1. Бан\n2. Кик\n3. Отправить сообщение\n4. Рандомизировать число и отправить его\n5. Случайный выбор\n6. Embed сообщение\n: "
							filedata=f.read()
						filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	value=random.randint({value1}, {value2})
	await ctx.send(value)
	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
						with open('bot.py', 'w') as f:
							f.write(filedata)
							time.sleep(1)
							clear()
							print(successful)
					elif command_actions =="4":
					#random message
						value1=input(black + "Введите первое сообщение...\n: ")
						value2=input(black + "Введите второе сообщение...\n: ")
						print(saving)
						with open('bot.py', 'r') as f:
						#"Добавьте действия к команде:\n1. Бан\n2. Кик\n3. Отправить сообщение\n4. Рандомизировать число и отправить его\n5. Случайный выбор\n6. Embed сообщение\n: "
							filedata=f.read()
						filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	value=random.choice(['{value1}', '{value2}'])
	await ctx.send(value)
	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
						with open('bot.py', 'w') as f:
							f.write(filedata)
						time.sleep(1)
						clear()
						print(successful)
					elif command_actions =="5":
					#embed message
						title=input(black + "Введите заголовок сообщения...\n: ")
						description=input(black + "Введите описание (текст) сообщения...\n: ")
						print(saving)
						with open('bot.py', 'r') as f:
						#"Добавьте действия к команде:\n1. Бан\n2. Кик\n3. Отправить сообщение\n4. Рандомизировать число и отправить его\n5. Случайный выбор\n6. Embed сообщение\n: "
							filedata=f.read()
						filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	embed=discord.Embed(title='{title}', description='{description}')
	await ctx.send(embed=embed)
	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
						with open('bot.py', 'w') as f:
							f.write(filedata)
							time.sleep(1)
							clear()
							print(successful)
					elif command_actions =="0":
						clear()
				while True:
					command_creator()

	elif menu =="3":
		clear()
		while True:
			settings=input(settings_input)
			if settings =="1":
				clear()
				setting_debug=input(setting_debug_input)
				if setting_debug =="1":
					with open('lib.py', 'r') as file:
						filedata = file.read()
					for row in cur.execute("SELECT debug_mode FROM user WHERE id=1"):
						debug_mode=f"{row[0]}"
					filedata = filedata.replace(f'debug_mode={debug_mode}', f'debug_mode=True')
					with open('lib.py', 'w') as file:
						file.write(filedata)
					cur.execute(f"UPDATE user SET debug_mode='True'")
					conn.commit()
					clear()
					print(saving)
					time.sleep(1)
					clear()
					print(successful)
				elif setting_debug =="2":
					with open('lib.py', 'r') as file:
						filedata = file.read()
					for row in cur.execute("SELECT debug_mode FROM user WHERE id=1"):
						debug_mode=f"{row[0]}"
					filedata = filedata.replace(f'debug_mode={debug_mode}', f'debug_mode=False')
					with open('lib.py', 'w') as file:
						file.write(filedata)
					cur.execute(f"UPDATE user SET debug_mode='False'")
					conn.commit()
					clear()
					print(saving)
					time.sleep(1)
					clear()
					print(successful)
			elif settings =="2":
				clear()
				setting_show_token=input(setting_show_token_input)
				if setting_show_token =="1":
					with open('lib.py', 'r') as file:
						filedata = file.read()
					for row in cur.execute("SELECT show_token FROM user WHERE id=1"):
						show_token=f"{row[0]}"
					filedata = filedata.replace(f'show_token={show_token}', f'show_token=True')
					with open('lib.py', 'w') as file:
						file.write(filedata)
					cur.execute(f"UPDATE user SET show_token='True'")
					conn.commit()
					clear()
					print(saving)
					time.sleep(1)
					clear()
					print(successful)
				elif setting_show_token =="2":
					with open('lib.py', 'r') as file:
						filedata = file.read()
					for row in cur.execute("SELECT show_token FROM user WHERE id=1"):
						show_all_information=f"{row[0]}"
					filedata = filedata.replace(f'show_token={show_token}', f'show_token=False')
					with open('lib.py', 'w') as file:
						file.write(filedata)
					cur.execute(f"UPDATE user SET show_token='False'")
					conn.commit()
					clear()
					print(saving)
					time.sleep(1)
					clear()
					print(successful)
				elif setting_show_token =="0":
					break
			elif settings =="3":
				clear()
				setting_show_all_information=input(setting_show_all_information_input)
				clear()
				if setting_show_all_information =="1":
					with open('lib.py', 'r') as file:
						filedata = file.read()
					for row in cur.execute("SELECT show_all_information FROM user WHERE id=1"):
						show_all_information=f"{row[0]}"
					filedata = filedata.replace(f'show_all_information={show_all_information}', f'show_all_information=True')
					with open('lib.py', 'w') as file:
						file.write(filedata)
					cur.execute(f"UPDATE user SET show_all_information='True'")
					conn.commit()
					clear()
					print(saving)
					time.sleep(1)
					clear()
					print(successful)
				elif setting_show_all_information =="2":
					with open('lib.py', 'r') as file:
						filedata = file.read()
					for row in cur.execute("SELECT show_all_information FROM user WHERE id=1"):
						show_all_information=f"{row[0]}"
					filedata = filedata.replace(f'show_all_information={show_all_information}', f'show_all_information=False')
					with open('lib.py', 'w') as file:
						file.write(filedata)
					cur.execute(f"UPDATE user SET show_all_information='False'")
					conn.commit()
					clear()
					print(saving)
					time.sleep(1)
					clear()
					print(successful)
				
				elif setting_show_all_information =="0":
					break
			elif settings =="0":
				break
	elif menu =="4":
		clear()
		help=input("В - Вопрос | О - Ответ\nВ: Для чего эта программа?\n-О: Данная программа поможет вам создать своего бота Discord не зная, как это сделать, при этом очень быстро.\n\nВ: Могу ли я редактировать созданную мною команду через программу?\n-О: Нет, вы не можете редактировать что либо в созданной вами команде, перед тем как завершить создание команды, обязательно подумайте, возможно стоит добавить что то ещё\n\nВ: Как получить токен бота?\n-О: Получить токен бота вы можете зарегистрировавшись на сайте discord developers, создав там своё приложение, перейдя во вкладку bot, нажимаете на add bot, и далее нажимаете на кнопку reset token, остаётся лишь скопировать токен, и вставить его когда вы будете создавать своего бота, токен автоматически сохранится вместе с остальными данными, для дальнейшего редактирования бота\n\nВ: Будет ли обновляться программа?\n-О: Да, она будет обновляться, но скорее всего не долго, т.к. у разработчика есть другие планы на будущее, однако не стоит волноваться, программа не будет удалена с GitHub, и будет далее функционировать без проблем, но если всё же вы нашли ошибку в коде, или у вас есть пожелания, то можете отправить письмо на почту: vlad1slav.nice@yandex.ru\n\n0. Назад\n: ")
		if help =="0":
			clear()
			print()
main()