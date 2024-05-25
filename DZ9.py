import requests
import datetime
from bs4 import BeautifulSoup
Time = datetime.datetime.now()

dt_string = Time.strftime("%d/%m/%Y %H:%M:%S")
print(dt_string)

response = requests.get('https://ua.sinoptik.ua/погода-житомир', headers={'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0', 'Accept':
'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding':
'gzip, deflate, br, zstd',
'Accept-Language':
'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'})
print(response.status_code)
if response.status_code == 200:
    text = response.text.encode('utf-8')
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all('div', class_=lambda cl: cl and 'main' in cl.split())
    for element in soup_list:
        for p in element.find_all_next('p'):
            print(p)
            # print(p.text)

else:
    print('error')