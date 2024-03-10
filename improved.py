import telebot;
from telebot import types;
bot = telebot.TeleBot("ТВОЙ ТОКЕН");
per = 0
def progress(message):             # Я добавил эту функцию, чтобы игрок не мог, например, перескочить сразу на Кабинет,
    global per              # не пройдя предыдущие этапы. Просто суй ее туда, где надо изменить счетчик.
    if per == 0 and message.text == '/start': 
        per = 1    # Добавлять счетчик через elif
    elif per == 1 and message.text == 'Да': 
        per = 2
    elif per == 2 and message.text == 'Закончить допрос':
        per = 3
    elif per == 3 and message.text == 'В кабинет':
        per = 4
    elif per == 4 and message.text == 'РАЗГАДКА':
        per = 5
    elif per == 5 and message.text == 'Здесь еще какой-то прикольный текст, такой же, как и в том ифе, где функция прогресс':
        per = 6     # и так далее

@bot.message_handler(commands=['start'])
def start_messages(message):
    bot.send_message(message.from_user.id, f"Здравствуй, {message.from_user.username}. " 
                     "Добро пожаловать в игру 'Glimmer of Guilt'! Сегодня тебе предстоит разгадать дело " 
                     "о запутанном и страшном деле о любви... и убийстве. Если ты готов начать, напиши 'Да'.")
    photo = open('pic.jpg', 'rb') 
    bot.send_photo(message.chat.id, photo)
    photo.close()
    progress(message)

# Далее каждый игровой "блок" будет отдельной функцией для удобства, чтобы программа переходила из одного блока в другой
# в конце каждого блока должна быть функция следующего блока

@bot.message_handler(content_types=['text'])
def start_game(message):
    global per
    if per < 1:
        
        return      # Здесь return, чтобы он скипал все то, что есть в функции дальше, и не выводил это
    if message.text == "Да" and per == 1:
        bot.send_message(message.from_user.id, f"Город, год. Ты детектив по имени " 
                         f"{message.from_user.username}. Неделю назад тебе позвонили и сообщили об убийстве. " 
                         "Ты приехал туда. Увидел старый дом. С кем поговоришь первым? Напиши имя персонажа")
        progress(message)
    first_part(message)

def first_part(message):
    global per
    if per == 2:
        if message.text == "1":
            bot.send_message(message.from_user.id, "Он сказал тебе, что был в саду")
        elif message.text == "2":
            bot.send_message(message.from_user.id, "Он сказал тебе, что был в гостиной")
        elif message.text == "3":
            bot.send_message(message.from_user.id, "Он сказал тебе, что был в кабинете")
        elif message.text == "Закончить допрос":
            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
            btn1 = types.KeyboardButton(text="В кабинет")
            btn2 = types.KeyboardButton(text="В гостиную")
            btn3 = types.KeyboardButton(text="В сад")
            keyboard.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, text="После допроса ты решил пойти осмотреться. Куда пойдем?", reply_markup=keyboard)
            progress(message)
        else:
            
            return          # Здесь return, чтобы он скипал все то, что есть в функции дальше, и не выводил это
    razvilka(message)

def razvilka(message):
    global per
    if per == 3:
        if message.text == "В сад":
            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
            btn4 = types.KeyboardButton(text="В кабинет")
            btn5 = types.KeyboardButton(text="В гостиную")
            keyboard.add(btn4, btn5)
            bot.send_message(message.chat.id, text="Сад заперт на ключ. Пойди куда-нибудь еще", reply_markup=keyboard)
        elif message.text == "В гостиную":
            bot.send_message(message.chat.id, text="Направо или налево?")
        elif message.text == "Направо":
            bot.send_message(message.chat.id, text="Вас убили. Вы проиграли")
        elif message.text == "Налево":
            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
            btn6 = types.KeyboardButton(text="В сад")
            btn7 = types.KeyboardButton(text="В кабинет")
            keyboard.add(btn6, btn7)
            bot.send_message(message.chat.id, text="Вы вернулись обратно. Куда пойдем?", reply_markup=keyboard)
        elif message.text == "В сад":
            bot.send_message(message.chat.id, text="Вас убили. Вы проиграли")
        elif message.text == "В кабинет":
            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
            btn8 = types.KeyboardButton(text="Выглянуть в окно")
            btn9 = types.KeyboardButton(text="Осмотреть бумаги")
            keyboard.add(btn8, btn9)
            bot.send_message(message.chat.id, text="Ты зашел в кабинет. Там стоит стол, кресло, "
                            "на стене непонятная карта. Через окно видно сад, на прогулке в котором застрелили лорда. "
                            "На столе ворох непонятных бумаг и загадочный предмет.", reply_markup=keyboard)
            progress(message)
        else:
            return          # Здесь return, чтобы он скипал все то, что есть в функции дальше, и не выводил это
    cabinet(message)

def cabinet(message):
    global per
    if per == 4:
        if message.text == "Выглянуть в окно": 
            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
            btn9 = types.KeyboardButton(text="Осмотреть бумаги")
            keyboard.add(btn9)
            bot.send_message(message.chat.id, text="Ты смотришь на место преступления. Вокруг цветы и деревья. "
                            "И вдруг вдалеке промелькнула чья-то тень... "
                            "Надо поторопиться, тебе здесь явно не рады", reply_markup=keyboard)
        elif message.text == "Осмотреть бумаги": 
            bot.send_message(message.chat.id, text="На столе лежат бумаги - неоплаченные счета, "
                            "документы, заметки лорда. Полная пепельница и хаос. "
                            "Ты открыл выдвижной ящик и увидел странную шкатулку с загадочными надписями... "
                            "На боку шкатулки есть замок. Кажется, ее можно открыть только если знать код. Или нет? "
                            "Напиши 'Начать', чтобы приступить к загадке")
        elif message.text == "Начать": 
            keyboard = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Загадка", url='https://vk.com/timestreamcat')
            keyboard.add(button1)
            bot.send_message(message.chat.id, "ЗДЕСЬ ОБЯЗАТЕЛЬНО КАКОЙ-ТО ТЕКСТ", reply_markup=keyboard)
        elif message.text == "РАЗГАДКА":
            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
            btn10 = types.KeyboardButton(text="Открыть дверь в сад")
            keyboard.add(btn10)
            bot.send_message(message.chat.id, text="Вы открываете шкатулку, и там находится ключ и письмо '"
                            "Текст письма к убийце, по которому уже можно догадаться, кто убил лорда'", reply_markup=keyboard)
            progress(message)
        else:
            
            return          # Здесь return, чтобы он скипал все то, что есть в функции дальше, и не выводил это
    endgame(message)

def endgame(message):
    global per
    if per == 5:
        if message.text == "Открыть дверь в сад":
            bot.send_message(message.chat.id, text="Место преступления. Ты находишь улики и орудие убийства... "
                            "И кусок карты, которая висела в кабинете, ты заметил деталь, которую упустил до этого. "
                            "Найти место на карте? Напиши 'Отправить'.")
            photo = open('pic.jpg', 'rb') 
            bot.send_photo(message.chat.id, photo)
            photo.close()
        elif message.text == "Отправить":
            bot.send_location(message.from_user.id, 59.938924, 30.315311)
        else:
            
            return          # Здесь return, чтобы он скипал все то, что есть в функции дальше, и не выводил это


bot.infinity_polling()
