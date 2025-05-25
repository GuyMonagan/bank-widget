from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number(1234567890123456) == "1234 56** **** 3456"


def test_get_mask_account():
    assert get_mask_account(9876543212345678) == "**5678"
