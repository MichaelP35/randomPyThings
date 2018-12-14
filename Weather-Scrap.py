import requests
from bs4 import BeautifulSoup


# Weather.gov's Forecast Search
locationinput = input("Input Your Zipcode = ")
url = ('https://www.weather.gov/' + locationinput)

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
