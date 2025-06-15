import pytest
from unittest.mock import patch, MagicMock

from src.data_loaders import load_transactions_from_csv, load_transactions_from_excel


def test_load_transactions_from_csv_success():
    mock_data = [{"id": 1}, {"id": 2}]

    with patch("src.data_loaders.pd.read_csv", return_value=MagicMock(to_dict=lambda orient: mock_data)):
        result = load_transactions_from_csv("fake.csv")
        assert result == mock_data


def test_load_transactions_from_csv_file_not_found():
    with patch("src.data_loaders.pd.read_csv", side_effect=FileNotFoundError):
        result = load_transactions_from_csv("missing.csv")
        assert result == []


def test_load_transactions_from_excel_success():
    mock_data = [{"id": 1}, {"id": 2}]
    mock_sheet = MagicMock()
    mock_sheet.empty = False
    mock_sheet.to_dict.return_value = mock_data

    mock_sheets = {"Sheet1": mock_sheet}

    with patch("src.data_loaders.pd.read_excel", return_value=mock_sheets):
        result = load_transactions_from_excel("fake.xlsx")
        assert result == mock_data


def test_load_transactions_from_excel_file_not_found():
    with patch("src.data_loaders.pd.read_excel", side_effect=FileNotFoundError):
        result = load_transactions_from_excel("missing.xlsx")
        assert result == []
