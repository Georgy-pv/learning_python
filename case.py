"""
Кейс: Разрабтка модели СПА комплекса при отеле 5*
Задача: разрработать Телеграм-бота для записи на процедуры в СПА комплекс
Token: 1808675918:AAGRq28a2vtiPsUVJLei79D7SK6_xpRhmC8
Ссылка: t.me/SpaOkuraBot
"""

#       Алгоритм работы бота
"""
    1
Приветствие клиента, информация о боте. Кнопки для прочтения информации об услугах и прайс-лист:
-Массажи
-Бани
-Косметология
-Тренажёрный зал
-СПА программы
-Записаться
"""

"""
    2
Нажав кнопку "Записаться", предоставляется выбор услуг для брони:
-Массажи
-Бани
-Косметология
-Тренажёрный зал
-СПА программы
"""

"""
    4
После выбора услуги предоставляется на выбор месяц - нынешний или следующий
"""

"""
    5
После выбора месяца, выбор дня брони. (тут либо кнопками, либо тектсом сам пользователь забивает)
"""

"""
    6
Выбор времени, которое можно забронировать. Из google таблицы подгружается свободное время в этот день
"""

"""
    7
Запрос имени и номера телефона пользователя. Данные записываются в таблицу
"""



#--------Что нам для этого нужно?--------
"""
Google таблица
Библиотека requests 
Библиотека pyTelegramBotAPI 

"""
import requests
import pprint
import telebot
from telebot import types
from telebot.types import Message
# Переменная с ссылкой на API бота
BASE_URL = 'https://api.telegram.org/bot1808675918:AAGRq28a2vtiPsUVJLei79D7SK6_xpRhmC8/'
 
TOKEN = '1808675918:AAGRq28a2vtiPsUVJLei79D7SK6_xpRhmC8'
bot = telebot.TeleBot(TOKEN)

# Клавиатура
but_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('Кнопка 1')
item2 = types.KeyboardButton('Кнопка 2')

but_markup.add(item1, item2)


# Обработка команды /start
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Здравствуйте! \nЯ виртуальный администратор SPA салона Алексей!', reply_markup=but_markup)


# Кнопки для описания услуг
services_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
service1 = types.KeyboardButton('Массажи')
service2 = types.KeyboardButton('СПА Программы')
service3 = types.KeyboardButton('Бани/Хаммам')
service4 = types.KeyboardButton('Эксклюзивные терапии')
service5 = types.KeyboardButton('Уход за внешностью')
services_buttons.add(service1, service2, service3, service4, service5)

# Обработка команды /help
@bot.message_handler(commands=['help'])
def help_services(message):
    bot.send_message(message.chat.id, 'Предлагаю ознакомиться с нашими услугами', reply_markup=services_buttons)


@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)
bot.polling()
