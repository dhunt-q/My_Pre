import requests
import json
import time
import os

API_KEY = "nLmHHrq9xy48tW9T4fMDd6lbO83FjfchuCt4BP6D"
BASE_URL = "https://api.sportradar.com/nba/production/v8/en"

def fetch_data(endpoint, filename):
    url = f"{BASE_URL}/{endpoint}"
    headers = {"accept": "application/json"}
    try:
        response = requests.get(url, headers=headers, params={"api_key": API_KEY})
        if response.status_code == 429:  # Too Many Requests
            retry_after = int(response.headers.get("Retry-After", 2))
            print(f"Rate limit hit. Retrying after {retry_after} seconds...")
            time.sleep(retry_after)
            return fetch_data(endpoint, filename)  # Retry
        response.raise_for_status()
        data = response.json()
        save_to_json(data, filename)
        return data
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

def save_to_json(data, filename):
    os.makedirs("data", exist_ok=True)
    with open(f"data/{filename}", "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to data/{filename}")

if __name__ == "__main__":
    # Fetch different data
    fetch_data("seasons/2024/REG/rankings.json", "rankings.json")
    time.sleep(2)
    fetch_data("players/8ec91366-faea-4196-bbfd-b8fab7434795/profile.json", "player_profile.json")
    time.sleep(2)
    fetch_data("seasons/2023/REG/leaders.json", "season_leaders.json")
    time.sleep(2)

