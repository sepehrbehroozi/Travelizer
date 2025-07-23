import requests
city = input("Enter city name: ").lower()
url = "https://the-weather-api.p.rapidapi.com/api/weather/" + city

headers = {
    "X-RapidAPI-Key": "d1239a423fmshf641e8dd5f79ef7p1efa59jsn63f33f4786cf",
    "X-RapidAPI-Host": "the-weather-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Try to parse the JSON response
    try:
        data = response.json()
        if data.get('success', False):
            weather_data = data.get('data', {})
            print("City:", city.capitalize())
            print("Current Weather:", weather_data.get('current_weather'))
            print("Temperature:", weather_data.get('temp') + "°C")
            print("Expected Temperature:", weather_data.get('expected_temp'))
            # Print other relevant information

        else:
            print("Request was not successful. Check the provided city name.")

    except Exception as e:
        print("Error parsing JSON response:", str(e))

else:
    print("Error in the request. Status Code:", response.status_code)
    
    