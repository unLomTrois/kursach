"""Тестирует модуль бота"""

from telebot import TeleBot
from bot import token


def test_token():
    """Тестирует, что токен объявлен, принадлежит к типу строки"""
    assert token is not None
    assert isinstance(token, str)
    assert token != ""


def test_bot_get_me():
    """Тестирует, что токен указан верно
    get_me() пытается подключиться к телеграму,
    но если токен не верный, то возвращается ошибка
    """
    test_bot = TeleBot(token)
    assert test_bot.get_me() is not None
