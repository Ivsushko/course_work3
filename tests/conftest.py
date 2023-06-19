import pytest

from src.classes import Operations


@pytest.fixture
def dict_fixture():
    return [
        {
            "id": 414894334,
            "state": "EXECUTED",
            "date": "2019-06-30T15:11:53.136004",
            "operationAmount": {
                "amount": "95860.47",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод на счет",
            "to": "Счет 43475624104328495820"
        },
        {},
        {
            "id": 596914981,
            "state": "CANCELED",
            "date": "2018-04-16T17:34:19.241289",
            "operationAmount": {
                "amount": "65169.27",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1813166339376336",
            "to": "Счет 97848259954268659635"
        }
    ]


@pytest.fixture()
def result_for_dict_fixture():
    return [
        {
            "id": 596914981,
            "state": "CANCELED",
            "date": "2018-04-16T17:34:19.241289",
            "operationAmount": {
                "amount": "65169.27",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1813166339376336",
            "to": "Счет 97848259954268659635"
        },
        {
            "id": 414894334,
            "state": "EXECUTED",
            "date": "2019-06-30T15:11:53.136004",
            "operationAmount": {
                "amount": "95860.47",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод на счет",
            "to": "Счет 43475624104328495820"
        },
    ]


@pytest.fixture()
def result_for_instance_json():
    operation_1 = Operations(596914981, "16.04.2018", "CANCELED", {"amount": "65169.27", "currency": {"name": "USD", "code": "USD",}}, "Перевод организации", "Счет 97848259954268659635", "Visa Platinum 1813166339376336")
    operation_2 = Operations(414894334, "30.06.2019", "EXECUTED", {"amount": "95860.47", "currency": {"name": "руб.", "code": "RUB"}}, "Перевод на счет", "Счет 43475624104328495820")
    return [operation_1, operation_2]