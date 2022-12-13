"""Модуль для работы с ботом"""

from telebot import TeleBot, types

from calc import GasCalculator
from utils import is_number

# Токен, который получаем из телеграм-бота BotFather
token: str = "5816605116:AAGlXFDKUWBUYt56_yJIA4jnJcCu2_sCCbY"

# Экземпляр бота, через этот объект отправляются сообщения
bot = TeleBot(token)

# @bot.message_handler делает так, что функция start обрабатывает сообщение пользователя
# start вызывается только на команду /start
@bot.message_handler(commands=["start"])
def start(message: types.Message):
    """Входная точка для работы с ботом"""

    bot.send_message(
        message.chat.id,
        "Привет! Это калькулятор для расчёта потребления газа!",
    )
    start_calc(message)


@bot.message_handler(commands=["calc"])
def start_calc(message: types.Message):
    """Просит пользователя ввести мощность"""
    bot.send_message(
        message.chat.id,
        "Для начала укажите мощность газовой плиты (в кВт, например: 2.5)",
    )
    # обработать следующее сообщение в функции ask_for_power
    bot.register_next_step_handler(
        message,
        ask_for_power,
    )


def ask_for_power(message: types.Message):
    """Бот спрашивает пользователя, какая мощность у его плиты"""

    # если пользователь отправил не текст, а что-то другое, вроде картинки
    if message.text is None:
        # то напомнить ему, что нужно сделать
        bot.send_message(
            message.chat.id, "укажите мощность газовой плиты (в кВт, например: 2.5)"
        )
        bot.register_next_step_handler(message, ask_for_power)
        return

    if not is_number(message.text):
        bot.send_message(
            message.chat.id, "укажите мощность газовой плиты (в кВт, например: 2.5)"
        )
        bot.register_next_step_handler(message, ask_for_power)
        return

    power = float(message.text)

    calc = GasCalculator(power=power, price=0)

    max_gas_usage_per_hour = round(calc.max_gas_usage, 2)

    bot.reply_to(
        message,
        f"Средний расход: {max_gas_usage_per_hour/2} куб.м/час\n"
        + f"Максимальный расход: {max_gas_usage_per_hour} куб.м/час\n\n"
        + "(если номинальный расход счётчика сильно меньше максимального расхода,"
        + "стоит задуматься о смене счётчика)",
    )
    bot.send_message(
        message.chat.id,
        "Теперь для расчёта затрат, укажите цену за 1 куб.м газа, например, 6.47",
    )
    bot.register_next_step_handler(message, ask_for_price, power)


def ask_for_price(message: types.Message, power: float):
    """Бот спрашивает пользователя, какая у него цена за газ"""

    # если пользователь отправил не текст, а что-то другое, вроде картинки
    if message.text is None:
        # то напомнить ему, что нужно сделать
        bot.send_message(
            message.chat.id,
            "Чтобы провести расчёт затрат, введите цену за куб.м газа, например, 6.47",
        )
        bot.register_next_step_handler(message, ask_for_power)
        return

    if not is_number(message.text):
        bot.send_message(
            message.chat.id,
            "Чтобы провести расчёт затрат, введите цену за куб.м газа, например, 6.47",
        )
        bot.register_next_step_handler(message, ask_for_power)
        return

    price = float(message.text)

    calc = GasCalculator(power=power, price=price)

    bot.reply_to(
        message,
        f"Стоимость топлива в день: {calc.price_per_day() / 2} руб.\n"
        + f"Стоимость топлива в месяц: {calc.price_per_month() / 2} руб.\n"
        + f"Стоимость топлива в год: {calc.price_per_year() / 2} руб.",
    )
    bot.send_message(message.chat.id, "Для нового расчёта используйте команду /calc")


def default_handler(_: types.Message):
    """Активирующая функция для стандартного обработчика, всегда вернёт True"""
    return True


# default_handler - то же самое, что и lambda message: True
@bot.message_handler(func=default_handler)
def default_command(message: types.Message):
    """Дефолтный обработчик, который обрабатывает сообщения после всех вычислений"""
    bot.send_message(message.chat.id, "Для расчёта используйте команду /calc")
