from src.utils import load_transactions

# Успешная загрузка
print(load_transactions("data/operations.json"))

# Попытка загрузить несуществующий файл
print(load_transactions("file_that_does_not_exist.json"))
