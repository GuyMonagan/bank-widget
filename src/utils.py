import json
from typing import Any


def load_transactions(filepath: str) -> list[dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.

    :param filepath: Путь до JSON-файла
    :return: Список словарей с транзакциями, либо пустой список
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data
            else:
                return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []
