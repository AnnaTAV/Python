# ***
# Телефонный справочник

# - Добавьте контакт
# - Найти контакт
# - Удалить контакт 
# - Показать
# - *Получить файл


# - Фамилия
# - Имя
# - Телефон

# Иван
# Иванов
# 8(965)1478956
# ***
import telebot

# bot = telebot.TeleBot('')
database = {0: [["Имя", "Фамилия", "Телефон"]]}


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(commands=["add"])
def add(message):
    global current_command
    current_command = "add"
    bot.send_message(message.chat.id, "Введите текст")


@bot.message_handler(commands=["show"])
def show(message):
    if message.chat.id in database:
        bot.send_message(message.chat.id, database[message.chat.id])
    else:
        bot.send_message(message.chat.id, "Нет информации")
    pass


@bot.message_handler(commands=["find"])
def find(message):
    global current_command
    current_command = "find"
    bot.send_message(message.chat.id, "Введите текст для поиска")


@bot.message_handler(commands=["delete"])
def delete(message):
    global current_command
    current_command = "delete"
    bot.send_message(message.chat.id, "Введите текст для удаления")


@bot.message_handler(сщтеуте_ензуы=["text"])
def actions(message):
    global current_command
    if current_command == "add":
        if message.chat.id not in database:
           database[message.chat.id] = [["Имя", "Фамилия", "Телефон"]]
        database[message.chat.id].append(message.text.split('\n'))
    elif current_command == "find":
        pass
    elif current_command == "delete":
        pass
    else:
     bot.send_message(message.chat.id, "Выберете команду")


bot.polling()