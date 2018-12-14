import requests
from bs4 import BeautifulSoup


# Weather.gov's Forecast for Chicago
url = (
    'https://forecast.weather.gov/'
    'MapClick.php?lat=41.96821070000004&lon=-87.76519899999994')

# Retreieves Data
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
print(Conditions, TemperatureF, TemperatureC)
