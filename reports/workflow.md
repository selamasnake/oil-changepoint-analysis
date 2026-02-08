# Laying the Foundation for Brent Oil Price Analysis

## 1. Introduction & Business Context
Brent crude oil prices drive global energy markets, influencing investment, policy, and operational decisions. Prices are volatile, affected by geopolitical conflicts, economic shocks, supply disruptions, and OPEC policy changes.

As a data scientist at **Birhan Energies**, a consultancy specializing in energy markets, this analysis aims to detect structural changes (change points) in daily Brent prices (May 20, 1987 – Sept 30, 2022) and link them to key geopolitical and economic events to support data-driven insights for stakeholders.

## 2. Data Overview
- **Primary dataset:** Daily Brent crude oil prices (Date, Price in USD per barrel).
- **Event dataset:** 15 key events compiled, including geopolitical conflicts, economic shocks, OPEC policy changes, and supply disruptions.

| Date       | Event                                | Category               |
|------------|--------------------------------------|------------------------|
| 1990-08-02 | Iraq invades Kuwait (Gulf War)       | Geopolitical Conflict  |
| 2008-09-15 | Global Financial Crisis intensifies  | Economic Shock         |
| 2020-03-09 | COVID-19 oil price crash             | Economic Shock         |
| 2022-02-24 | Russia invades Ukraine               | Geopolitical Conflict  |
*Full event dataset is in `data/key_events.csv`*

## 3. Initial Exploratory Data Analysis (EDA)
**Price Trends:** Long-term growth with sharp spikes during crises (e.g., 2008 financial crisis, 2020 pandemic).  

**Stationarity:** Raw prices are non-stationary; log returns improve stationarity and are suitable for modeling.  

**Volatility Patterns:** Observed clustering during crises motivates probabilistic modeling.  

*Visualizations are included in the EDA notebook.*

## 4. Data Analysis Workflow
1. **Data Loading & Cleaning**
   - Convert `Date` to datetime
   - Sort chronologically
   - Handle missing or anomalous values
2. **Exploratory Data Analysis**
   - Plot prices and log returns
   - Examine volatility clustering
3. **Event Data Compilation**
   - Align key events with price data
   - Document event dates and categories
4. **Bayesian Change Point Modeling**
   - Define switch-point model with pre/post change parameters
   - Run MCMC to estimate posterior distributions
5. **Interpretation**
   - Map change points to events
   - Quantify impact of major events
6. **Communication**
   - **Jupyter Notebook:** Technical exploration
   - **Report / Blog:** Executive summary for stakeholders
   - **Dashboard:** Interactive exploration of trends and events

## 5. Assumptions & Limitations
**Assumptions:**  
- Events have near-immediate market effects.
- Structural breaks reflect meaningful shifts.  
- Daily prices adequately capture major market dynamics.  

**Limitations:**  
- Change points indicate correlation, not causation.
- Overlapping events complicate interpretation.  
- Lagged effects may not be captured.  
- Macroeconomic indicators are excluded at this stage.

## 6. Understanding the Model
**Time Series Properties:** Trend, stationarity, and volatility patterns inform modeling choices.
**Change Point Models:** Identify shifts in statistical properties; outputs include posterior distributions for break dates and pre/post regime parameters.  
**Bayesian Approach:** Provides probabilistic estimates, quantifies uncertainty, and allows formal hypothesis testing.  
