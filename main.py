import requests
from random import *
import random
import telebot
import datetime
from tkinter import *
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = 'your_bot_token'

with open('keys.txt', 'r', encoding='utf-8') as f:
    containt = f.read().split(', ')
    keyword = random.choice(containt)
    keyword = keyword[1:-1]
    print(keyword)

nations = {
     'usa':'США 🇺🇸', ##
     'ussr':'СССР ☭ / Россия 🇷🇺', ##
     'france':'Франция 🇫🇷',##
     'japan':'Япония 🇯🇵', ##
     'china':'Китай 🇨🇳', #
     'britain':'Британия 🇬🇧',##
     'sweden':'Швеция 🇸🇪 / Финляндия 🇫🇮',##
     'italy':'Италия 🇮🇹', #
     'israel':'Израиль 🇮🇱',##
     'germany':'Германия 🇩🇪'##
}

bot = telebot.TeleBot(BOT_TOKEN)
number = 0
@bot.message_handler(commands=['start']) 
def send_welcome(message):
    keyboard = ReplyKeyboardMarkup (resize_keyboard=True) 
    button1 = KeyboardButton("Техника🎲")
    button2 = KeyboardButton("Помощь с использованием❓")
    button3 = KeyboardButton("Написать жалобу на бота✍️")
    button_1 = KeyboardButton("Япония🇯🇵")
    button_2 = KeyboardButton("Германия🇩🇪")
    button_3 = KeyboardButton("Израиль🇮🇱")
    button_4 = KeyboardButton("США🇺🇸")
    button_5 = KeyboardButton("Швеция🇸🇪/Финляндия🇫🇮")
    button_6 = KeyboardButton("СССР☭/Россия🇷🇺")
    button_7 = KeyboardButton("Франция🇫🇷")
    button_8 = KeyboardButton("Китай🇨🇳")
    button_9 = KeyboardButton("Британия🇬🇧")
    button_10 = KeyboardButton("Италия🇮🇹")
    keyboard.add(button1,button2,button3,button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9,button_10)
    bot.send_message(message.chat.id, 'Привет! Этот бот может отправлять тебе разные изображения и информацию про технику из War Thunder. "Помощь с использованием"  Для начала нажми кнопку "Техника" внизу экрана.', reply_markup=keyboard) 

# нам эта константа похоже не нужна но пусть будет

CONSTANT = (number < 200)

# тут будет список техники из которой она будет случайно выбираться

# он заполняется пока бот стартует

vehicle_list = []

# номер страницы с техникой, начинается с 0, последняя страница 14, дальше пустые списки

number_url = 0

# это чисто чтобы знать что происходит

print('Updating current vehicle list...')

# хз загрузка актуального списка лень полностью комментировать. Короче он перебирает все словари в списках на страницах с 0 по 14

while True:
    if number_url != 15:
        url = 'https://www.wtvehiclesapi.sgambe.serv00.net/api/vehicles?limit=200&page=' + str(number_url)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            lenght = len(data)
            index = 0
            if lenght != 0:
                while True:
                    if index < lenght:
                        vehicle = data[index]
                        identifier_gotten = vehicle.get('identifier')
                        vehicle_list.append(identifier_gotten)
                        index = index + 1
                    else:
                        number_url += 1
                        break
    else: break

# после этого ботом можно пользоватся

bot_status = '\n  Bot started   '
print(bot_status)
time = datetime.datetime.now()
str_time = str(time)
with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write('\n'+bot_status+str_time+'\n\n'+keyword)

# вызов информации сообщением/кнопкой

@bot.message_handler(func=lambda message: message.text == 'Техника🎲')
def send_quest(message):
    new_ident = choice(vehicle_list)
    url_for_message = 'https://www.wtvehiclesapi.sgambe.serv00.net/api/vehicles/' + str(new_ident)
    response = requests.get(url_for_message)
    data = response.json()
    nation = data.get('country')
    image_list = data.get('images')
    image_url = image_list.get('image')
    time = datetime.datetime.now()
    bot.send_photo(message.chat.id, photo=image_url)
    ident_name = data.get('identifier')
    final_name = 'Идентификатор: ' + ident_name
    arcade_battle_rating = data.get('arcade_br')
    realistic_battle_rating = data.get('realistic_br')
    simulator_battle_rating = data.get('simulator_br')
    final_battle_rating = 'АБ: ' + str(float(arcade_battle_rating)) + '  РБ: ' + str(float(realistic_battle_rating)) + '  СБ: ' + str(float(simulator_battle_rating))
    flag_nation = nations.get(nation)
    print(ident_name)
    print(flag_nation)
    final_message_text = final_name + '\n' + final_battle_rating + '\n' + flag_nation
    bot.send_message(message.chat.id, final_message_text)
    final_chat_id = str(message.chat.id)
    print(final_chat_id)
    log_message = '\n\n' + final_chat_id + '\n' + ident_name + '\n' + str(time) + '\n' + final_name + '\n' + final_battle_rating
    with open('logs.txt', 'a', encoding='utf-8') as f:
       f.write(log_message)

# Япония

@bot.message_handler(func=lambda message: message.text == 'Япония🇯🇵')
def send_quest(message):
    while True:
        new_ident = choice(vehicle_list)
        url_for_message = 'https://www.wtvehiclesapi.sgambe.serv00.net/api/vehicles/' + str(new_ident)
        response = requests.get(url_for_message)
        data = response.json()
        nation = data.get('country')
        if nation == 'japan':
            break
    image_list = data.get('images')
    image_url = image_list.get('image')
    time = datetime.datetime.now()
    bot.send_photo(message.chat.id, photo=image_url)
    ident_name = data.get('identifier')
    final_name = 'Идентификатор: ' + ident_name
    arcade_battle_rating = data.get('arcade_br')
    realistic_battle_rating = data.get('realistic_br')
    simulator_battle_rating = data.get('simulator_br')
    final_battle_rating = 'АБ: ' + str(float(arcade_battle_rating)) + '  РБ: ' + str(float(realistic_battle_rating)) + '  СБ: ' + str(float(simulator_battle_rating))
    flag_nation = nations.get(nation)
    print(ident_name)
    print(flag_nation)
    final_message_text = final_name + '\n' + final_battle_rating + '\n' + flag_nation
    bot.send_message(message.chat.id, final_message_text)
    final_chat_id = str(message.chat.id)
    print(final_chat_id)
    log_message = '\n\n' + final_chat_id + '\n' + ident_name + '\n' + str(time) + '\n' + final_name + '\n' + final_battle_rating
    with open('logs.txt', 'a', encoding='utf-8') as f:
       f.write(log_message)

# Китай

@bot.message_handler(func=lambda message: message.text == 'Китай🇨🇳')
def send_quest(message):
    while True:
        new_ident = choice(vehicle_list)
        url_for_message = 'https://www.wtvehiclesapi.sgambe.serv00.net/api/vehicles/' + str(new_ident)
        response = requests.get(url_for_message)
        data = response.json()
        nation = data.get('country')
        if nation == 'china':
            break
    image_list = data.get('images')
    image_url = image_list.get('image')
    time = datetime.datetime.now()
    bot.send_photo(message.chat.id, photo=image_url)
    ident_name = data.get('identifier')
    final_name = 'Идентификатор: ' + ident_name
    arcade_battle_rating = data.get('arcade_br')
    realistic_battle_rating = data.get('realistic_br')
    simulator_battle_rating = data.get('simulator_br')
    final_battle_rating = 'АБ: ' + str(float(arcade_battle_rating)) + '  РБ: ' + str(float(realistic_battle_rating)) + '  СБ: ' + str(float(simulator_battle_rating))
    flag_nation = nations.get(nation)
    print(ident_name)
    print(flag_nation)
    final_message_text = final_name + '\n' + final_battle_rating + '\n' + flag_nation
    bot.send_message(message.chat.id, final_message_text)
    final_chat_id = str(message.chat.id)
    print(final_chat_id)
    log_message = '\n\n' + final_chat_id + '\n' + ident_name + '\n' + str(time) + '\n' + final_name + '\n' + final_battle_rating
    with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write(log_message)

# СССР/РФ

@bot.message_handler(func=lambda message: message.text == 'СССР☭/Россия🇷🇺')
def send_quest(message):
    while True:
        new_ident = choice(vehicle_list)
        url_for_message = 'https://www.wtvehiclesapi.sgambe.serv00.net/api/vehicles/' + str(new_ident)
        response = requests.get(url_for_message)
        data = response.json()
        nation = data.get('country')
        if nation == 'ussr':
            break
    image_list = data.get('images')
    image_url = image_list.get('image')
    time = datetime.datetime.now()
    bot.send_photo(message.chat.id, photo=image_url)
    ident_name = data.get('identifier')
    final_name = 'Идентификатор: ' + ident_name
    arcade_battle_rating = data.get('arcade_br')
    realistic_battle_rating = data.get('realistic_br')
    simulator_battle_rating = data.get('simulator_br')
    final_battle_rating = 'АБ: ' + str(float(arcade_battle_rating)) + '  РБ: ' + str(float(realistic_battle_rating)) + '  СБ: ' + str(float(simulator_battle_rating))
    flag_nation = nations.get(nation)
    print(ident_name)
    print(flag_nation)
    final_message_text = final_name + '\n' + final_battle_rating + '\n' + flag_nation
    bot.send_message(message.chat.id, final_message_text)
    final_chat_id = str(message.chat.id)
    print(final_chat_id)
    log_message = '\n\n' + final_chat_id + '\n' + ident_name + '\n' + str(time) + '\n' + final_name + '\n' + final_battle_rating
    with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write(log_message)


# США

@bot.message_handler(func=lambda message: message.text == 'США🇺🇸')
def send_quest(message):
    while True:
        new_ident = choice(vehicle_list)
        url_for_message = 'https://www.wtvehiclesapi.sgambe.serv00.net/api/vehicles/' + str(new_ident)
        response = requests.get(url_for_message)
        data = response.json()
        nation = data.get('country')
        if nation == 'usa':
            break
    image_list = data.get('images')
    image_url = image_list.get('image')
    time = datetime.datetime.now()
    bot.send_photo(message.chat.id, photo=image_url)
    ident_name = data.get('identifier')
    final_name = 'Идентификатор: ' + ident_name
    arcade_battle_rating = data.get('arcade_br')
    realistic_battle_rating = data.get('realistic_br')
    simulator_battle_rating = data.get('simulator_br')
    final_battle_rating = 'АБ: ' + str(float(arcade_battle_rating)) + '  РБ: ' + str(float(realistic_battle_rating)) + '  СБ: ' + str(float(simulator_battle_rating))
    flag_nation = nations.get(nation)
    print(ident_name)
    print(flag_nation)
    final_message_text = final_name + '\n' + final_battle_rating + '\n' + flag_nation
    bot.send_message(message.chat.id, final_message_text)
    final_chat_id = str(message.chat.id)
    print(final_chat_id)
    log_message = '\n\n' + final_chat_id + '\n' + ident_name + '\n' + str(time) + '\n' + final_name + '\n' + final_battle_rating
    with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write(log_message)


# Италия

@bot.message_handler(func=lambda message: message.text == 'Италия🇮🇹')
def send_quest(message):
    while True:
        new_ident = choice(vehicle_list)
        url_for_message = 'https://www.wtvehiclesapi.sgambe.serv00.net/api/vehicles/' + str(new_ident)
        response = requests.get(url_for_message)
        data = response.json()
        nation = data.get('country')
        if nation == 'italy':
            break
    image_list = data.get('images')
    image_url = image_list.get('image')
    time = datetime.datetime.now()
    bot.send_photo(message.chat.id, photo=image_url)
    ident_name = data.get('identifier')
    final_name = 'Идентификатор: ' + ident_name
    arcade_battle_rating = data.get('arcade_br')
    realistic_battle_rating = data.get('realistic_br')
    simulator_battle_rating = data.get('simulator_br')
    final_battle_rating = 'АБ: ' + str(float(arcade_battle_rating)) + '  РБ: ' + str(float(realistic_battle_rating)) + '  СБ: ' + str(float(simulator_battle_rating))
    flag_nation = nations.get(nation)
    print(ident_name)
    print(flag_nation)
    final_message_text = final_name + '\n' + final_battle_rating + '\n' + flag_nation
    bot.send_message(message.chat.id, final_message_text)
    final_chat_id = str(message.chat.id)
    print(final_chat_id)
    log_message = '\n\n' + final_chat_id + '\n' + ident_name + '\n' + str(time) + '\n' + final_name + '\n' + final_battle_rating
    with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write(log_message)


# Германия

@bot.message_handler(func=lambda message: message.text == 'Германия🇩🇪')
def send_quest(message):
    while True:
        new_ident = choice(vehicle_list)
        url_for_message = 'https://www.wtvehiclesapi.sgambe.serv00.net/api/vehicles/' + str(new_ident)
        response = requests.get(url_for_message)
        data = response.json()
        nation = data.get('country')
        if nation == 'germany':
            break
    image_list = data.get('images')
    image_url = image_list.get('image')
    time = datetime.datetime.now()
    bot.send_photo(message.chat.id, photo=image_url)
    ident_name = data.get('identifier')
    final_name = 'Идентификатор: ' + ident_name
    arcade_battle_rating = data.get('arcade_br')
    realistic_battle_rating = data.get('realistic_br')
    simulator_battle_rating = data.get('simulator_br')
    final_battle_rating = 'АБ: ' + str(float(arcade_battle_rating)) + '  РБ: ' + str(float(realistic_battle_rating)) + '  СБ: ' + str(float(simulator_battle_rating))
    flag_nation = nations.get(nation)
    print(ident_name)
    print(flag_nation)
    final_message_text = final_name + '\n' + final_battle_rating + '\n' + flag_nation
    bot.send_message(message.chat.id, final_message_text)
    final_chat_id = str(message.chat.id)
    print(final_chat_id)
    log_message = '\n\n' + final_chat_id + '\n' + ident_name + '\n' + str(time) + '\n' + final_name + '\n' + final_battle_rating
    with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write(log_message)


# Британия

@bot.message_handler(func=lambda message: message.text == 'Британия🇬🇧')
def send_quest(message):
    while True:
        new_ident = choice(vehicle_list)
        url_for_message = 'https://www.wtvehiclesapi.sgambe.serv00.net/api/vehicles/' + str(new_ident)
        response = requests.get(url_for_message)
        data = response.json()
        nation = data.get('country')
        if nation == 'britain':
            break
    image_list = data.get('images')
    image_url = image_list.get('image')
    time = datetime.datetime.now()
    bot.send_photo(message.chat.id, photo=image_url)
    ident_name = data.get('identifier')
    final_name = 'Идентификатор: ' + ident_name
    arcade_battle_rating = data.get('arcade_br')
    realistic_battle_rating = data.get('realistic_br')
    simulator_battle_rating = data.get('simulator_br')
    final_battle_rating = 'АБ: ' + str(float(arcade_battle_rating)) + '  РБ: ' + str(float(realistic_battle_rating)) + '  СБ: ' + str(float(simulator_battle_rating))
    flag_nation = nations.get(nation)
    print(ident_name)
    print(flag_nation)
    final_message_text = final_name + '\n' + final_battle_rating + '\n' + flag_nation
    bot.send_message(message.chat.id, final_message_text)
    final_chat_id = str(message.chat.id)
    print(final_chat_id)
    log_message = '\n\n' + final_chat_id + '\n' + ident_name + '\n' + str(time) + '\n' + final_name + '\n' + final_battle_rating
    with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write(log_message)


# Швеция & Финляндия

@bot.message_handler(func=lambda message: message.text == 'Швеция🇸🇪/Финляндия🇫🇮')
def send_quest(message):
    while True:
        new_ident = choice(vehicle_list)
        url_for_message = 'https://www.wtvehiclesapi.sgambe.serv00.net/api/vehicles/' + str(new_ident)
        response = requests.get(url_for_message)
        data = response.json()
        nation = data.get('country')
        if nation == 'sweden':
            break
    image_list = data.get('images')
    image_url = image_list.get('image')
    time = datetime.datetime.now()
    bot.send_photo(message.chat.id, photo=image_url)
    ident_name = data.get('identifier')
    final_name = 'Идентификатор: ' + ident_name
    arcade_battle_rating = data.get('arcade_br')
    realistic_battle_rating = data.get('realistic_br')
    simulator_battle_rating = data.get('simulator_br')
    final_battle_rating = 'АБ: ' + str(float(arcade_battle_rating)) + '  РБ: ' + str(float(realistic_battle_rating)) + '  СБ: ' + str(float(simulator_battle_rating))
    flag_nation = nations.get(nation)
    print(ident_name)
    print(flag_nation)
    final_message_text = final_name + '\n' + final_battle_rating + '\n' + flag_nation
    bot.send_message(message.chat.id, final_message_text)
    final_chat_id = str(message.chat.id)
    print(final_chat_id)
    log_message = '\n\n' + final_chat_id + '\n' + ident_name + '\n' + str(time) + '\n' + final_name + '\n' + final_battle_rating
    with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write(log_message)


# Израиль

@bot.message_handler(func=lambda message: message.text == 'Израиль🇮🇱')
def send_quest(message):
    while True:
        new_ident = choice(vehicle_list)
        url_for_message = 'https://www.wtvehiclesapi.sgambe.serv00.net/api/vehicles/' + str(new_ident)
        response = requests.get(url_for_message)
        data = response.json()
        nation = data.get('country')
        if nation == 'israel':
            break
    image_list = data.get('images')
    image_url = image_list.get('image')
    time = datetime.datetime.now()
    bot.send_photo(message.chat.id, photo=image_url)
    ident_name = data.get('identifier')
    final_name = 'Идентификатор: ' + ident_name
    arcade_battle_rating = data.get('arcade_br')
    realistic_battle_rating = data.get('realistic_br')
    simulator_battle_rating = data.get('simulator_br')
    final_battle_rating = 'АБ: ' + str(float(arcade_battle_rating)) + '  РБ: ' + str(float(realistic_battle_rating)) + '  СБ: ' + str(float(simulator_battle_rating))
    flag_nation = nations.get(nation)
    print(ident_name)
    print(flag_nation)
    final_message_text = final_name + '\n' + final_battle_rating + '\n' + flag_nation
    bot.send_message(message.chat.id, final_message_text)
    final_chat_id = str(message.chat.id)
    print(final_chat_id)
    log_message = '\n\n' + final_chat_id + '\n' + ident_name + '\n' + str(time) + '\n' + final_name + '\n' + final_battle_rating
    with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write(log_message)


# Франция

@bot.message_handler(func=lambda message: message.text == 'Франция🇫🇷')
def send_quest(message):
    while True:
        new_ident = choice(vehicle_list)
        url_for_message = 'https://www.wtvehiclesapi.sgambe.serv00.net/api/vehicles/' + str(new_ident)
        response = requests.get(url_for_message)
        data = response.json()
        nation = data.get('country')
        if nation == 'france':
            break
    image_list = data.get('images')
    image_url = image_list.get('image')
    time = datetime.datetime.now()
    bot.send_photo(message.chat.id, photo=image_url)
    ident_name = data.get('identifier')
    final_name = 'Идентификатор: ' + ident_name
    arcade_battle_rating = data.get('arcade_br')
    realistic_battle_rating = data.get('realistic_br')
    simulator_battle_rating = data.get('simulator_br')
    final_battle_rating = 'АБ: ' + str(float(arcade_battle_rating)) + '  РБ: ' + str(float(realistic_battle_rating)) + '  СБ: ' + str(float(simulator_battle_rating))
    flag_nation = nations.get(nation)
    print(ident_name)
    print(flag_nation)
    final_message_text = final_name + '\n' + final_battle_rating + '\n' + flag_nation
    bot.send_message(message.chat.id, final_message_text)
    final_chat_id = str(message.chat.id)
    print(final_chat_id)
    log_message = '\n\n' + final_chat_id + '\n' + ident_name + '\n' + str(time) + '\n' + final_name + '\n' + final_battle_rating
    with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write(log_message)


# выключение бота ключом

@bot.message_handler(func=lambda message: message.text == keyword)
def destroy_message(message):
    final_chat_id = str(message.chat.id)
    bot_status = '\n  Bot turned off by user ' + final_chat_id + ' at ' + str_time +'\n\n'
    print(bot_status)
    with open('logs.txt', 'a', encoding='utf-8') as f:
            f.write('\n'+keyword+'\n'+bot_status)
    bot.stop_polling()
    exit()


# жалоба

@bot.message_handler(func=lambda message: message.text == 'Написать жалобу на бота✍️')
def destroy_message(message):
    keyboard2 = InlineKeyboardMarkup()
    claim_button = InlineKeyboardButton("Перейти к написанию электронного письма", url="www.gmail.com")
    keyboard2.add(claim_button)
    bot.send_message(message.chat.id, f'К сожалению, наш бот тоже неидеален, как и сама суть мироздания...\n\nПочта создателя бота: timofey.achieve@gmail.com', reply_markup=keyboard2)


# вместо /help

@bot.message_handler(func=lambda message: message.text == "Помощь с использованием❓")
def send_reaction(message):
    keyboard1 = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Страница проекта на GitHub", url="https://www.example.com")
    keyboard1.add(button1)
    bot.send_message(message.chat.id, 'С ботом можно взаимодействовать с помощью интерактивного меню внизу экрана\nКнопка "Техника" - отправить случайное изображение и информацию о технике на нем\nКнопка "Написать жалобу на бота" - ваше сообщение вскоре будет внимательно рассмотрено нашими администраторами', reply_markup=keyboard1)

bot.polling()
