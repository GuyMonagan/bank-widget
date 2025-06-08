import pytest
from unittest.mock import patch, Mock
from src.external_api import convert_to_rubles


@patch("src.external_api.requests.get")
def test_convert_usd_to_rub(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 1234.56}
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "15.00",
            "currency": {"code": "USD"}
        }
    }

    result = convert_to_rubles(transaction)
    assert result == 1234.56
    mock_get.assert_called_once()


def test_convert_rub_no_api():
    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "RUB"}
        }
    }

    result = convert_to_rubles(transaction)
    assert result == 100.0


def test_convert_invalid_currency():
    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "BTC"}  # не поддерживаем
        }
    }

    with pytest.raises(ValueError):
        convert_to_rubles(transaction)


@patch("src.external_api.requests.get")
def test_convert_api_error(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = Exception("API error")
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "50.00",
            "currency": {"code": "USD"}
        }
    }

    with pytest.raises(Exception, match="API error"):
        convert_to_rubles(transaction)
