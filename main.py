import requests
from random import *
import random
import telebot
import datetime
from tkinter import *
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
with open('keys.txt', 'r', encoding='utf-8') as f:
    containt = f.read().split(', ')
    keyword = random.choice(containt)
    keyword = keyword[1:-1]
    print(keyword)
nations = {
     'usa':'США 🇺🇸',
     'ussr':'СССР ☭ / Россия 🇷🇺',
     'france':'Франция 🇫🇷',
     'japan':'Япония 🇯🇵',
     'china':'Китай 🇨🇳',
     'britain':'Британия 🇬🇧',
     'sweden':'Швеция 🇸🇪',
     'italy':'Италия 🇮🇹',
     'israel':'Израиль 🇮🇱',
     'germany':'Германия 🇩🇪'
}
bot = telebot.TeleBot('YOUR_TOKEN')
number = 0
@bot.message_handler(commands=['start']) 
def send_welcome(message):
    keyboard = ReplyKeyboardMarkup (resize_keyboard=True) 
    button1 = KeyboardButton("Техника") 
    button2 = KeyboardButton("Помощь с использованием")
    button3 = KeyboardButton("Написать жалобу на бота")
    keyboard.add(button1,button2,button3)
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
bot_status = '\n  Bot started \n'
print(bot_status)
with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write('\n'+bot_status)
# вызов информации сообщением/кнопкой
@bot.message_handler(func=lambda message: message.text == 'Техника')
def send_quest(message):
    new_ident = choice(vehicle_list)
    url_for_message = 'https://www.wtvehiclesapi.sgambe.serv00.net/api/vehicles/' + str(new_ident)
    response = requests.get(url_for_message)
    data = response.json()
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
    nation = data.get('country')
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
    bot_status = '\n  Bot turned off by user ' + final_chat_id + '\n'
    print(bot_status)
    with open('logs.txt', 'a', encoding='utf-8') as f:
            f.write('\n'+bot_status)
    bot.stop_polling()
# жалоба
@bot.message_handler(func=lambda message: message.text == 'Написать жалобу на бота')
def destroy_message(message):
    bot.send_message(message.chat.id, f'К сожалению, наш бот тоже неидеален, как и сама суть мироздания...\nЖалобу можно написать по адресу электронной почты создателя бота timofey.achieve@gmail.com')
# вместо /help
@bot.message_handler(func=lambda message: message.text == "Помощь с использованием")
def send_reaction(message):
    keyboard1 = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Страница проекта на GitHub", url="https://github.com/TheTutel/June-2025/tree/main")
    keyboard1.add(button1)
    bot.send_message(message.chat.id, 'С ботом можно взаимодействовать с помощью интерактивного меню внизу экрана\nКнопка "Техника" - отправить случайное изображение и информацию о технике на нем\nКнопка "Написать жалобу на бота" - ваше сообщение вскоре будет внимательно рассмотрено нашими администраторами', reply_markup=keyboard1)
bot.polling()
