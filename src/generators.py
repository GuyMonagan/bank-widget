from typing import Iterator

def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Фильтрует транзакции по коду валюты (currency), возвращает итератор."""
    yield from ()  # TODO: заменить на логику

def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Генерирует описания транзакций по очереди."""
    yield from ()  # TODO: заменить на логику

def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX от start до stop включительно."""
    yield from ()  # TODO: заменить на логику
