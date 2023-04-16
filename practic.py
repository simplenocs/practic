import csv

with open('currencies23.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['NAME', 'SYMBOL', 'PRICE', 'MARKET_CAP'])
    crypto_list = list(reader)

while True:
    search_term = input("Введите название криптовалюты: ")
    if search_term == 'stop':
        break
    
    search_results = []
    for crypto in crypto_list:
        if search_term.lower() == crypto['NAME'].lower():
            search_results.append(crypto)

    if search_results:
        for crypto in search_results:
            print("NAME: ", crypto['NAME'])
            print("SYMBOL: ", crypto['SYMBOL'])
            print("PRICE: ", crypto['PRICE'])
            print("MARKET_CAP: ", crypto['MARKET_CAP'])
            print("----------------------")
    else:
        print("Криптовалюта не найдена.")
