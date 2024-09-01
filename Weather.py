import requests

def get_weather(api_key, city):
    url = "http://api.openweathermap.org/data/2.5/forecast"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }

    response = requests.get(url, params=params)
   
    if response.status_code == 200:
        data = response.json()
        
        
        print(f"Weather forecast for {city}:")
        for entry in data['list']:
            dt_txt = entry['dt_txt']
            main = entry['main']
            weather = entry['weather'][0]
            
            print(f"\nDate and Time: {dt_txt}")
            print(f"Temperature: {main['temp']}°C")
            print(f"Weather: {weather['description'].capitalize()}")
            print(f"Humidity: {main['humidity']}%")
            print(f"Pressure: {main['pressure']} hPa")
            
    else:
        print("Error fetching weather data. Please check your API key and city name.")

api_key = 'e114a7a0ae595a3fab28ba629489de90'
city = input("Enter your city name: ")
get_weather(api_key, city)
