import requests
import datetime
from bs4 import BeautifulSoup
Time = datetime.datetime.now()

dt_string = Time.strftime("%d/%m/%Y %H:%M:%S")
print(dt_string)

response = requests.get('https://ua.sinoptik.ua/погода-житомир')
text = response.text

parse = text.split('<p class="today-temp">')

result = []

for item in parse:
    if item.startswith('+'):
        for value in item.split('</p>'):
            if value.startswith('+') and value[1].isdigit():
                result.append(value)

temperature = result[0].split('&')[0]

print(f'{temperature} C')