import numpy as np
from scipy.stats import poisson

def calculate_lambda(df, team):
    home_matches = df[df['HomeTeam'] == team]
    away_matches = df[df['AwayTeam'] == team]
    home_lambda = home_matches['HomeGoals'].mean() if not home_matches.empty else 1.0
    away_lambda = away_matches['AwayGoals'].mean() if not away_matches.empty else 1.0
    return home_lambda, away_lambda

def poisson_matrix(home_lambda, away_lambda, max_goals=5):
    matrix = np.zeros((max_goals+1, max_goals+1))
    for h in range(max_goals+1):
        for a in range(max_goals+1):
            matrix[h, a] = poisson.pmf(h, home_lambda) * poisson.pmf(a, away_lambda)
    return matrix

def outcome_probabilities(matrix):
    home_win = np.sum(np.tril(matrix, -1))
    draw = np.sum(np.diag(matrix))
    away_win = np.sum(np.triu(matrix, 1))
    return home_win, draw, away_win

def top_scorelines(matrix, top_n=5):
    flat_index = np.argsort(matrix.flatten())[::-1][:top_n]
    scores = [(i//matrix.shape[0], i%matrix.shape[1], matrix[i//matrix.shape[0], i%matrix.shape[1]]) for i in flat_index]
    return scores
