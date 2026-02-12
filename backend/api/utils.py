import os
import pandas as pd

# Base directory is backend folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_historical_prices():
    path = os.path.join(BASE_DIR, "..", "data", "processed", "brent_log_returns_model.csv")
    return pd.read_csv(path, parse_dates=["Date"])

def load_change_points():
    path = os.path.join(BASE_DIR, "..", "data", "processed", "change_points.csv")
    return pd.read_csv(path, parse_dates=["change_date", "lower_date", "upper_date"])

def load_key_events():
    path = os.path.join(BASE_DIR, "..", "data", "key_events.csv")
    return pd.read_csv(path, parse_dates=["date"])
