import telebot
from telebot import types

from app.bot.utils import is_number
from app.calc import GasCalculator


token: str = "5816605116:AAGlXFDKUWBUYt56_yJIA4jnJcCu2_sCCbY"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message: types.Message):
    bot.send_message(
        message.chat.id,
        "Привет! Это калькулятор для расчёта потребления газа!",
    )
    sent = bot.send_message(
        message.chat.id,
        "Для начала укажите мощность газовой плиты (в кВт, например: 2.5)",
    )
    bot.register_next_step_handler(
        sent,
        get_power,
    )


def get_power(message: types.Message):
    if message.text is None:
        sent = bot.send_message(
            message.chat.id, "укажите мощность газовой плиты (в кВт, например: 2.5)"
        )
        bot.register_next_step_handler(sent, get_power)
        return

    power = message.text
    if not is_number(power):
        sent = bot.send_message(
            message.chat.id, "укажите мощность газовой плиты (в кВт, например: 2.5)"
        )
        bot.register_next_step_handler(sent, get_power)
        return

    power = float(power)
    # H = 34.02
    # KPD = 0.45

    calc = GasCalculator(power=power, price=0)

    v = round(calc.v_max, 2)

    bot.reply_to(message, f"Максимальный расход: {v} куб.м/час")
