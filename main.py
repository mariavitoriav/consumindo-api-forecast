import locale
import requests
import config

locale.setlocale(locale.LC_ALL, '')
URL = 'https://api.hgbrasil.com/weather'.format('?key={0}', config.api_key)
response = requests.get(URL)
print(response)

temp = int(response.json()['results']['temp'])
print(temp)
req_date = response.json()['results']['date']
print(req_date)
req_time = response.json()['results']['time']
print(req_time)
description = response.json()['results']['description']
print(description)
currently = response.json()['results']['currently']
print(currently)
humidity = response.json()['results']['humidity']
print(humidity)
wind_speedy = response.json()['results']['wind_speedy']
print(wind_speedy)
sunrise = response.json()['results']['sunrise']
print(sunrise)
sunset = response.json()['results']['sunset']
print(sunset)
condition = response.json()['results']['condition_slug']
print(condition)
forecasts = (response.json()['results']['forecast'])

total_max = 0
days_max = 0

for forecast in forecasts:
    total_max = total_max + forecast['max']
    days_max = days_max + 1

print(total_max/days_max)

total_min = 0
days_min = 0

for forecast in forecasts:
    total_min = total_min + forecast['min']
    days_min = days_min + 1

print(total_min/days_min)

