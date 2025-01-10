import joblib
import pandas as pd

def predict_stats(model_path, avg_points, opponent_def_eff, minutes_played):
    model = joblib.load(model_path)
    input_data = pd.DataFrame({
        "avg_points_last_5": [avg_points],
        "opponent_def_eff": [opponent_def_eff],
        "minutes_played": [minutes_played]
    })
    prediction = model.predict(input_data)
    return prediction[0]

if __name__ == "__main__":
    prediction = predict_stats("models/player_stats_model.pkl", 25.4, 1.05, 34)
    print(f"Predicted Points: {prediction}")

