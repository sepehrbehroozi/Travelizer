import requests

def get_country_flag(country_name):
    # API request
    api_url = f'https://restcountries.com/v3.1/name/{country_name}'

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad responses

        data = response.json()

        if data:
            flag_url = data[0]['flags']['png']
            print(f"Flag URL for {country_name}: {flag_url}")
            # You can now use this URL to download or display the flag image

        else:
            print(f"Flag not found for the specified country: {country_name}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    country_name = input("Enter a country name: ")
    get_country_flag(country_name)
 