from typing import Iterator

def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """
    Фильтрует транзакции по коду валюты (например, 'USD').

    :param transactions: список транзакций
    :param currency: код валюты (например, 'USD', 'RUB')
    :return: итератор по подходящим транзакциям
    """
    for tx in transactions:
        if (
            "operationAmount" in tx
            and "currency" in tx["operationAmount"]
            and tx["operationAmount"]["currency"].get("code") == currency
        ):
            yield tx

def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Генерирует описания транзакций по очереди.

    :param transactions: список словарей с транзакциями
    :return: генератор описаний
    """
    for tx in transactions:
        description = tx.get("description")
        if description:
            yield description

def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX от start до stop включительно."""
    yield from ()  # TODO: заменить на логику
