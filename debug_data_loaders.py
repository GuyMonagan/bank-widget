from src.data_loaders import load_transactions_from_csv, load_transactions_from_excel

csv_data = load_transactions_from_csv("data/transactions.csv")
print(f"CSV: Загружено {len(csv_data)} транзакций")

excel_data = load_transactions_from_excel("data/transactions_excel.xlsx")
print(f"Excel: Загружено {len(excel_data)} транзакций")
