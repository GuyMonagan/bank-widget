from pathlib import Path

import pytest
from _pytest.capture import CaptureFixture

from decorators import log


# === Тест логирования в консоль (успешный вызов) ===
def test_log_to_console_success(capsys: CaptureFixture[str]) -> None:
    @log()
    def add(x: int, y: int) -> int:
        return x + y

    assert add(2, 3) == 5
    captured = capsys.readouterr()
    assert "add ok" in captured.out


# === Тест логирования в консоль (ошибка) ===
def test_log_to_console_error(capsys: CaptureFixture[str]) -> None:
    @log()
    def divide(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0)" in captured.out


# === Тест логирования в файл (успешный вызов) ===
def test_log_to_file_success(tmp_path: Path) -> None:
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def say_hello() -> str:
        return "hello"

    assert say_hello() == "hello"

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert "say_hello ok" in content


# === Тест логирования в файл (ошибка) ===
def test_log_to_file_error(tmp_path: Path) -> None:
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def explode() -> None:
        raise ValueError("Boom")

    with pytest.raises(ValueError):
        explode()

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert "explode error: ValueError" in content
    assert "Inputs: ()" in content
