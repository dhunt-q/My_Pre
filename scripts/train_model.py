import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

def train_model(data_path, model_path):
    # Load processed data
    data = pd.read_csv(data_path)

    # Features and target
    X = data[["avg_points_last_5", "opponent_def_eff", "minutes_played"]]
    y = data["points"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Model Mean Squared Error: {mse}")

    # Save the model
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

# Example usage:
# train_model("data/processed_data.csv", "models/player_stats_model.pkl")
