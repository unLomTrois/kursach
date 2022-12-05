"""Дополнительные функции"""

def is_number(value: str) -> bool:
    """проверяет строку value на то, что оно может быть приведено к типу float"""
    if value.isdigit():
        return True
    if value.count(".") == 0:
        return False
    first_part, second_part = value.split(".")
    if first_part.isdigit() and second_part.isdigit():
        return True

    return False
