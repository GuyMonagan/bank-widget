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
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: начальное значение (включительно)
    :param stop: конечное значение (включительно)
    :yield: строка с форматированным номером
    """
    for number in range(start, stop + 1):
        card_str = str(number).rjust(16, "0")
        formatted = " ".join([card_str[i:i+4] for i in range(0, 16, 4)])
        yield formatted

