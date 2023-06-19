from src.utils import load_json, get_sorted_data, find_card_or_account, card_formatting, \
    account_formatting, date_formatting


def test_load_json(dict_fixture):
    assert load_json("json/test.json") == dict_fixture


def test_get_sorted_data(dict_fixture, result_for_dict_fixture):
    assert get_sorted_data(dict_fixture) == result_for_dict_fixture


def test_date_formatting(result_for_dict_fixture, result_for_instance_json):
    assert date_formatting(result_for_dict_fixture) == result_for_instance_json


def test_find_card_or_account():
    assert find_card_or_account("Счет 90424923579946435907") == "Счет **5907"
    assert find_card_or_account("Visa Platinum 1813166339376336") == "Visa Platinum 1813 16** **** 6336"


def test_card_formatting():
    assert card_formatting(["Visa", "Platinum", "1813166339376336"]) == "Visa Platinum 1813 16** **** 6336"
    assert card_formatting(["Maestro", "3928549031574026"]) == "Maestro 3928 54** **** 4026"
    assert card_formatting(["Visa", "Gold", "5999414228426353"]) == "Visa Gold 5999 41** **** 6353"


def test_account_formatting():
    assert account_formatting(["Счет", "84163357546688983493"]) == "Счет **3493"
