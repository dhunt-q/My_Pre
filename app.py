import streamlit as st
from scripts.predict_stats import predict_stats

st.title("NBA Player Stats Predictor")

# Input fields
player_name = st.text_input("Player Name", "LeBron James")
avg_points = st.number_input("Average Points in Last 5 Games", value=25.4, step=0.1)
opponent_def_eff = st.number_input("Opponent Defense Efficiency", value=1.05, step=0.01)
minutes_played = st.number_input("Expected Minutes Played", value=34, step=1)

# Predict button
if st.button("Predict"):
    try:
        prediction = predict_stats("models/player_stats_model.pkl", avg_points, opponent_def_eff, minutes_played)
        st.write(f"Predicted Points for {player_name}: {prediction:.2f}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

