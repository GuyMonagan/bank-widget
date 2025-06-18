from typing import Dict, List

import pytest

from processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


def test_filter_by_state_default(sample_operations: List[Dict[str, str]]) -> None:
    result = filter_by_state(sample_operations)
    assert all(op["state"] == "EXECUTED" for op in result)


def test_filter_by_state_custom(sample_operations: List[Dict[str, str]]) -> None:
    result = filter_by_state(sample_operations, state="CANCELED")
    assert len(result) == 1 and result[0]["state"] == "CANCELED"


def test_sort_by_date_descending(sample_operations: List[Dict[str, str]]) -> None:
    result = sort_by_date(sample_operations)
    assert result[0]["date"] == "2023-01-05T09:30:00"


def test_sort_by_date_ascending(sample_operations: List[Dict[str, str]]) -> None:
    result = sort_by_date(sample_operations, descending=False)
    assert result[0]["date"] == "2023-01-01T10:00:00"


@pytest.mark.parametrize(
    "state,expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 1),
        ("PENDING", 1),
        ("REJECTED", 0),
    ],
)
def test_filter_by_state_param(state: str, expected_count: int, sample_operations: List[Dict[str, str]]) -> None:
    result = filter_by_state(sample_operations, state)
    assert len(result) == expected_count


@pytest.mark.parametrize(
    "search_term, expected_count",
    [
        ("Перевод", 2),
        ("Оплата", 1),
        ("Не существует", 0),
    ],
)
def test_process_bank_search(sample_transactions: list[dict], search_term: str, expected_count: int) -> None:
    result = process_bank_search(sample_transactions, search_term)
    assert len(result) == expected_count
    for op in result:
        assert search_term in op["description"]


@pytest.mark.parametrize(
    "categories, expected",
    [
        (["Перевод", "Оплата"], {"Перевод": 2, "Оплата": 1}),
        (["Перевод"], {"Перевод": 2}),
        (["Не существует"], {"Не существует": 0}),
    ],
)
def test_process_bank_operations(sample_transactions: list[dict], categories: list[str], expected: dict) -> None:
    result = process_bank_operations(sample_transactions, categories)
    assert result == expected
