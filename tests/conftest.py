from typing import Any, Dict, List

import pytest


@pytest.fixture
def sample_operations() -> List[Dict[str, Any]]:
    """Фикстура с примером банковских операций с разными статусами и датами."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-03T14:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-01T10:00:00"},
        {"id": 3, "state": "PENDING", "date": "2023-01-05T09:30:00"},
        {"id": 4, "state": "EXECUTED", "date": "2023-01-02T08:00:00"},
    ]


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "Доллар", "code": "USD"},
            },
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "200.00",
                "currency": {"name": "Рубль", "code": "RUB"},
            },
            "description": "Оплата товара",
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": "300.00",
                "currency": {"name": "Доллар", "code": "USD"},
            },
            "description": "Перевод со счета",
        },
    ]
