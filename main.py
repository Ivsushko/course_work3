from src.utils import load_json, date_formatting, get_sorted_data, find_card_or_account

database = load_json('operations.json')
new_database = get_sorted_data(database)
instance_operations = date_formatting(new_database)

counter = 0
for item in reversed(instance_operations):
    amount = item.operationAmount["amount"]
    currency = item.operationAmount["currency"]["name"]
    if counter < 5 and item.state == "EXECUTED":
        counter += 1
        print(f'{item.date} {item.description}')
        trans_to = find_card_or_account(item.to_)
        if item.from_ is None:
            print(f'{trans_to}')
        else:
            trans_from = find_card_or_account(item.from_)
            print(f'{trans_from} -> {trans_to}')
        print(f'{amount} {currency}\n')
    else:
        continue
