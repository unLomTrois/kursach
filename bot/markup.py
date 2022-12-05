from telebot import types


def start_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("Да", callback_data="cb_start_button"))
    return markup


def burner_count_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(types.InlineKeyboardButton("1", callback_data="cb_burner_count_1"))
    markup.add(types.InlineKeyboardButton("2", callback_data="cb_burner_count_2"))
    markup.add(types.InlineKeyboardButton("4", callback_data="cb_burner_count_4"))
    return markup


def burner_power_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(types.InlineKeyboardButton("1", callback_data="cb_burner_power_low"))
    markup.add(
        types.InlineKeyboardButton("1.75", callback_data="cb_burner_power_medium")
    )
    markup.add(types.InlineKeyboardButton("3", callback_data="cb_burner_power_high"))
    return markup
