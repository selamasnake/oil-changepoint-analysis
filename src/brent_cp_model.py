import pandas as pd
import numpy as np
import pymc as pm
import arviz as az
import matplotlib.pyplot as plt
import seaborn as sns

class BrentChangePointModel:
    def __init__(self, data_filepath):
        """
        Initialize the model with a CSV file containing Date and log_return columns.
        """
        self.model_df = pd.read_csv(data_filepath, parse_dates=["Date"])
        self.returns = self.model_df["log_return"].values
        self.time_idx = np.arange(len(self.returns))
        self.trace = None
        self.tau_samples = None
        self.tau_median = None
        self.change_date = None
        self.lower_date = None
        self.upper_date = None

    # -----------------------------
    # 1. Run Single Change Point Model
    # -----------------------------
    def run_single_cp_model(self, draws=3000, tune=2000, target_accept=0.95):
        """
        Build and sample a Bayesian single change point model.
        """
        with pm.Model() as model:

            # Single change point prior
            tau = pm.DiscreteUniform("tau", lower=0, upper=len(self.returns)-1)

            # Means before and after
            mu_1 = pm.Normal("mu_1", mu=0.0, sigma=0.02)
            mu_2 = pm.Normal("mu_2", mu=0.0, sigma=0.02)

            # Shared volatility
            sigma = pm.HalfNormal("sigma", sigma=0.02)

            # Assign mean to each time point
            mu_t = pm.math.switch(self.time_idx < tau, mu_1, mu_2)

            # Likelihood
            obs = pm.Normal("obs", mu=mu_t, sigma=sigma, observed=self.returns)

            # Sampling
            self.trace = pm.sample(
                draws=draws,
                tune=tune,
                target_accept=target_accept,
                return_inferencedata=True
            )
        return self.trace

    # -----------------------------
    # 2. Summarize Trace
    # -----------------------------
    def summarize_trace(self):
        """
        Print summary and plot traces of the model.
        """
        if self.trace is None:
            raise ValueError("Run the model first with run_single_cp_model()")

        summary = az.summary(self.trace, var_names=["mu_1","mu_2","sigma","tau"])
        print(summary)
        az.plot_trace(self.trace, var_names=["mu_1","mu_2","sigma","tau"])
        plt.show()

    # -----------------------------
    # 3. Extract Change Point
    # -----------------------------
    def extract_change_point(self):
        """
        Extract median change point and 95% credible interval.
        """
        if self.trace is None:
            raise ValueError("Run the model first with run_single_cp_model()")
        
        self.tau_samples = self.trace.posterior["tau"].stack(samples=("chain", "draw")).values
        self.tau_median = int(np.median(self.tau_samples))
        self.change_date = self.model_df["Date"].iloc[self.tau_median]

        tau_hdi = az.hdi(self.tau_samples, hdi_prob=0.95)
        lower_idx, upper_idx = int(tau_hdi[0]), int(tau_hdi[1])
        self.lower_date, self.upper_date = self.model_df["Date"].iloc[lower_idx], self.model_df["Date"].iloc[upper_idx]

        return self.change_date, self.lower_date, self.upper_date, self.tau_median

    # -----------------------------
    # 4. Plot Tau Posterior
    # -----------------------------
    def plot_tau_posterior(self):
        if self.tau_samples is None or self.tau_median is None:
            raise ValueError("Call extract_change_point() first")
        plt.figure(figsize=(12,5))
        sns.histplot(self.tau_samples, bins=50, kde=True, color="skyblue")
        plt.axvline(self.tau_median, color='red', linestyle='--', label='Median Tau')
        plt.title("Posterior Distribution of Change Point")
        plt.xlabel("Time Index")
        plt.ylabel("Density")
        plt.legend()
        plt.show()

    # -----------------------------
    # 5. Quantify Impact
    # -----------------------------
    def quantify_impact(self):
        if self.trace is None:
            raise ValueError("Run the model first with run_single_cp_model()")
        mu1 = self.trace.posterior["mu_1"].mean().values
        mu2 = self.trace.posterior["mu_2"].mean().values
        delta = mu2 - mu1

        print(f"Average daily log return before change point (mu_1): {mu1:.5f}")
        print(f"Average daily log return after change point (mu_2): {mu2:.5f}")
        print(f"Change in daily log return: {delta:.5f}")
        print(f"Approximate % change in daily return: {delta*100:.3f}%")

        az.plot_posterior(self.trace, var_names=["mu_1","mu_2"], hdi_prob=0.95)
        plt.show()
        
        return mu1, mu2, delta

    # -----------------------------
    # 6. Match Events
    # -----------------------------
    def match_events(self, events_filepath):
        events = pd.read_csv(events_filepath, parse_dates=["date"])
        events["days_diff"] = (events["date"] - self.change_date).dt.days.abs()

        closest_event = events.iloc[events["days_diff"].argsort()[:1]]

        events_in_interval = events[(events["date"] >= self.lower_date) & (events["date"] <= self.upper_date)]

        print("\nClosest Event:")
        print(f"Change point: {self.change_date}")
        print(f"Event: {closest_event['event'].values[0]}")
        print(f"Event Date: {closest_event['date'].values[0]}")
