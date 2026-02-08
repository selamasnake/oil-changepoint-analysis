# oil-changepoint-analysis

### Overview

This project analyzes Brent crude oil prices to detect structural changes (change points) in the time series and associate these changes with major geopolitical, economic, and OPEC-related events. The goal is to provide data-driven insights for investors, policymakers, and energy analysts to better understand market behavior and respond to shocks.

The analysis covers daily Brent prices from May 20, 1987, to September 30, 2022, using Bayesian change point models implemented in PyMC. A secondary dataset of 15 key events captures major crises, conflicts, and policy decisions affecting oil prices.

### Datasets

* `brent_prices.csv`: Daily Brent crude prices (Date, Price in USD per barrel).
* `key_events.csv`: 15 key events affecting oil prices, including date, event description, and category (Geopolitical, Economic, OPEC Policy, Supply Shock, Sanctions).

### Project Workflow

1. Data Loading & Cleaning: Convert dates, handle missing values, and sort chronologically.
2. Exploratory Data Analysis: Visualize trends, compute log returns, and examine volatility patterns.
3. Event Alignment: Map key geopolitical, economic, and OPEC events to the time series.
4. Change Point Modeling (Task 2): Apply Bayesian switch-point models to detect structural changes.
5. Interpretation & Reporting: Quantify the impact of change points and associate them with events.
6. Dashboard (Task 3): Interactive visualization of price trends, change points, and event highlights.

