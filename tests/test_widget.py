import pytest

from widget import get_date, mask_account_card


def test_mask_account_card_card() -> None:
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"


def test_mask_account_card_account() -> None:
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"


# Тесты для mask_account_card
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(input_str: str, expected: str) -> None:
    assert mask_account_card(input_str) == expected


# Тесты для get_date
@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2020-01-01T00:00:00.000000", "01.01.2020"),
    ],
)
def test_get_date(input_date: str, expected: str) -> None:
    assert get_date(input_date) == expected
