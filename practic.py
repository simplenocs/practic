import csv

with open('currencies23.csv', 'r') as file:
    reader = csv.reader(file)
    crypto_list = list(reader)

header = crypto_list[0]
crypto_list.pop(0)

while True:
    search_name = input('Введите имя криптовалюты (для выхода введите "quit"): ')
    if search_name == 'quit':
        print("GOODBYE MY FRIEND =)")
        break

    results = []

    for crypto in crypto_list:
        name, symbol, price, market_cap = crypto
        if name.strip().lower() == search_name.strip().lower():
            results.append(crypto)

    if len(results) > 0:
        print('{:<15} {:<15} {:<15} {:<15}'.format(*header))
        for crypto in results:
            print('{:<15} {:<15} {:<15} {:<15}'.format(*crypto))
    else:
        print('Криптовалюта с именем "{}" не найдена.'.format(search_name))
