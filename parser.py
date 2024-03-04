from bs4 import BeautifulSoup
import requests

url = 'https://yandex.com.am/weather/yekaterinburg?lat=56.838011&lon=60.597465'
response = requests.get(url)
bs = BeautifulSoup(response.text,"lxml")
temp = bs.find('span', 'temp__value temp__value_with-unit')
print(temp.text)