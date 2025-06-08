import pytest
import json
from src.utils import load_transactions
from unittest.mock import mock_open, patch


def test_load_transactions_success():
    fake_data = [
        {
            "id": 1,
            "operationAmount": {
                "amount": "123.45",
                "currency": {"code": "RUB"}
            }
        }
    ]

    # превращаем список в JSON-строку
    json_str = json.dumps(fake_data)

    with patch("builtins.open", mock_open(read_data=json_str)):
        with patch("json.load", return_value=fake_data):
            result = load_transactions("data/operations.json")
            assert isinstance(result, list)
            assert result == fake_data
