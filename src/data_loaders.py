import json
import logging
import os
from typing import Any, cast

import pandas as pd

# Создаём папку logs
os.makedirs("logs", exist_ok=True)

# Настройка логгера для data_loaders
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/data_loaders.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

if not logger.hasHandlers():
    logger.addHandler(file_handler)


def load_transactions_from_csv(filepath: str) -> list[dict[str, Any]]:
    """
    Загружает транзакции из CSV-файла.

    :param filepath: Путь к CSV-файлу
    :return: Список словарей с транзакциями
    """
    try:
        df = pd.read_csv(filepath, sep=";")  # ОБЯЗАТЕЛЬНО УКАЖИ sep!
        data = cast(list[dict[str, Any]], df.to_dict(orient="records"))
        logger.debug(f"Загружено {len(data)} транзакций из CSV: {filepath}")
        return data
    except FileNotFoundError:
        logger.error(f"Файл CSV не найден: {filepath}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV: {filepath} | {e}")
        return []


def load_transactions_from_excel(filepath: str) -> list[dict[str, Any]]:
    """
    Загружает транзакции из Excel-файла (.xlsx).

    :param filepath: Путь к Excel-файлу
    :return: Список словарей с транзакциями
    """
    try:
        df = pd.read_excel(filepath, sheet_name=None, engine="openpyxl")
        logger.debug(f"Листы Excel: {list(df.keys())}")

        for name, sheet in df.items():
            if not sheet.empty:
                data = cast(list[dict[str, Any]], sheet.to_dict(orient="records"))
                logger.debug(f"Загружено {len(data)} транзакций из Excel (лист: {name})")
                return data

        logger.warning(f"Все листы Excel пусты: {filepath}")
        return []
    except FileNotFoundError:
        logger.error(f"Файл Excel не найден: {filepath}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel: {filepath} | {e}")
        return []


def load_transactions_from_json(filepath: str) -> list[dict[str, Any]]:
    """
    Загружает транзакции из JSON-файла.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                logger.warning(f"JSON не содержит список: {filepath}")
                return []
            logger.debug(f"Загружено {len(data)} транзакций из JSON: {filepath}")
            return data
    except FileNotFoundError:
        logger.error(f"Файл JSON не найден: {filepath}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Некорректный JSON в файле: {filepath} | {e}")
        return []
    except Exception as e:
        logger.exception(f"Ошибка при чтении JSON: {filepath} | {e}")
        return []
