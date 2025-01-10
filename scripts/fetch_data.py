import pandas as pd
import requests
import json
import time
import os
from datetime import datetime

API_KEY = "nLmHHrq9xy48tW9T4fMDd6lbO83FjfchuCt4BP6D"
BASE_URL = "https://api.sportradar.us/nba/trial/v7/en"

def fetch_schedule():
    """Fetch today's game schedule from SportsRadar."""
    today = datetime.today().strftime('%Y/%m/%d')
    url = f"{BASE_URL}/games/{today}/schedule.json?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        schedule = response.json()
        games = []
        for game in schedule['games']:
            games.append({
                'game_id': game['id'],
                'home_team': game['home']['name'],
                'away_team': game['away']['name'],
                'scheduled_time': game['scheduled'],
            })
        return pd.DataFrame(games)
    else:
        print(f"Error fetching schedule: {response.status_code}")
        return pd.DataFrame()

def fetch_injury_reports():
    """Fetch injury reports for all teams."""
    url = f"{BASE_URL}/league/injuries.json?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        injury_data = response.json()
        injuries = []
        for team in injury_data['teams']:
            for player in team['players']:
                # Safely check for the 'injury' key
                injury = player.get('injury', {})
                injuries.append({
                    'player_id': player['id'],
                    'player_name': player['full_name'],
                    'team': team['name'],
                    'position': player.get('primary_position', 'N/A'),
                    'injury': injury.get('description', 'None'),
                    'status': injury.get('status', 'Healthy'),
                })
        return pd.DataFrame(injuries)
    else:
        print(f"Error fetching injuries: {response.status_code}")
        return pd.DataFrame()

def fetch_player_stats(player_id):
    """Fetch player stats for a given player."""
    url = f"{BASE_URL}/players/{player_id}/profile.json?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        player_data = response.json()
        stats = []
        for season in player_data['seasons']:
            if 'teams' in season:
                for team in season['teams']:
                    if 'statistics' in team:
                        stats.append({
                            'season': season['year'],
                            'team': team['name'],
                            'games_played': team['statistics']['games_played'],
                            'points_per_game': team['statistics']['average']['points'],
                            'rebounds_per_game': team['statistics']['average']['rebounds'],
                            'assists_per_game': team['statistics']['average']['assists'],
                            'blocks_per_game': team['statistics']['average']['blocks'],
                            'steals_per_game': team['statistics']['average']['steals'],
                        })
        return pd.DataFrame(stats)
    else:
        print(f"Error fetching player stats: {response.status_code}")
        return pd.DataFrame()

if __name__ == "__main__":
    # Fetch today's schedule
    print("Fetching today's schedule...")
    schedule = fetch_schedule()
    schedule.to_json('data/schedule.json', orient='records')

    # Fetch injury reports
    print("Fetching injury reports...")
    injuries = fetch_injury_reports()
    injuries.to_json('data/injury_data.json', orient='records')

    # Fetch player stats for all players playing today
    print("Fetching player stats...")
    player_stats = []
    for game in schedule.itertuples():
        home_team = game.home_team
        away_team = game.away_team
        print(f"Fetching players for {home_team} and {away_team}...")
        # Example logic: fetch players for both teams and their stats (use real IDs)
        # Add your player fetching logic here!
    # player_stats.to_csv('data/player_stats.csv', index=False)
    print("Data fetched and saved!")

