import requests

url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchAirport"

current_city = input("Enter current city name: ")
destination_city = input("Enter destination city name: ")
querystring = {"query": current_city}


headers = {
    "X-RapidAPI-Key": "0916e7c493mshac98414bf7ef0dcp10608ajsn34ef6e8d81d7",
    "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
}

#Current city
response = requests.get(url, headers=headers, params=querystring)
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    json_data = response.json()
    # Check if 'data' key exists in the JSON response
    if 'data' in json_data: 
        # Check if 'children' key exists in the 'data' dictionary
        if 'children' in json_data['data'][0]:
            # Access the first element's 'airportCode'
            current_airport_code = json_data['data'][0]['children'][0]['airportCode']
            print(f"Aiport Code for {current_city}: {current_airport_code}")
        else:
            print("No 'children' key found in the 'data' dictionary.")
    else:
        print("No 'data' key found in the JSON response.")
else:
    print(f"Request failed with status code {response.status_code}")

#Destination city
querystring = {"query": destination_city}

headers = {
    "X-RapidAPI-Key": "0916e7c493mshac98414bf7ef0dcp10608ajsn34ef6e8d81d7",
    "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
# Check if the request was successful (status code 200)
if response.status_code == 200: 
    # Parse the JSON response
    json_data = response.json()
    # Check if 'data' key exists in the JSON response
    if 'data' in json_data:
        # Check if 'children' key exists in the 'data' dictionary
        if 'children' in json_data['data'][0]:
            # Access the first element's 'airportCode'
            destination_airport_code = json_data['data'][0]['children'][0]['airportCode']
            print(f"Aiport Code for {destination_city}: {destination_airport_code}")
        else:
            print("No 'children' key found in the 'data' dictionary.")
    else:
        print("No 'data' key found in the JSON response.")
else:
    print(f"Request failed with status code {response.status_code}")
