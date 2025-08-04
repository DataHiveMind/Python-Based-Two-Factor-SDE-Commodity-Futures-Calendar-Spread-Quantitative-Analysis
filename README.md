Python-Based Two-Factor SDE Commodity Futures Calendar Spread Analysis
This repository implements a modular Python pipeline designed to systematically ingest, cleanse, engineer features for, and model commodity futures calendar spreads using a two-factor stochastic differential equation (SDE) framework. The focus is on WTI-Brent cross-commodity analysis, automating the end-to-end workflow from raw market data through alpha generation.

# Problem Statement
Commodity futures term structures exhibit rich dynamics driven by mean-reversion, seasonality, stochastic volatility, and evolving convenience yields. Capturing alpha in calendar spreads demands disentangling transient demand shocks from long-term structural trends.

At a senior quantitative level, we pose the following challenge:

We model the front-month and back-month futures spread 
𝑆
𝑡
=
𝐹
𝑡
(
1
)
−
𝐹
𝑡
(
2
)
 under a two-factor SDE

𝑑
𝑋
𝑡
= 𝜅
𝑋
(
𝜃
𝑋
−
𝑋
𝑡
)
 
𝑑
𝑡
+
𝜎
𝑋
 
𝑑
𝑊
𝑡
𝑋
𝜅
𝑋
(
𝜃
𝑋
−
𝑋
𝑡
)
 
𝑑
𝑡
+
𝜎
𝑋
 
𝑑
𝑊
𝑡
𝑋
,


dyt =
𝜇
𝑌
 
𝑑
𝑡
+
𝜎
𝑌
 
𝑑
𝑊
𝑡
𝑌

,
where 
𝑋
𝑡
 captures the mean-reverting convenience yield component, and 
𝑌
𝑡
 captures the non-stationary long-term drift of the spread.

Our task is to calibrate 
{
𝜅
𝑋
,
𝜃
𝑋
,
𝜎
𝑋
,
𝜇
𝑌
,
𝜎
𝑌
}
 on historical WTI and Brent futures, extract predictive signals via time-series feature engineering, and integrate machine-learning models (XGBoost, deep neural networks) to forecast spread returns. The ultimate goal is to generate statistically significant, risk-adjusted P&L across rolling backtests, while maintaining robust controls for transaction costs and regime shifts.

# Key Features
1. Automated data ingestion from multiple vendor APIs with version control

2. Data cleansing modules handling missing values, outliers, and corporate actions

3. Two-factor SDE feature generation capturing convenience yield and trend dynamics

4. Time-series features: rolling moments, cointegration residuals, seasonality indices

5. Cross-commodity analysis leveraging both WTI and Brent curves

6. Flexible modeling: XGBoost, feed-forward, and recurrent neural networks

7. Backtesting framework with transaction cost modeling and walk-forward optimization

8. Continuous integration with linting, unit tests, and a reproducible Docker environment

# Project Structure
|- Config/   Configuration files (YAML)
|- Data/     Raw, and Processed Datasets
|- Notebooks/ Exploratory analysis and experiments
|- Src/  Core modules: ingestion, cleaning, features, modeling
|- Tests/  Unit tests for each pipeline stage
|- Models/ Trained model artifacts
|- Scripts/ Shell wrappers for pipeline execution
|- Reports/ Figures, tables, and performance summaries

# Installation
1. Clone the repository:
    git clone https://github.com/your-org/python-sde-calendar-spread.git
cd python-sde-calendar-spread

2. Create and activate the Conda environment:
    conda env create -f environment.yml
conda activate sde-spread

3. Install additional dependencies (if using pip):
    pip install -r requirements.txt
4. Configure local parameters:
    cp config/default.yaml config/local.yaml

# Usage:
## Data ingestion:
bash scripts/run_preprocessing.sh

## Model Training: 
bash scripts/run_training.sh

## Evaluation & Reporting:
bash scripts/run_evaluation.sh

# Contributing
## We welcome improvements in:

1. Feature engineering modules (seasonality, liquidity, macro overlays)

2. New modeling approaches (Gaussian processes, reinforcement learning)

3. Enhanced backtesting rigor (Monte Carlo resampling, stress testing)

Please open issues or submit pull requests against the develop branch.


