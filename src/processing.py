import re

from collections import Counter
from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список операций по значению поля 'state'.

    :param data: список словарей с операциями
    :param state: статус для фильтрации (по умолчанию 'EXECUTED')
    :return: отфильтрованный список словарей
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список операций по полю 'date'.

    :param data: список словарей с операциями
    :param descending: сортировать по убыванию (True) или возрастанию (False)
    :return: отсортированный список
    """
    return sorted(data, key=lambda x: x.get("date", ""), reverse=descending)


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """Поиск транзакций по описанию через регулярные выражения."""
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [item for item in data if pattern.search(item.get("description", ""))]

def process_bank_operations(data: List[Dict]) -> Dict[str, int]:
    """Подсчёт количества транзакций по описанию."""
    descriptions = [item.get("description", "") for item in data]
    return dict(Counter(descriptions))