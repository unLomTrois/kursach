import telebot
from telebot import types

from bot.markup import start_markup, what_is_power_markup
from bot.utils import calc_methane_max_v, clear_markup, is_number


token: str = "5816605116:AAGlXFDKUWBUYt56_yJIA4jnJcCu2_sCCbY"

tb = telebot.TeleBot(token)


@tb.message_handler(commands=["start"])
def start(message: types.Message):
    tb.send_message(
        message.chat.id,
        "Привет! Это калькулятор для расчёта потребления газа! Начнём?",
        reply_markup=start_markup(),
    )


@tb.callback_query_handler(func=lambda call: call.data == "cb_start_button")
def callback_inline_start(call: types.CallbackQuery):
    tb.answer_callback_query(call.id, "Хорошо!")
    clear_markup(tb, call)
    sent = tb.send_message(
        call.message.chat.id,
        "Для начала укажите мощность газовой плиты (в кВт, например: 2.5)",
        reply_markup=what_is_power_markup(),
    )
    tb.register_next_step_handler(
        sent,
        get_power,
    )


@tb.callback_query_handler(func=lambda call: call.data == "cb_what_is_power")
def answer_what_is_power(call: types.CallbackQuery):
    tb.answer_callback_query(call.id)
    clear_markup(tb, call)
    tb.send_message(
        call.message.chat.id,
        "Мощность плиты состоит из суммы мощностей всех горелок (конфорок)."
        + "Обычно это указывают в паспорте к плите, и его выдадут по требованию."
        + "Чтобы не решать проблему чрезмерного потребления газа, следует избегать продукции без паспорта.",
    )
    tb.send_message(
        call.message.chat.id,
        "Чтобы найти мощность плиты, найдите модель в интернете",
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
