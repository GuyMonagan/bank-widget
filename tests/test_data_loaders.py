import json
from unittest.mock import MagicMock, patch, mock_open

from src.data_loaders import (
    load_transactions_from_csv,
    load_transactions_from_excel,
    load_transactions_from_json,
)


def test_load_transactions_from_csv_success():
    mock_data = [{"id": 1}, {"id": 2}]
    mock_df = MagicMock()
    mock_df.to_dict.return_value = mock_data

    with patch("src.data_loaders.pd.read_csv", return_value=mock_df):
        result = load_transactions_from_csv("fake.csv")
        assert result == mock_data


def test_load_transactions_from_csv_file_not_found():
    with patch("src.data_loaders.pd.read_csv", side_effect=FileNotFoundError):
        result = load_transactions_from_csv("missing.csv")
        assert result == []


def test_load_transactions_from_csv_unexpected_error():
    with patch("src.data_loaders.pd.read_csv", side_effect=ValueError("oops")):
        result = load_transactions_from_csv("bad.csv")
        assert result == []


def test_load_transactions_from_excel_success():
    mock_data = [{"id": 1}, {"id": 2}]
    mock_sheet = MagicMock()
    mock_sheet.empty = False
    mock_sheet.to_dict.return_value = mock_data

    sheets = {"Sheet1": mock_sheet}

    with patch("src.data_loaders.pd.read_excel", return_value=sheets):
        result = load_transactions_from_excel("fake.xlsx")
        assert result == mock_data


def test_load_transactions_from_excel_all_sheets_empty():
    mock_sheet = MagicMock()
    mock_sheet.empty = True

    sheets = {"Sheet1": mock_sheet, "Sheet2": mock_sheet}

    with patch("src.data_loaders.pd.read_excel", return_value=sheets):
        result = load_transactions_from_excel("fake.xlsx")
        assert result == []


def test_load_transactions_from_excel_file_not_found():
    with patch("src.data_loaders.pd.read_excel", side_effect=FileNotFoundError):
        result = load_transactions_from_excel("missing.xlsx")
        assert result == []


def test_load_transactions_from_excel_unexpected_error():
    with patch("src.data_loaders.pd.read_excel", side_effect=ValueError("oops")):
        result = load_transactions_from_excel("bad.xlsx")
        assert result == []


def test_load_transactions_from_json_success():
    mock_data = [{"id": 1}, {"id": 2}]
    m = mock_open(read_data=json.dumps(mock_data))

    with patch("builtins.open", m):
        result = load_transactions_from_json("fake.json")
        assert result == mock_data


def test_load_transactions_from_json_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_transactions_from_json("missing.json")
        assert result == []


def test_load_transactions_from_json_invalid_json():
    m = mock_open(read_data="not a json")

    with patch("builtins.open", m):
        result = load_transactions_from_json("bad.json")
        assert result == []


def test_load_transactions_from_json_not_a_list():
    # JSON, но не список
    m = mock_open(read_data=json.dumps({"foo": "bar"}))

    with patch("builtins.open", m):
        result = load_transactions_from_json("weird.json")
        assert result == []


def test_logger_setup(monkeypatch):
    """
    Проверка, что при импорте создаются папка и файл логгера.
    """
    makedirs = MagicMock()
    file_handler = MagicMock()

    monkeypatch.setattr("src.data_loaders.os.makedirs", makedirs)
    monkeypatch.setattr("src.data_loaders.logging.FileHandler", lambda *a, **kw: file_handler)

    # Перегружаем модуль, чтобы заново запустить логгер
    import importlib
    import src.data_loaders as dl
    importlib.reload(dl)

    makedirs.assert_called_once_with("logs", exist_ok=True)
    file_handler.setLevel.assert_called()
    file_handler.setFormatter.assert_called()
