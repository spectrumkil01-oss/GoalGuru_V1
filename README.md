 # GoalGuru V1

GoalGuru V1 is the first version of the football prediction app.  
It predicts **exact match scores**, **outcome probabilities** (Home/Draw/Away), and suggests **value bets** using historical match data.

## Features
- Single match prediction
- Team-specific goal expectations (λ)
- Poisson + Dixon–Coles prediction
- Top scorelines with probabilities
- EV calculation vs bookmaker odds
- Bar chart visualization of outcome probabilities
- Mobile-friendly layout

## Getting Started

### Prerequisites
- Python 3.9+
- Streamlit

### Installation
```bash
git clone <YOUR_GITHUB_REPO_URL>
cd GoalGuru_V1
pip install -r requirements.txt
streamlit run app.py
