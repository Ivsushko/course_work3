import json
import operator
from datetime import datetime

from src.classes import Operations


def load_json(path):
    """
    Загружает json файл,
    :param path: Принимает файл
    :return: Возвращает список словарей
    """
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_sorted_data(path):
    """
    Убирает пустые словари из списка словарей
    и сортирует список словарей по ключу 'data'
    :param path: Принимает список словарей, созданный из json файла
    :return: Возвращает отсортированный по ключу 'data' список словарей
    """
    new_list = []
    for item in path:
        if item == {}:
            continue
        else:
            new_list.append(item)
    sorted_list = sorted(new_list, key=operator.itemgetter("date"))
    return sorted_list


def date_formatting(data):
    """
    Создает экземпляры класса с форматированием даты
    :param data: Принимает список словарей
    :return: Возвращает список операций с датой нужного формата
    """
    operations_list = []
    for item in data:
        date = datetime.fromisoformat(item["date"])
        date_formatted = date.strftime("%d.%m.%Y")
        operations = Operations(item["id"],
                                date_formatted,
                                item["state"],
                                item["operationAmount"],
                                item["description"],
                                item["to"],
                                item.get("from"))
        operations_list.append(operations)
    return operations_list


def find_card_or_account(data):
    """
    Разделяет поле экземпляра класса в виде строки по пробелу и
    вычисляет что использовалось (карта или счет)
    :param data: Принимает поле экземпляра класса (from или to)
    :return: Возвращает измененный вид карты или счета
    """
    invoice_list = data.split()
    if len(invoice_list[-1]) == 16:
        return card_formatting(invoice_list)
    elif len(invoice_list[-1]) == 20:
        return account_formatting(invoice_list)


def card_formatting(data):
    """
    Форматирование номера карты в соответствие с заданием
    :param data: Принимает список данных карты
    :return: Возвращает номер карты нужного формата
    """
    if len(data) < 3:
        return f'{data[0]} {data[1][:4]} {data[1][4:6]}** **** {data[1][-4:]}'
    elif len(data) == 3:
        return f'{data[0]} {data[1]} {data[2][:4]} {data[2][4:6]}** **** {data[2][-4:]}'


def account_formatting(data):
    """
    Форматирование номера счёта в соответствие с заданием
    :param data: Принимает список данных счета
    :return: Возвращает номер счета нужного формата
    """
    return f'{data[0]} **{data[1][-4:]}'
