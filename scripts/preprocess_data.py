import pandas as pd
import json
import os

def preprocess_data():
    try:
        # Step 1: Load JSON file
        print("Loading player profile JSON file...")
        with open("data/player_profile.json", "r") as f:
            player_stats = json.load(f)
        print("Player profile loaded successfully!")

        # Step 2: Convert to DataFrame
        print("Converting player data to DataFrame...")
        player_data = pd.json_normalize(player_stats)
        print("Player DataFrame created:")
        print(player_data.head())  # Display the first few rows of the DataFrame

        # Step 3: Extract and flatten the nested "seasons" field
        print("Extracting and flattening 'seasons' field...")
        if "seasons" not in player_data.columns:
            raise KeyError("'seasons' field is missing in the data!")
        
        seasons = player_data.loc[0, "seasons"]
        if not isinstance(seasons, list):
            raise ValueError("'seasons' field is not a list as expected!")
        
        seasons_data = pd.json_normalize(
            seasons, 
            record_path=["teams"],  # Extract nested teams data
            meta=["year", "type"],  # Include season year and type
            sep="_"
        )
        print("'Seasons' DataFrame created:")
        print(seasons_data.head())  # Display the first few rows

        # Debug: Check available columns
        print("Available columns in 'seasons_data':")
        print(seasons_data.columns.tolist())

        # Step 4: Extract relevant metrics
        print("Processing metrics for modeling...")
        required_columns = ["year", "type", "name", "total_points", "total_minutes", "total_field_goals_made", "total_rebounds"]
        
        # Handle missing columns gracefully
        missing_columns = [col for col in required_columns if col not in seasons_data.columns]
        if missing_columns:
            raise KeyError(f"The following required columns are missing: {missing_columns}")
        
        seasons_data = seasons_data[required_columns]
        print("Metrics extracted successfully:")
        print(seasons_data.head())

        # Rename columns for clarity
        seasons_data.rename(columns={"total_points": "points", "total_minutes": "minutes_played"}, inplace=True)

        # Create additional columns
        print("Creating additional calculated columns...")
        seasons_data["avg_points_last_5"] = seasons_data["points"].rolling(5).mean()  # Average points over last 5 games
        seasons_data["opponent_def_eff"] = 1.0  # Placeholder; Replace with real defensive efficiency data
        print("Additional columns created:")
        print(seasons_data.head())  # Display the updated DataFrame

        # Step 5: Save processed data
        print("Saving processed data to 'data/processed_data.csv'...")
        os.makedirs("data", exist_ok=True)
        seasons_data.to_csv("data/processed_data.csv", index=False)
        print("Processed data saved successfully!")

    except Exception as e:
        print(f"Error during preprocessing: {e}")

if __name__ == "__main__":
    preprocess_data()
