import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=53.8589&longitude=-9.29&current=temperature_2m,wind_speed_10m"

# Make the HTTP GET request to the URL
response = requests.get(url)

# Parse the JSON content of the response
data = response.json()

# Extract the temperature from the 'current' dictionary
temperature = data['current']['temperature_2m']
wind = data['current']['wind_speed_10m']

# Print the temperature
print(f"Temperature: {temperature}°C")
print(f'Wind speed: {wind}km/h')
