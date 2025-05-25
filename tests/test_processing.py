from processing import filter_by_state, sort_by_date

test_data = [
    {"id": 1, "state": "EXECUTED", "date": "2020-01-01T10:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2020-02-01T10:00:00"},
    {"id": 3, "state": "EXECUTED", "date": "2019-12-01T10:00:00"},
]


def test_filter_by_state_default() -> None:
    result = filter_by_state(test_data)
    assert all(op["state"] == "EXECUTED" for op in result)


def test_filter_by_state_custom() -> None:
    result = filter_by_state(test_data, state="CANCELED")
    assert len(result) == 1 and result[0]["state"] == "CANCELED"


def test_sort_by_date_descending() -> None:
    result = sort_by_date(test_data)
    assert result[0]["date"] == "2020-02-01T10:00:00"


def test_sort_by_date_ascending() -> None:
    result = sort_by_date(test_data, descending=False)
    assert result[0]["date"] == "2019-12-01T10:00:00"
