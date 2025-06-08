import json
import tempfile
from unittest.mock import mock_open, patch

from src.utils import load_transactions


def test_load_transactions_success():
    fake_data = [{"id": 1, "operationAmount": {"amount": "123.45", "currency": {"code": "RUB"}}}]

    # превращаем список в JSON-строку
    json_str = json.dumps(fake_data)

    with patch("builtins.open", mock_open(read_data=json_str)):
        with patch("json.load", return_value=fake_data):
            result = load_transactions("data/operations.json")
            assert isinstance(result, list)
            assert result == fake_data


def test_load_transactions_file_not_found():
    result = load_transactions("data/nonexistent.json")
    assert result == []


def test_load_transactions_empty_file():
    with patch("builtins.open", mock_open(read_data="")):
        with patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0)):
            result = load_transactions("data/fake.json")
            assert result == []


def test_load_transactions_not_list():
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".json", delete=False) as tmp:
        json.dump({"foo": "bar"}, tmp)
        tmp_path = tmp.name

    result = load_transactions(tmp_path)
    assert result == []
