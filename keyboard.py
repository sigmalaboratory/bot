from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


button_1 = KeyboardButton('/ввм')
button_2 = KeyboardButton('/ввм_лр')
button_3 = KeyboardButton('/опос')
button_4 = KeyboardButton('/опос_лр')
button_5 = KeyboardButton('/тп')
button_6 = KeyboardButton('/тп_лр')
button_7 = KeyboardButton('/мок')
button_8 = KeyboardButton('/Філософія')
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard.row(button_1, button_2).row(button_3, button_4).row(button_5, button_6).row(button_7, button_8)


button_s = KeyboardButton('/start')
keyboard_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_start.add(button_s)