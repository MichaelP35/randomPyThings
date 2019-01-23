import requests
from bs4 import BeautifulSoup


# Weather.gov's Forecast Search
location_input = input("Input Your Zip-code = ")
url = ('https://www.weather.gov/' + location_input)

# Retrieves Data
data = requests.get(url)

# Converts Data using BS4
soup = BeautifulSoup(data.text, 'html.parser')

# Prints Conditions
Conditions = soup.find(
    'p', {'class': 'myforecast-current'}).text.strip()
# Prints Temperature
TemperatureF = soup.find(
    'p', {'class': 'myforecast-current-lrg'}).text.strip()
TemperatureC = soup.find(
    'p', {'class': 'myforecast-current-sm'}).text.strip()
print(f"\n{Conditions} {TemperatureF} {TemperatureC}")
