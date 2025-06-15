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
## Переменные окружения

Для работы внешнего API используется переменная окружения API_URL.

Создайте .env на основе примера:
```
cp .env.example .env
```
 
Содержимое .env.example:
```
API_URL=https://api.exchangerate.host/latest

```

## Модуль utils

`load_transactions(path: str)` — загружает список транзакций из JSON-файла.

## Модуль external_api

`fetch_exchange_rates()` — возвращает текущие курсы валют с внешнего API.

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

## Модуль decorators

Модуль decorators предоставляет декоратор @log, который логирует вызовы функций и возможные ошибки.
Поддерживает логирование как в консоль, так и в файл.

### Пример использования:

```
from decorators import log

@log()
def add(x: int, y: int) -> int:
    return x + y

@log(filename="errors.log")
def divide(x: int, y: int) -> float:
    return x / y

add(2, 3)        # Лог: add ok
divide(1, 0)     # Лог: divide error: ZeroDivisionError

```
### Вывод в консоль
```
add ok
divide error: ZeroDivisionError
Inputs: (1, 0)

```
### Вывод в файл (errors.log)

```
divide error: ZeroDivisionError
Inputs: (1, 0)

```

## Модуль `data_loaders`

Поддержка новых форматов данных: CSV и Excel.

### Функции

- `load_transactions_from_csv(filepath: str) -> list[dict[str, Any]]`  
  Загружает список транзакций из CSV-файла.

- `load_transactions_from_excel(filepath: str) -> list[dict[str, Any]]`  
  Загружает список транзакций из Excel (.xlsx).

### Пример использования

```
from data_loaders import load_transactions_from_csv, load_transactions_from_excel

csv_data = load_transactions_from_csv("data/transactions.csv")
excel_data = load_transactions_from_excel("data/transactions_excel.xlsx")

print(len(csv_data))   # ➜ 1000
print(len(excel_data)) # ➜ 1000
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
