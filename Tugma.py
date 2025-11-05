from aiogram import Bot, Dispatcher, types

def return_keyboards():
    kbs = [
        [types.KeyboardButton(text="Sherik kerak"), types.KeyboardButton(text="Ish joyi kerak")],
        [types.KeyboardButton(text="Xodim"), types.KeyboardButton(text="Ustoz kerak")],
        [types.KeyboardButton(text="Shogird kerak")]
    ]
    reply_kb = types.ReplyKeyboardMarkup(keyboard=kbs, resize_keyboard=True)
    return reply_kb

def confirmation_keyboard():
    kbs = [
        [types.KeyboardButton(text="✅ Ha, to'g'ri"), types.KeyboardButton(text="🔄 Qayta to'ldirish")],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kbs, resize_keyboard=True)