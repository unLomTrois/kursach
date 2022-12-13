"""Тестирует модуль utils"""

from utils import is_number


def test_is_number():
    """Тестирует на то, что строки с числами преобразуются к float"""
    assert is_number("1") is True
    assert is_number("1.0") is True
    assert is_number("1,0") is False
    assert is_number("abc") is False
    assert is_number("1.abc") is False
