from bs4 import BeautifulSoup
import requests

url = 'https://yandex.ru/pogoda/?lat=55.03020096&lon=82.92043304'
res = requests.get(url)
print(res)

basa = BeautifulSoup(res.text, "lxml")
print(basa)

temp = basa.find('span', 'temp__value temp__value_with-unit')
print(temp.text)


