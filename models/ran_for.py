import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# --- Charger ton CSV ---
df = pd.read_csv("/Users/juliane/Desktop/Projet dabdab/FinanceJR/helpers/data/KER_2025.csv")

# --- Préparation des features ---
df["return"] = df["AdjClose"].pct_change()
df["MA5"] = df["AdjClose"].rolling(5).mean()
df["MA10"] = df["AdjClose"].rolling(10).mean()
df["Vol5"] = df["return"].rolling(5).std()
df["Vol10"] = df["return"].rolling(10).std()
df["DeltaVol"] = df["Volume"].pct_change()
df["RatioPriceMA10"] = df["AdjClose"] / df["MA10"]

# --- Cible : prix du lendemain ---
df["target"] = df["AdjClose"].shift(-1)

df = df.dropna()

X = df[["return", "MA5", "MA10", "Vol5", "Vol10", "DeltaVol", "RatioPriceMA10"]]
y = df["target"]

# --- Split temporel ---
train_size = int(len(df) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# --- Random Forest ---
model = RandomForestRegressor(n_estimators=200, max_depth=8, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)
pred = model.predict(X_test)

# --- Évaluation ---
mae = mean_absolute_error(y_test, pred)
r2 = r2_score(y_test, pred)
print(f"MAE: {mae:.2f}")
print(f"R²: {r2:.3f}")

# --- Importance des features ---
importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nImportance des variables :")
print(importances)

# --- Graphique ---
plt.figure(figsize=(10,5))
plt.plot(y_test.index, y_test, label="Réel", color="blue")
plt.plot(y_test.index, pred, label="Prédit", color="orange")
plt.title("Prédiction du prix (Random Forest)")
plt.legend()
plt.show()