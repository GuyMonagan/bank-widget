# Entry point (не используется в этом задании)
from processing import filter_by_state, sort_by_date, process_bank_search, process_bank_operations
from generators import filter_by_currency
from widget import get_date, mask_account_card

def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Тут — чтение из файла (пока можно заглушку или загруженный список)
    transactions = []  # TODO: прочитать JSON/CSV/XLSX

    # Фильтрация по статусу
    allowed_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input(f"Введите статус для фильтрации ({', '.join(allowed_statuses)}): ").upper()
        if status in allowed_statuses:
            break
        print(f"Статус {status} недоступен.")
    filtered = filter_by_state(transactions, state=status)

    # Остальные фильтры: сортировка, валюта, поиск по описанию
    # TODO: Реализовать

    # Печать
    print(f"Найдено {len(filtered)} операций")
    for op in filtered:
        print(op)