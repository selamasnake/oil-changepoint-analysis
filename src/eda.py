# eda.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller


class EDA:
    """Class for initial EDA"""
    def load_data(self, path):
        """Load CSV and sort by date."""
        try:
            df = pd.read_csv(path)
            df['Date'] = pd.to_datetime(df['Date'])
            df = df.sort_values('Date')
            return df
        except FileNotFoundError:
            print(f"Error: {path} not found.")
            return None

    def compute_log_returns(self, df, price_col='Price'):
        """Add log returns column."""
        df['log_return'] = np.log(df[price_col]).diff()
        return df
    
    def compute_rolling_volatility(self, df, return_col='log_return', window=30):
        """
        Compute rolling volatility (standard deviation of log returns).
        """
        df['volatility'] = df[return_col].rolling(window=window).std()
        return df

    def adf_test(self, series, col_name='Series'):
        """Run Augmented Dickey-Fuller test and print results."""
        result = adfuller(series.dropna())
        print(f"ADF Test for {col_name}")
        print(f"  ADF Statistic: {result[0]:.4f}")
        print(f"  p-value: {result[1]:.4f}")
        print(f"  Critical Values: {result[4]}")
        if result[1] < 0.05:
            print("  => The series is stationary")
        else:
            print("  => The series is non-stationary")
