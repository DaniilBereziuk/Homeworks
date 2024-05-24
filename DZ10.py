import requests

response = requests.get('https://bank.gov.ua/ua/markets/exchangerates')
text = response.text

parse = text.split('<td data-label="Офіційний курс">')

result = []

for item in parse:
    for value in item.split('</td>'):
        if len(value) > 1 and value[1].isdigit():
            result.append(value.strip())

usd_cost = float(result[4].replace(',', '.'))
print(f'USD cost -- {usd_cost}')

how_many = int(input('How many UAH -- '))

diya = how_many / usd_cost

print(diya)