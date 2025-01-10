import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import os

def train_model():
    # Load processed data
    data = pd.read_csv("data/processed_data.csv")

    # Features and target
    X = data[["avg_points_last_5", "opponent_def_eff", "minutes_played"]]
    y = data["points"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error: {mse}")

    # Save model
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/player_stats_model.pkl")
    print("Model saved to models/player_stats_model.pkl")

if __name__ == "__main__":
    train_model()


# Example usage:
# train_model("data/processed_data.csv", "models/player_stats_model.pkl")
