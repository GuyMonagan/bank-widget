from typing import List, Dict, Any
from generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_usd(sample_transactions: List[Dict[str, Any]]) -> None:
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    for tx in result:
        assert tx["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_absent(sample_transactions: List[Dict[str, Any]]) -> None:
    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert result == []


def test_transaction_descriptions(sample_transactions: List[Dict[str, Any]]) -> None:
    result = list(transaction_descriptions(sample_transactions))
    assert result == [
        "Перевод организации",
        "Оплата товара",
        "Перевод со счета",
    ]


def test_transaction_descriptions_empty() -> None:
    result = list(transaction_descriptions([]))
    assert result == []


def test_card_number_generator_basic() -> None:
    result = list(card_number_generator(1, 3))
    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]


def test_card_number_generator_edges() -> None:
    result = list(card_number_generator(9999_9999_9999_9998, 9999_9999_9999_9999))
    assert result == [
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]


def test_card_number_generator_empty_range() -> None:
    result = list(card_number_generator(5, 4))
    assert result == []

