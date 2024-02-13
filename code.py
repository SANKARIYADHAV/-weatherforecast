import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # You can change units to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error {response.status_code}: {data['message']}")
            return None

    except requests.ConnectionError:
        print("Error: Unable to connect to the API.")
        return None

def display_weather(weather_data):
    if weather_data:
        print("\nWeather Information:")
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        print(f"Description: {weather_data['weather'][0]['description']}")
    else:
        print("Unable to retrieve weather information.")

def main():
    api_key =(https://openweathermap.org/)   # Replace with your OpenWeatherMap API key
    location = input("Enter city name or zip code: ")
    
    weather_data = get_weather(api_key, location)

    display_weather(weather_data)

if __name__ == "__main__":
    main()
