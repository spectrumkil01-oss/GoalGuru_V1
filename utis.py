import plotly.graph_objects as go

def plot_outcome_bar(home, draw, away):
    """Plot bar chart of outcome probabilities"""
    fig = go.Figure([go.Bar(x=['Home', 'Draw', 'Away'], y=[home, draw, away],
                            marker_color=['green', 'gray', 'red'])])
    fig.update_layout(title='GoalGuru – Match Outcome Probabilities', yaxis=dict(title='Probability'))
    return fig

def expected_value(prob, odds):
    """Calculate Expected Value vs odds"""
    return (prob * odds) - 1

def highlight_scores(prob, threshold=0.1):
    """Add check mark if probability exceeds threshold"""
    return '✅' if prob > threshold else ''
