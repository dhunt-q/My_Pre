import pandas as pd
import requests

API_KEY = "nLmHHrq9xy48tW9T4fMDd6lbO83FjfchuCt4BP6D"
BASE_URL = "https://api.sportradar.com/nba/production/v8/en"


def fetch_data(endpoint):
    """
    Fetch data from Sportradar API.

    Args:
        endpoint (str): The API endpoint (relative to BASE_URL).

    Returns:
        dict: JSON response if the request is successful, otherwise None.
    """
    url = f"{BASE_URL}/{endpoint}"
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, headers=headers, params={"api_key": API_KEY})
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None


# Fetch different types of data using the function
if __name__ == "__main__":
    # Fetch team rankings for the 2024 regular season
    rankings = fetch_data("seasons/2024/REG/rankings.json")
    print("Rankings:", rankings)

    # Fetch player profile
    player_profile = fetch_data("players/8ec91366-faea-4196-bbfd-b8fab7434795/profile.json")
    print("Player Profile:", player_profile)

    # Fetch season leaders for 2023 regular season
    season_leaders = fetch_data("seasons/2023/REG/leaders.json")
    print("Season Leaders:", season_leaders)

    # Fetch league hierarchy
    league_hierarchy = fetch_data("league/hierarchy.json")
    print("League Hierarchy:", league_hierarchy)

    # Fetch game summary
    game_summary = fetch_data("games/aaa3ddb3-dd1b-459e-a686-d2bfc4408881/summary.json")
    print("Game Summary:", game_summary)

    # Fetch game play-by-play (PBP)
    game_pbp = fetch_data("games/aaa3ddb3-dd1b-459e-a686-d2bfc4408881/pbp.json")
    print("Game PBP:", game_pbp)

    # Fetch game boxscore
    game_boxscore = fetch_data("games/aaa3ddb3-dd1b-459e-a686-d2bfc4408881/boxscore.json")
    print("Game Boxscore:", game_boxscore)
