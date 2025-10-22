import streamlit as st
import pandas as pd
from predictor import calculate_lambda, poisson_matrix, outcome_probabilities, top_scorelines
from utils import plot_outcome_bar, expected_value, highlight_scores

st.set_page_config(page_title="GoalGuru V1", layout="wide")
st.title("GoalGuru V1 – Single Match Prediction")
st.subheader("Predict exact scores and outcome probabilities for one match at a time")

# --- Load League Data ---
league_file = st.selectbox("Select League CSV", ["data/league1.csv", "data/league2.csv"])
df = pd.read_csv(league_file)

# --- Select Match ---
teams = list(set(df['HomeTeam']).union(set(df['AwayTeam'])))
home_team = st.selectbox("Select Home Team", teams)
away_team = st.selectbox("Select Away Team", [team for team in teams if team != home_team])

# --- Calculate λ ---
if st.button("Predict Match"):
    home_lambda, away_lambda = calculate_lambda(df, home_team)
    
    # Poisson Matrix
    matrix = poisson_matrix(home_lambda, away_lambda, max_goals=5)
    
    # Outcome Probabilities
    home_prob, draw_prob, away_prob = outcome_probabilities(matrix)
    
    # Top Scorelines
    top_scores = top_scorelines(matrix)
    
    st.write(f"**Prediction for {home_team} vs {away_team}**")
    st.write(f"Home Win Probability: {home_prob:.2f}")
    st.write(f"Draw Probability: {draw_prob:.2f}")
    st.write(f"Away Win Probability: {away_prob:.2f}")
    
    st.write("**Top Scorelines:**")
    for score in top_scores:
        st.write(f"{score[0]} - {score[1]} | Probability: {score[2]:.2f} {highlight_scores(score[2])}")
    
    # Plot Outcome Probabilities
    st.plotly_chart(plot_outcome_bar(home_prob, draw_prob, away_prob), use_container_width=True)
    
    # Example EV Calculation (assuming sample odds)
    sample_odds = {"Home": 2.0, "Draw": 3.0, "Away": 4.0}
    ev_home = expected_value(home_prob, sample_odds["Home"])
    ev_draw = expected_value(draw_prob, sample_odds["Draw"])
    ev_away = expected_value(away_prob, sample_odds["Away"])
    
    st.write(f"**Expected Value (EV) vs Sample Odds:**")
    st.write(f"Home: {ev_home:.2f}, Draw: {ev_draw:.2f}, Away: {ev_away:.2f}")
