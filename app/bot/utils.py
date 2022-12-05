def is_number(value: str) -> bool:
    if value.isdigit():
        return True
    if value.count(".") == 0:
        return False
    first_part, second_part = value.split(".")
    if first_part.isdigit() and second_part.isdigit():
        return True

    return False
