import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()  # загружаем переменные из .env

API_KEY = os.getenv("API_KEY")


def convert_to_rubles(transaction: dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли, если валюта — USD или EUR.
    Возвращает сумму в рублях (float).
    """

    amount_str = transaction["operationAmount"]["amount"]
    currency_code = transaction["operationAmount"]["currency"]["code"]

    if currency_code == "RUB":
        return float(amount_str)

    if currency_code not in ("USD", "EUR"):
        raise ValueError(f"Неизвестная валюта: {currency_code}")

    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"from": currency_code, "to": "RUB", "amount": amount_str}
    headers = {"apikey": API_KEY}

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    data = response.json()

    return float(data["result"])
