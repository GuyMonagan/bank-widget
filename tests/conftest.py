import pytest


@pytest.fixture
def sample_operations():
    """Фикстура с примером банковских операций с разными статусами и датами."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-03T14:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-01T10:00:00"},
        {"id": 3, "state": "PENDING", "date": "2023-01-05T09:30:00"},
        {"id": 4, "state": "EXECUTED", "date": "2023-01-02T08:00:00"},
    ]
