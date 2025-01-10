import requests

API_KEY = "nLmHHrq9xy48tW9T4fMDd6lbO83FjfchuCt4BP6D"
BASE_URL = "https://api.sportradar.com/nba/trial/v8/en"

def fetch_player_stats(player_id):
    url = f"{BASE_URL}/players/{player_id}/profile.json"
    response = requests.get(url, params={"api_key": API_KEY})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching player stats: {response.status_code}, {response.text}")
        return None

def fetch_opponent_stats(team_id):
    url = f"{BASE_URL}/teams/{team_id}/profile.json"
    response = requests.get(url, params={"api_key": API_KEY})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching opponent stats: {response.status_code}, {response.text}")
        return None

def fetch_upcoming_games():
    today = pd.Timestamp.now().strftime("%Y/%m/%d")
    url = f"{BASE_URL}/games/{today}/schedule.json"
    response = requests.get(url, params={"api_key": API_KEY})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching upcoming games: {response.status_code}, {response.text}")
        return None
