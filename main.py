from pathlib import Path

from data_loaders import (
    load_transactions_from_csv,
    load_transactions_from_excel,
    load_transactions_from_json,
)
from external_api import get_transactions_from_api
from generators import filter_by_currency
from processing import (
    filter_by_state,
    process_bank_operations,
    process_bank_search,
    sort_by_date,
)
from widget import get_date, mask_account_card

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


def ask_yes_no(prompt: str) -> bool:
    """Задаёт вопрос пользователю и возвращает True/False."""
    while True:
        answer = input(f"{prompt} (Да/Нет): ").strip().lower()
        if answer in ("да", "yes", "y"):
            return True
        elif answer in ("нет", "no", "n"):
            return False
        print("Пожалуйста, ответьте 'Да' или 'Нет'.")


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите источник данных:")
    print("0. Получить данные из API")
    print("1. JSON")
    print("2. CSV")
    print("3. XLSX")

    while True:
        choice = input("Введите 0, 1, 2 или 3: ").strip()
        if choice in ("0", "1", "2", "3"):
            break
        print("Неверный выбор, попробуйте снова.")

    if choice == "0":
        transactions = get_transactions_from_api()
    elif choice == "1":
        print("Загрузка JSON...")
        transactions = load_transactions_from_json(DATA_DIR / "operations.json")
    elif choice == "2":
        print("Загрузка CSV...")
        transactions = load_transactions_from_csv(DATA_DIR / "transactions.csv")
    else:
        print("Загрузка XLSX...")
        transactions = load_transactions_from_excel(DATA_DIR / "transactions_excel.xlsx")

    allowed_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input(f"Введите статус ({', '.join(allowed_statuses)}): ").strip().upper()
        if status in allowed_statuses:
            break
        print(f"Статус '{status}' недоступен.")

    filtered = filter_by_state(transactions, state=status)

    if ask_yes_no("Отсортировать операции по дате?"):
        descending = ask_yes_no("Сортировать по убыванию?")
        filtered = sort_by_date(filtered, descending=descending)

    if ask_yes_no("Выводить только рублёвые транзакции?"):
        filtered = filter_by_currency(filtered, currency="RUB")

    if ask_yes_no("Отфильтровать по слову в описании?"):
        word = input("Введите слово: ").strip()
        filtered = process_bank_search(filtered, word)

    filtered = list(filtered)

    if not filtered:
        print("Ни одной транзакции не найдено.")
        return

    print(f"Всего операций: {len(filtered)}\n")

    for op in filtered:
        date = get_date(op.get("date", ""))
        desc = op.get("description", "")

        # 1) Получаем amount и currency ПЕРЕД print
        if "operationAmount" in op:
            amount = op["operationAmount"].get("amount", "???")
            currency = op["operationAmount"].get("currency", {}).get("code", "???")
        else:
            amount = op.get("amount", "???")
            currency = op.get("currency_code", "???")

        # 2) Маскируем номера счетов/карт
        from_account = op.get("from", "")
        to_account = op.get("to", "")

        from_masked = mask_account_card(from_account) if from_account else ""
        to_masked = mask_account_card(to_account) if to_account else ""

        # 3) Формируем строку
        if from_account and to_account:
            print(f"{date} | {desc} | {from_masked} -> {to_masked} | Сумма: {amount} {currency}")
        else:
            print(f"{date} | {desc} | Сумма: {amount} {currency}")

    categories = ["Перевод", "Открытие вклада", "Оплата"]
    counts = process_bank_operations(filtered, categories)
    print("\nПодсчет категорий:", counts)


if __name__ == "__main__":
    main()
