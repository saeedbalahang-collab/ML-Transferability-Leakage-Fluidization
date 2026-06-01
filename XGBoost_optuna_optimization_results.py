!pip install optuna
import pickle
import optuna

with open("hydraulics_optuna.pkl", "rb") as f:
    import joblib
    study = joblib.load("hydraulics_optuna.pkl")

for trial in study.trials:
    print(f"Trial {trial.number}: params={trial.params}, value={trial.value}")
import pandas as pd

rows = []

for trial in study.trials:
    row = {
        "trial": trial.number,
        "value": trial.value,
    }
    row.update(trial.params)
    rows.append(row)

df = pd.DataFrame(rows)

df.to_csv("optuna_results.csv", index=False)
