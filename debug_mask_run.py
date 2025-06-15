from src.masks import get_mask_account, get_mask_card_number

if __name__ == "__main__":
    # Успешные вызовы
    print(get_mask_card_number(1234567812345678))
    print(get_mask_account(8765432187654321))

    # Ошибки (например, слишком короткий номер)
    try:
        print(get_mask_card_number(123))  # Ошибка: короткий номер
    except Exception:
        pass

    try:
        print(get_mask_account("abc123"))  # Ошибка: не число
    except Exception:
        pass
