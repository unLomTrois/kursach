import telebot
from telebot import types

from bot.markup import burner_count_markup, burner_power_markup, start_markup


token: str = "5816605116:AAGlXFDKUWBUYt56_yJIA4jnJcCu2_sCCbY"

bot = telebot.TeleBot(token)


HELLO_TEXT = "Привет! Это калькулятор для расчёта потребления газа! Начнём?"


@bot.message_handler(commands=["start"])
def start(message: types.Message):
    bot.send_message(message.chat.id, HELLO_TEXT, reply_markup=start_markup())


@bot.callback_query_handler(func=lambda call: call.data == "cb_start_button")
def callback_inline_start(call: types.CallbackQuery):
    bot.answer_callback_query(call.id, "Хорошо!")
    bot.edit_message_reply_markup(
        call.message.chat.id, call.message.id, reply_markup=None
    )
    bot.send_message(
        call.message.chat.id,
        "Сколько конфорок у вашей плиты?",
        reply_markup=burner_count_markup(),
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("cb_burner_count_"))
def callback_inline_burner_count(call: types.CallbackQuery):
    # burner_count = int(call.data.split("cb_burner_count_")[1])
    bot.edit_message_reply_markup(
        call.message.chat.id, call.message.id, reply_markup=None
    )
    bot.send_message(
        call.message.chat.id,
        "Чудно! Теперь напишите или выберите мощность каждой конфорки",
    )
    sent = bot.send_message(
        call.message.chat.id,
        "Начнём с первой:",
        reply_markup=burner_power_markup(),
    )
    bot.send_message(
        call.message.chat.id,
        "(если не знаете, можете выбрать 1 из трёх кнопок, обычно самая маленькая около 1кВт, средняя 1.75, а мощная 3)",
    )
    bot.register_next_step_handler(sent, callback_inline_burner_power)


@bot.callback_query_handler(func=lambda call: call.data.startswith("cb_burner_power_"))
def callback_inline_burner_power(call: types.CallbackQuery):
    bot.edit_message_reply_markup(
        call.message.chat.id, call.message.id, reply_markup=None
    )
