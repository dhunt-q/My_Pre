import pandas as pd
import os

def preprocess_data():
    try:
        # Load data
        player_stats = pd.read_json("data/player_profile.json")
        
        # Example: Extract necessary columns
        processed_data = pd.json_normalize(player_stats, sep="_")
        
        # Save processed data
        os.makedirs("data", exist_ok=True)
        processed_data.to_csv("data/processed_data.csv", index=False)
        print("Processed data saved to data/processed_data.csv")
    except Exception as e:
        print(f"Error during preprocessing: {e}")

if __name__ == "__main__":
    preprocess_data()


# Example usage:
# player_stats = pd.read_csv("data/player_stats.csv")
# opponent_stats = pd.read_csv("data/opponent_stats.csv")
# processed_data = preprocess_data(player_stats, opponent_stats)
# processed_data.to_csv("data/processed_data.csv", index=False)
