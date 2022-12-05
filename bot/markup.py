from telebot import types


def start_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Да", callback_data="cb_start_button"))
    return markup


def what_is_power_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Что такое мощность плиты?", callback_data="cb_what_is_power"
        )
    )
    return markup
