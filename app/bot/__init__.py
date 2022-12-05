import telebot
from telebot import types

from app.bot.utils import calc_methane_max_v, is_number


token: str = "5816605116:AAGlXFDKUWBUYt56_yJIA4jnJcCu2_sCCbY"

tb = telebot.TeleBot(token)


@tb.message_handler(commands=["start"])
def start(message: types.Message):
    tb.send_message(
        message.chat.id,
        "Привет! Это калькулятор для расчёта потребления газа!",
    )
    sent = tb.send_message(
        message.chat.id,
        "Для начала укажите мощность газовой плиты (в кВт, например: 2.5)",
    )
    tb.register_next_step_handler(
        sent,
        get_power,
    )


def get_power(message: types.Message):
    if message.text is None:
        sent = tb.send_message(
            message.chat.id, "укажите мощность газовой плиты (в кВт, например: 2.5)"
        )
        tb.register_next_step_handler(sent, get_power)
        return

    power = message.text
    if not is_number(power):
        sent = tb.send_message(
            message.chat.id, "укажите мощность газовой плиты (в кВт, например: 2.5)"
        )
        tb.register_next_step_handler(sent, get_power)
        return

    power = float(power)
    H = 34.02
    KPD = 0.45

    v = round(calc_methane_max_v(power, H, KPD), 2)

    tb.reply_to(message, f"Максимальный расход: {v} куб.м/час")
