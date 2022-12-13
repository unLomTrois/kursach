"""Дополнительные функции"""

def is_number(string: str) -> bool:
    """проверяет строку value на то, что оно может быть приведено к типу float"""
    if string.isdigit():
        return True
    if string.count(".") == 0:
        return False
    first_part, second_part = string.split(".")
    if first_part.isdigit() and second_part.isdigit():
        return True

    return False
