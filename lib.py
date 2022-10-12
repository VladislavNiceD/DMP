#lib for BPFD
import os
import time
import colorama
from colorama import Back, Style, Fore
import sqlite3
import random


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

version="2.0"
dmp="DMP"
dmp0="Discord Management Panel"

black=Fore.BLACK + Style.BRIGHT
warning=f"{Fore.YELLOW}[!]{Style.RESET_ALL}"
question=f"{Fore.RED}{Style.DIM}[?]{Style.RESET_ALL}"
error=f"{Fore.RED}[×]{Style.RESET_ALL}"
success=f"{Fore.GREEN}[✓]{Style.RESET_ALL}"
unkown_error="Неизвестная ошибка"
file_bot_not_exists="Файл bot.py не существует, создайте его в папке с этой программой"

main_menu=black + f"{dmp} | Version: {version}\n\n1. Создать нового бота\n2. Редактировать существующего бота\n3. Запустить бота\n4. Помощь\n: "
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
command_actions_input=black + "Добавьте действия к команде:\n1. Бан\n2. Отправить сообщение\n3. Рандомизировать число и отправить его\n4. Случайный выбор\n5. Добавить embed\n6. Отправить сообщение пользователю\n7. Управление сервером\n0. Отмена\n: "




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
				token_new=input(token_new_input)
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
							command_ban=True
							time.sleep(1)
							clear()
							print(successful)
					elif command_actions =="2":
						type=input(black + "Выберите тип сообщения\n1. Embed\n2. Обычный\n: ")
						if type =="1":
							a=input(black + "Вы уверены?\nПрежде чем делать отправку embed сообщения, обязательно добавьте сам embed, в команду, иначе бот ничего не отправит\n1. Ок\n2. Отмена\n: ")
							if a =="2":
								raise SystemExit
							with open('bot.py', 'r') as f:
						#"Добавьте действия к команде:\n1. Бан\n2. Кик\n3. Отправить сообщение\n4. Рандомизировать число и отправить его\n5. Случайный выбор\n6. Embed сообщение\n: "
								filedata=f.read()
							filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	await ctx.send(embed=embed)	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
							with open('bot.py', 'w') as f:
								f.write(filedata)
						elif type =="2":
							text=input(black + "Введите текст сообщения...\n: ")
							with open('bot.py', 'r') as f:
						#"Добавьте действия к команде:\n1. Бан\n2. Кик\n3. Отправить сообщение\n4. Рандомизировать число и отправить его\n5. Случайный выбор\n6. Embed сообщение\n: "
								filedata=f.read()
							filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	await ctx.send('{text}')	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
							with open('bot.py', 'w') as f:
								f.write(filedata)
						print(saving)
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
						title=input(black + "Введите заголовок embed сообщения...\n: ")
						description=input(black + "Введите описание embed сообщения...\n: ")
						print(saving)
						with open('bot.py', 'r') as f:
						#"Добавьте действия к команде:\n1. Бан\n2. Кик\n3. Отправить сообщение\n4. Рандомизировать число и отправить его\n5. Случайный выбор\n6. Embed сообщение\n: "
							filedata=f.read()
						filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	embed=discord.Embed(title='{title}', description='{description}')
	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
						with open('bot.py', 'w') as f:
							f.write(filedata)
							time.sleep(1)
							clear()
							print(successful)
					elif command_actions =="6":
						type=input(black + "Выберите тип сообщения\n1. Embed\n2. Обычный\n: ")
						if type =="1":
							a=input(black + "Вы уверены?\nПрежде чем делать отправку embed сообщения, обязательно добавьте сам embed, в команду, иначе бот ничего не отправит\n1. Ок\n2. Отмена\n: ")
							if a =="2":
								raise SystemExit
							with open('bot.py', 'r') as f:
						#"Добавьте действия к команде:\n1. Бан\n2. Кик\n3. Отправить сообщение\n4. Рандомизировать число и отправить его\n5. Случайный выбор\n6. Embed сообщение\n: "
								filedata=f.read()
							filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	await ctx.author.send(embed=embed)	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
							with open('bot.py', 'w') as f:
								f.write(filedata)
						elif type =="1":
							text=input(black + "Введите текст сообщения...\n: ")
							with open('bot.py', 'r') as f:
						#"Добавьте действия к команде:\n1. Бан\n2. Кик\n3. Отправить сообщение\n4. Рандомизировать число и отправить его\n5. Случайный выбор\n6. Embed сообщение\n: "
								filedata=f.read()
							filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	await ctx.author.send('{text}')	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
							with open('bot.py', 'w') as f:
								f.write(filedata)
						print(saving)
						time.sleep(1)
						clear()
						print(successful)
					elif command_actions =="7":
						clear()
						type=input(black + "Управление сервером\n1. Изменить аватарку\n2. Изменить название\n3. Создать роль\n4. Создать текстовый канал\n5. Создать категорию\n7. Создать голосовой канал\n9. Выйти с сервера\n0. Назад\n: ")
						if type =="0":
							pass
						elif type =="1":
							clear()
							print(warning + " Замените image.png на своё изображение!")
							time.sleep(1.5)
							with open('bot.py', 'r') as f:
								filedata=f.read()
							filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	with open('image.png', 'rb') as f:
		icon = f.read()
	await ctx.guild.edit(icon=icon)	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
							with open('bot.py', 'w') as f:
								f.write(filedata)
							print(saving)
							time.sleep(1)
							clear()
							print(successful)
						elif type =="2":
							clear()
							name=input(black + "Введите новое название сервера...\n: ")
							with open('bot.py', 'r') as f:
								filedata=f.read()
							filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	await ctx.guild.edit(name='{name}')	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
							with open('bot.py', 'w') as f:
								f.write(filedata)
							print(saving)
							time.sleep(1)
							clear()
							print(successful)
						elif type =="3":
							clear()
							name=input(black + "Введите название роли...\n: ")
							with open('bot.py', 'r') as f:
								filedata=f.read()
							filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	perms = discord.Permissions(xxxxcodexxxx=None)
	await ctx.guild.create_role(name='{name}', permissions=perms)	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
							with open('bot.py', 'w') as f:
								f.write(filedata)
							permissions=input(black + "Выберите права для роли...\n1. Добавлять реакции\n2. Администратор\n3. Прикреплять файлы\n4. Банить участников\n5. Изменять никнейм\n6. Присоединяться к голосовому каналу\n7. Создавать приглашения\n8. Создавать приватные ветки\n9. Создавать публичные ветки\n10. Отправлять участников подумать о своём поведении\n11. Embed ссылки\n12. Использовать эмодзи с других серверов\n13. Использовать стикеры с других серверов\n14. Кикать участников\n15. Управлять каналами\n16. Управлять эмодзи\n17. Управлять эмодзи и стикерами\n18. Управлять событиями\n19. Управлять сервером\n20. Управлять сообщениями\n21. Управлять никнеймами\n22. Управлять правами\n23. Управлять ролями\n24. Управлять ветками\n25. Управлять вебхуками\n26. Упоминать @everyone\n27. Модерировать участников\n28. Перемещать участников в голосовом канале\n29. Мутить участников в голосовом канале\n30. Приоретный режим в голосовом канале\n31. Читать историю сообщений\n32. Читать сообщения\n33. Попросить выступить на трибуне\n34. Отправлять сообщения\n35. Отправлять сообщения в ветках\n36. отправлять tts сообщения\n37. Говорить в голосовом канале\n38. Стримить\n39. Использовать команды приложения\n40. Использовать активности\n41. Просматривать журнал аудита\n42. Просматривать каналы\n: ")
							if permissions =="1":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'add_reactions=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="2":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'administrator=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="3":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'attach_files=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="4":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'ban_members=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="5":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'change_nickname=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="6":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'connect=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="7":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'create_instant_invite=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="8":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'create_private_threads=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="9":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'create_public_threads=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="10":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'deafen_members=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="11":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'embed_links=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="12":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'external_emojis=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="13":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'external_stickers=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="14":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'kick_members=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="15":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'manage_channels=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="16":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'manage_emojis=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="17":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'manage_emojis_and_stickers=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="18":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'manage_events=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="19":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'manage_guild=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="20":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'manage_messages=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="21":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'manage_nicknames=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="22":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'manage_permissions=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="23":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'manage_roles=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="24":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'manage_threads=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="25":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'manage_webhooks=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="26":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'mention_everyone=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="27":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'moderate_members=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="28":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'move_members=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="29":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'mute_members=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="30":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'priority_speaker=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="31":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'read_message_history=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="32":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'read_messages=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="33":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'request_to_speak=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="34":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'send_messages=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="35":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'send_messages_in_threads=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="36":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'send_tts_messages=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="37":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'speak=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="38":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'stream=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif commands =="39":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'use_application_commands=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="40":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'use_embedded_activities=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="41":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'view_audit_log=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
							elif permissions =="42":
								with open('bot.py', 'r') as f:
									filedata=f.read()
								filedata=filedata.replace(f'xxxxcodexxxx=None',f'view_channel=True, xxxxcodexxxx=None')
								with open('bot.py', 'w') as f:
									f.write(filedata)
									clear()
							print(saving)
							time.sleep(1)
							clear()
							print(successful)
						elif type =="4":
							clear()
							name = input(black + "Введите название текстового канала...\n: ")
							clear()
							with open('bot.py', 'r') as f:
								filedata=f.read()
							filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	await ctx.guild.create_text_channel(name='{name}')	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
							with open('bot.py', 'w') as f:
								f.write(filedata)
							print(saving)
							time.sleep(1)
							clear()
							print(successful)
						elif type =="5":
							clear()
							name=input(black + "Введите название категории...\n: ")
							with open('bot.py', 'r') as f:
								filedata=f.read()
							filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	await ctx.guild.create_category(name='{name}')	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
							with open('bot.py', 'w') as f:
								f.write(filedata)
							clear()
							print(saving)
							time.sleep(1)
							clear()
							print(successful)
						elif type =="6":
							clear()
							type=input(black + "Введите название интеграции...\n: ")
							with open('bot.py', 'r') as f:
								filedata=f.read()
							id = random.randint(123456789, 987654321)
							filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	await ctx.guild.create_integration(type='{type}', id='{id}')	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
							with open('bot.py', 'w') as f:
								f.write(filedata)
							clear()
							print(saving)
							time.sleep(1)
							clear()
							print(successful)
						elif type =="7":
							clear()
							name=input(black + "Введите название голосового канала...\n: ")
							with open('bot.py', 'r') as f:
								filedata=f.read()
							filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	await ctx.guild.create_voice_channel(name='{name}')	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
							with open('bot.py', 'w') as f:
								f.write(filedata)
							clear()
							print(saving)
							time.sleep(1)
							clear()
							print(successful)
						elif type =="8":
							clear()
							name=input(black + "Введите название форума...\n: ")
							with open('bot.py', 'r') as f:
								filedata=f.read()
							filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	await ctx.guild.create_forum(name='{name}')	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
							with open('bot.py', 'w') as f:
								f.write(filedata)
							clear()
							print(saving)
							time.sleep(1)
							clear()
							print(successful)
						elif type =="9":
							with open('bot.py', 'r') as f:
								filedata=f.read()
							filedata=filedata.replace(f'''#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36''',f'''
	await ctx.guild.leave()	#XhObmY9TbOlSgOmc52RiA70Mn8H4FsZi99Ytqy6BC1xOpm68GjT36
''')
							with open('bot.py', 'w') as f:
								f.write(filedata)
							clear()
							print(saving)
							time.sleep(1)
							clear()
							print(successful)
					elif command_actions =="0":
						clear()
				while True:
					command_creator()
	elif menu =="3":
		clear()
		print(warning + " Запускаем бота...")
		time.sleep(1)
		clear()
		try:
			os.system("pip install discord")
			os.system("python bot.py")
			clear()
		except:
			print(error + " Не удалось запустить бота")
	elif menu =="4":
		clear()
		help=input("В - Вопрос | О - Ответ\nВ: Для чего эта программа?\n-О: Данная программа поможет вам создать своего бота Discord не зная, как это сделать, при этом очень быстро.\n\nВ: Могу ли я редактировать созданную мною команду через программу?\n-О: Нет, вы не можете редактировать что либо в созданной вами команде, перед тем как завершить создание команды, обязательно подумайте, возможно стоит добавить что то ещё\n\nВ: Как получить токен бота?\n-О: Получить токен бота вы можете зарегистрировавшись на сайте discord developers, создав там своё приложение, перейдя во вкладку bot, нажимаете на add bot, и далее нажимаете на кнопку reset token, остаётся лишь скопировать токен, и вставить его когда вы будете создавать своего бота, токен автоматически сохранится вместе с остальными данными, для дальнейшего редактирования бота\n\nВ: Будет ли обновляться программа?\n-О: Да, она будет обновляться, но скорее всего не долго, т.к. у разработчика есть другие планы на будущее, однако не стоит волноваться, программа не будет удалена с GitHub, и будет далее функционировать без проблем, но если всё же вы нашли ошибку в коде, или у вас есть пожелания, то можете отправить письмо на почту: vlad1slav.nice@yandex.ru\n\n0. Назад\n: ")
		if help =="0":
			clear()
			print()
main()