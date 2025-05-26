from generators import filter_by_currency


def test_filter_by_currency_usd(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    for tx in result:
        assert tx["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_absent(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert result == []


from generators import transaction_descriptions


def test_transaction_descriptions(sample_transactions):
    result = list(transaction_descriptions(sample_transactions))
    assert result == [
        "Перевод организации",
        "Оплата товара",
        "Перевод со счета",
    ]

def test_transaction_descriptions_empty():
    result = list(transaction_descriptions([]))
    assert result == []
