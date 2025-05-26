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
## Модуль generators

Модуль предназначен для работы с транзакциями и генерации данных в потоковом режиме.

### Функции
filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]
Возвращает итератор по транзакциям, где валюта совпадает с заданной.

transaction_descriptions(transactions: list[dict]) -> Iterator[str]
Генератор, возвращающий описания транзакций из списка.

card_number_generator(start: int, stop: int) -> Iterator[str]
Генератор, создающий номера карт в формате XXXX XXXX XXXX XXXX.

### Примеры использования

```
from generators import filter_by_currency, transaction_descriptions, card_number_generator

transactions = [
    {
        "id": 1,
        "operationAmount": {"amount": "1000", "currency": {"code": "USD", "name": "USD"}},
        "description": "Перевод организации"
    },
    {
        "id": 2,
        "operationAmount": {"amount": "500", "currency": {"code": "RUB", "name": "руб."}},
        "description": "Перевод со счета"
    }
]

# Фильтрация по валюте
usd_ops = filter_by_currency(transactions, "USD")
print(next(usd_ops))  # Вернёт только транзакции в USD

# Генерация описаний
for desc in transaction_descriptions(transactions):
    print(desc)

# Генерация номеров карт
for card in card_number_generator(1, 3):
    print(card)
# → 0000 0000 0000 0001
# → 0000 0000 0000 0002
# → 0000 0000 0000 0003
```



## Тесты

```bash
poetry run pytest
poetry run mypy src tests
poetry run flake8
poetry run isort --check .
poetry run black --check .
poetry run coverage run -m pytest
poetry run coverage report
poetry run coverage html  # HTML-отчёт будет в htmlcov/index.html
```
>Покрытие тестами: 100%
Используются фикстуры и параметризация
