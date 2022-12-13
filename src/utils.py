"""Дополнительные функции"""

def soderzhit_tochku(stroka: str) -> bool:
    return stroka.count(".") > 0

def is_number(stroka: str) -> bool:
    """проверяет строку value на то, что оно может быть приведено к типу float"""
    if stroka.isdigit():
        return True
    if not soderzhit_tochku(stroka):
        return False
    first_part, second_part = stroka.split(".")
    if first_part.isdigit() and second_part.isdigit():
        return True

    return False
