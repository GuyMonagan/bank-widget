import json
from typing import Any
import logging
import os

# Создание папки logs, если её нет
os.makedirs("logs", exist_ok=True)

# Настройка логгера для модуля utils
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Добавляем обработчик
if not logger.hasHandlers():
    logger.addHandler(file_handler)


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
                logger.debug(f"Загружено {len(data)} транзакций из {filepath}")
                return data
            else:
                logger.error(f"Ожидался список в {filepath}, получен {type(data).__name__}")
                return []

    except FileNotFoundError:
        logger.error(f"Файл {filepath} не найден")
        return []

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON из файла {filepath}: {e}")
        return []

