import datetime as dt
import pandas as pd
import yfinance as yf
from pathlib import Path

TICKER = "KER.PA"
START = "2025-01-01"
END = (dt.date.today() + dt.timedelta(days = 1)).isoformat()

OUT_DIR = Path("data")
OUT_DIR.mkdir(parents = True, exist_ok = True)
OUT_FILE = OUT_DIR / "KER_2025.csv"

def loadcsv():
    print (f"Téléchargement {TICKER} de {START} à {END}")
    df = yf.download(TICKER, start = START, end = END, auto_adjust = False)

    if df.empty :
        raise SystemExit("Aucune donnée reçue")

    df = df.reset_index()

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    print("Colonnes après flatten :", list(df.columns))  # debug

    rename_map = {
        "Date": "Date",
        "Open": "Open",
        "High": "High",
        "Low": "Low",
        "Close": "Close",
        "Adj Close": "AdjClose",
        "Volume": "Volume",
    }
    df = df.rename(columns=rename_map)

    if "AdjClose" not in df.columns and "Close" in df.columns:
        df["AdjClose"] = df["Close"]

    wanted = ["Date", "Open", "High", "Low", "Close", "AdjClose", "Volume"]
    present = [c for c in wanted if c in df.columns]
    df = df[present]

    subset_clean = [c for c in ["Open", "High", "Low", "Close", "Volume"] if c in df.columns]
    if subset_clean:
        df = df.dropna(subset=subset_clean)
        if "Volume" in df.columns:
            df = df[df["Volume"] > 0]

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors = "coerce").dt.date.astype(str)
        df = df.sort_values("Date")

    df.to_csv(OUT_FILE, index=False)
    print(f"Fichier sauvegardé -> {OUT_FILE.resolve()}")
    print("\nAperçu :")
    print(df.head().to_string(index=False))
    print("\nInfos :")
    print(f"Lignes : {len(df)} | Période : {df['Date'].min()} -> {df['Date'].max()}")
    print("Colonnes :", ", ".join(df.columns))

    return (df)