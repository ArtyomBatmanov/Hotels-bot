from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def request_contact():
    keyboard = ReplyKeyboardMarkup(True, True)
    keyboard.add(KeyboardButton('Отправить контакт', request_contact=True))
    return keyboard

