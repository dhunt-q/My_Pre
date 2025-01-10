import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(player_stats, opponent_stats):
    # Convert to DataFrame
    player_df = pd.DataFrame(player_stats)
    opponent_df = pd.DataFrame(opponent_stats)

    # Merge player and opponent data
    merged_df = pd.merge(player_df, opponent_df, on="team_id")

    # Add rolling averages
    merged_df["avg_points_last_5"] = (
        player_df.groupby("player_id")["points"].rolling(5).mean().reset_index(drop=True)
    )

    # Normalize data
    scaler = StandardScaler()
    merged_df[["avg_points_last_5", "opponent_def_eff"]] = scaler.fit_transform(
        merged_df[["avg_points_last_5", "opponent_def_eff"]]
    )
    return merged_df

# Example usage:
# player_stats = pd.read_csv("data/player_stats.csv")
# opponent_stats = pd.read_csv("data/opponent_stats.csv")
# processed_data = preprocess_data(player_stats, opponent_stats)
# processed_data.to_csv("data/processed_data.csv", index=False)
