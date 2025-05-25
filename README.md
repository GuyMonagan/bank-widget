# Bank Widget

Виджет для отображения замаскированных номеров карт и счетов.  
Включает функции маскировки и тесты.  
Проект создан с использованием Poetry.

## Цель

- маскировка номеров карт и счетов
- фильтрация по статусу (`filter_by_state`)
- сортировка по дате (`sort_by_date`)

## Установка

```bash
git clone https://github.com/GuyMonagan/bank-widget.git
cd bank-widget
poetry install
```

## Использование

```python
from processing import filter_by_state, sort_by_date

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2020-01-01T10:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2020-02-01T10:00:00"},
]

# Фильтрация по статусу (по умолчанию — 'EXECUTED')
executed_ops = filter_by_state(operations)

# Сортировка по дате (по умолчанию — по убыванию)
sorted_ops = sort_by_date(executed_ops)
```

## Тесты

```bash
poetry run pytest
poetry run flake8
poetry run mypy src tests
poetry run black --check .
poetry run isort --check .
```

