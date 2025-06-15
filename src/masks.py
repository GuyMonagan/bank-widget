import logging
import os

# Создание папки logs, если её нет
os.makedirs("logs", exist_ok=True)

# Настройка логгера для masks
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

if not logger.hasHandlers():
    logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает замаскированный номер карты в формате: XXXX XX** **** XXXX.
    Показывает первые 6 и последние 4 цифры, остальное скрыто.
    """
    try:
        card_str = str(card_number)
        result = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
        logger.debug(f"Карта успешно замаскирована: {result}")
        return result
    except Exception as e:
        logger.error(f"Ошибка при маскировании карты {card_number}: {e}")
        raise


def get_mask_account(account_number: int) -> str:
    """
    Возвращает замаскированный номер счёта в том же формате, что и карта.
    """
    try:
        account_str = str(account_number)
        result = f"**{account_str[-4:]}"
        logger.debug(f"Номер счёта успешно замаскирован: {result}")
        return result
    except Exception as e:
        logger.error(f"Ошибка при маскировании номера счёта {account_number}: {e}")
        raise
