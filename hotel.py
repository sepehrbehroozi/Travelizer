import requests

url = "https://hotels4.p.rapidapi.com/locations/search"
city = input("enter name of city: ")
querystring = {"query": city, "locale": "en_US"}

headers = {
    "X-RapidAPI-Key": "49212aa93emshb997e86a06ade4ep1618a6jsnc5c7d3fa5148",
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json() 

# Extracting the names of the top 3 hotels
top_3_hotels = []

for suggestion in data.get("suggestions", [])[:3]:
    hotels = suggestion.get('entities', [])
    for hotel in hotels:
        hotel_name = hotel.get('name', '')
        if hotel_name and len(top_3_hotels) <= 3:
            top_3_hotels.append(hotel_name)

for hotel_name in top_3_hotels:
    print(hotel_name)
