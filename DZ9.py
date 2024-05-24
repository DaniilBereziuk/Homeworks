import requests
import datetime

Time = datetime.datetime.now()

dt_string = Time.strftime("%d/%m/%Y %H:%M:%S")
print(dt_string)

response = requests.get('https://pogoda.meta.ua/ua/Zhytomyrska/Zhytomyrskyi/Zhytomyr/')
text = response.text
parse = text.split('<div class="city__forecast-feels">')

result = []

for item in parse:
    for value in item.split('</div>'):
        if value[1].isdigit():
            result.append(value)

print(result)