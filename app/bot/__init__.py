"""Модуль для работы с ботом"""

import telebot
from telebot import types

from app.bot.utils import is_number
from app.calc import GasCalculator


token: str = "5816605116:AAGlXFDKUWBUYt56_yJIA4jnJcCu2_sCCbY"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message: types.Message):
    """Входная точка для работы с ботом"""

    bot.send_message(
        message.chat.id,
        "Привет! Это калькулятор для расчёта потребления газа!",
    )
    bot.send_message(
        message.chat.id,
        "Для начала укажите мощность газовой плиты (в кВт, например: 2.5)",
    )
    # обработать следующее сообщение в функции get_power
    bot.register_next_step_handler(
        message,
        ask_for_power,
    )


def ask_for_power(message: types.Message):
    """Бот спрашивает пользователя, какая мощность у его плиты"""

    # если пользователь отправил не текст, а что-то другое, вроде картинки
    if message.text is None:
        # то напомнить ему, что нужно сделать
        sent = bot.send_message(
            message.chat.id, "укажите мощность газовой плиты (в кВт, например: 2.5)"
        )
        bot.register_next_step_handler(sent, ask_for_power)
        return

    power = message.text
    if not is_number(power):
        sent = bot.send_message(
            message.chat.id, "укажите мощность газовой плиты (в кВт, например: 2.5)"
        )
        bot.register_next_step_handler(sent, ask_for_power)
        return

    power = float(power)

    calc = GasCalculator(power=power, price=0)

    max_gas_usage_per_hour = round(calc.v_max, 2)

    bot.reply_to(message, f"Максимальный расход: {max_gas_usage_per_hour} куб.м/час")
    bot.send_message(
        message.chat.id, f"Стоимость топлива в год: {calc.price_per_year()} куб.м/час"
    )
