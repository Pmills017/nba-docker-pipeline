import requests
import os

API_KEY = os.getenv("API_KEY")
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "nba-api-free-data.p.rapidapi.com"
}

def check_atlantic_teams():
    url = "https://rapidapi.com"
    print("Connecting to live sports API endpoint...")
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        print("Connection Successful! Ingesting data payload:")
        print(response.text)
    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    check_atlantic_teams()
