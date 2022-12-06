"""Модуль для работы с ботом"""

import telebot
from telebot import types

from calc import GasCalculator
from utils import is_number

# Токен, который получаем из телеграм-бота BotFather
token: str = "5816605116:AAGlXFDKUWBUYt56_yJIA4jnJcCu2_sCCbY"

# Экземпляр бота, через этот объект отправляются сообщения
bot = telebot.TeleBot(token)

# @bot.message_handler делает так, что функция start обрабатывает сообщение пользователя
# start вызывается только на команду /start
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

    bot.reply_to(
        message,
        f"Средний расход: {max_gas_usage_per_hour/2} куб.м/час\n"
        + f"Максимальный расход: {max_gas_usage_per_hour} куб.м/час\n\n"
        + "(если номинальный расход счётчика сильно меньше максимального расхода,"
        + "стоит задуматься о смене счётчика)",
    )
    sent = bot.send_message(
        message.chat.id,
        "Теперь для расчёта затрат, укажите цену за 1 куб.м газа, например, 6.47",
    )
    bot.register_next_step_handler(sent, ask_for_price, power)


def ask_for_price(message: types.Message, power: float):
    """Бот спрашивает пользователя, какая у него цена за газ"""

    # если пользователь отправил не текст, а что-то другое, вроде картинки
    if message.text is None:
        # то напомнить ему, что нужно сделать
        sent = bot.send_message(
            message.chat.id,
            "Чтобы провести расчёт затрат, введите цену за куб.м газа, например, 6.47",
        )
        bot.register_next_step_handler(sent, ask_for_power)
        return

    price = message.text

    if not is_number(price):
        sent = bot.send_message(
            message.chat.id,
            "Чтобы провести расчёт затрат, введите цену за куб.м газа, например, 6.47",
        )
        bot.register_next_step_handler(sent, ask_for_power)
        return

    price = float(price)

    calc = GasCalculator(power=power, price=price)

    bot.reply_to(
        message,
        f"Стоимость топлива в день: {calc.price_per_day() / 2} руб.\n"
        + f"Стоимость топлива в месяц: {calc.price_per_month() / 2} руб.\n"
        + f"Стоимость топлива в год: {calc.price_per_year() / 2} руб.",
    )
