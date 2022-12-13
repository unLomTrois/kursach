"""Тестирует модуль бота"""

from telebot import TeleBot
from bot import token

def test_token():
    """Тестирует, что токен объявлен, принадлежит к типу строки"""
    assert token is not None
    assert isinstance(token, str)
    assert token != ""


def test_bot():
    """Тестирует, что токен указан верно"""
    testbot = TeleBot(token)
    assert testbot.get_me() is not None
