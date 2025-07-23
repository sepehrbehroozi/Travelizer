import requests

print("***HEALTH***")
country = input("Enter the country name: ")

url = "https://covid-193.p.rapidapi.com/statistics"

querystring = {"country": country}

headers = {
    "X-RapidAPI-Key": "d1239a423fmshf641e8dd5f79ef7p1efa59jsn63f33f4786cf",
    "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()  # Convert response to JSON

# Check if 'response' key exists in the data
if 'response' in data:
    # Check if the 'response' list is not empty
    if data['response']:
        # Access the first item in the 'response' list
        first_response = data['response'][0]
        
        # Access the 'cases' dictionary within the first response
        cases = first_response.get('cases', {})

        # Access the 'active' value within the 'cases' dictionary
        active_cases = cases.get('active')

        if active_cases is not None:
            if active_cases > 5000:
                print(f"There are {active_cases} active cases in {country}.")
                print("It is recommended that you social distance for this trip and carry face masks to lower chances of getting the COVID-19 virus")
        else:
            print(f"No active cases data available for {country}")
    else:
        print(f"No data available for {country}")
else:
    print(f"Error in API response for {country}: {data.get('errors', 'Unknown error')}")
 
    
    
