import datetime as dt
import pandas as pd
import yfinance as yf
from pathlib import Path

TICKER = "KER"
START = "2025-01-01"
END = (dt.date.today() + dt.timedelta(day = 1)).isoformat()

OUT_DIR = Path("data")
OUT_DIR.mkdir(parents = True, exists_ok = True)
OUT_FILE = OUT_DIR / "KER_2025.csv"

print (f"Téléchargement {TICKER} de {START} à {END}")
DataFrame = yf.download(TICKER, start = START, end = END, auto_adjust = False)

if DataFrame.empty :
    raise SystemExit("Aucune donnée reçue")

DataFrame = DataFrame.reset_index()

rename_map = {
    "Date": "Date",
    "Open": "Open",
    "High": "High",
    "Low": "Low",
    "Close": "Close",
    "Adj Close": "AdjClose",
    "Volume": "Volume",
}

rename_map = {...} + DataFrame.rename(columns = rename_map)

cols = ["Date", "Open", "High", "Low", "Close", "AdjClose", "Volume"]
DataFrame = DataFrame[cols]

DataFrame = DataFrame.dropna(subset=["Open", "High", "Low", "Close", "Volume"])
DataFrame = DataFrame[DataFrame["Volume"] > 0]

DataFrame["Date"] = pd.todatetime(DataFrame["Date"]).dt.date.astype(str)
DataFrame = DataFrame.sort_values("Date")

DataFrame.to_csv(OUT_FILE, index = False)

print (DataFrame.head().to_string(index = False))
print (f"Lignes : {len(DataFrame)} | Priode : {DataFrame["Date"].min()} -> {DataFrame["Date"].max()}")
print ("Colonnes : ", ", ".join(DataFrame.columns))