from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Принимает строку с типом и номером карты или счета.
    Возвращает строку с замаскированным номером.
    """
    if data.startswith("Счет"):
        label, number = data.split(" ", 1)
        masked = get_mask_account(int(number))
        return f"{label} {masked}"
    else:
        parts = data.rsplit(" ", 1)
        label, number = parts[0], parts[1]
        masked = get_mask_card_number(int(number))
        return f"{label} {masked}"


def get_date(datetime_str: str) -> str:
    """
    Преобразует дату из строки вида "2024-03-11T02:26:18.671407"
    в формат "день.месяц.год" → "11.03.2024"
    """
    dt = datetime.fromisoformat(datetime_str)
    return dt.strftime("%d.%m.%Y")
