import joblib
import pandas as pd

def predict_stats(model_path, avg_points, opponent_def_eff, minutes_played):
    # Load the trained model
    model = joblib.load(model_path)

    # Prepare input data
    input_data = pd.DataFrame(
        {"avg_points_last_5": [avg_points], "opponent_def_eff": [opponent_def_eff], "minutes_played": [minutes_played]}
    )

    # Make prediction
    prediction = model.predict(input_data)
    return prediction[0]
