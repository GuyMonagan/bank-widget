import os
from typing import Any, Dict, List

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL", "https://api.apilayer.com/exchangerates_data/convert")
API_TRANSACTIONS_URL = os.getenv("API_TRANSACTIONS_URL", "https://example.com/api/transactions")  # заглушка


def convert_to_rubles(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли, если валюта — USD или EUR.
    """
    amount_str = transaction["operationAmount"]["amount"]
    currency_code = transaction["operationAmount"]["currency"]["code"]

    if currency_code == "RUB":
        return float(amount_str)

    if currency_code not in ("USD", "EUR"):
        raise ValueError(f"Неизвестная валюта: {currency_code}")

    url = API_URL
    params = {"from": currency_code, "to": "RUB", "amount": amount_str}
    headers = {"apikey": API_KEY}

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    data = response.json()

    return float(data["result"])


def get_transactions_from_api() -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из внешнего API.
    Если настоящего API нет — возвращает фейковые данные для теста.
    """
    try:
        headers = {"apikey": API_KEY} if API_KEY else {}
        response = requests.get(API_TRANSACTIONS_URL, headers=headers)
        response.raise_for_status()
        return response.json()  # Ожидается, что API вернёт список словарей
    except Exception:
        print("⚠️ Не удалось получить данные из реального API. Возвращаю заглушку.")
        # Фейковые данные, если API недоступно
        return [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2023-01-01",
                "description": "Перевод организации",
                "operationAmount": {"amount": "100", "currency": {"code": "USD"}},
            },
            {
                "id": 2,
                "state": "CANCELED",
                "date": "2023-01-02",
                "description": "Оплата услуг",
                "operationAmount": {"amount": "5000", "currency": {"code": "RUB"}},
            },
        ]
