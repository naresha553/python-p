import requests

API_KEY = '1049527fb02515ae0773e4f43633ec91'
BASE_URL =  'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"City: {data['name']}")
        print(f'Temperature in {city_name}: {data["main"]["temp"]}°C')
        print(f'Weather: {data["weather"][0]["description"]}')
    else:
        print(f'Error: {data["message"]}')

if __name__ == '__main__':
    city_name = input('Enter city name: ')
    get_weather(city_name)
