"""Главный исполняемый модуль"""

from bot import bot

if __name__ == "__main__":
    try:
        print("бот успешно запущен, откройте телеграм")
        bot.polling()
    except Exception as e:
        print("кек", e)
