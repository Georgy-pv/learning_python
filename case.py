"""
Кейс: Разрабтка модели СПА комплекса при отеле 5*
Задача: разрработать Телеграм-бота для записи на процедуры в СПА комплекс
Token: 1808675918:AAFON5SS_6FqE2asZHpp2PJ-6aSOGI_nP_I
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
from telebot.types import Message
# Переменная с ссылкой на API бота
BASE_URL = 'https://api.telegram.org/bot1808675918:AAFON5SS_6FqE2asZHpp2PJ-6aSOGI_nP_I/'
r = requests.get(f'{BASE_URL}getUpdates')
# Ответ в формате JSON
# pprint.pprint(r.json()['result'][-1]) 

# Оформление ответного сообщения
payload = {}
payload['chat_id'] = 1060475816
payload['text'] = 'Hello World'
# Отправление сообщения
r = requests.post(f'{BASE_URL}sendMessage', data = payload)

 
TOKEN = '1808675918:AAFON5SS_6FqE2asZHpp2PJ-6aSOGI_nP_I'
bot = telebot.TeleBot(TOKEN)
# преобразование сообщения пользователия в верхний регистр и отправка
@bot.message_handler(func=lambda message: True)
def upperLetter(message: Message):
    bot.reply_to(message, message.text.upper())

# Отслеживание изменений
bot.polling()
