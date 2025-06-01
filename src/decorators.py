from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор логирует успешное выполнение функции или ошибку при её вызове.
    Логи записываются в файл, если указан filename, иначе выводятся в консоль.

    :param filename: имя файла для записи логов. Если не задано — лог в консоль.
    :return: обёрнутая функция.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message)
                else:
                    print(message, end="")
                return result
            except Exception as e:
                err_type = type(e).__name__
                message = f"{func.__name__} error: {err_type}. " f"Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message)
                else:
                    print(message, end="")
                raise  # Пробрасываем исключение дальше

        return wrapper

    return decorator
