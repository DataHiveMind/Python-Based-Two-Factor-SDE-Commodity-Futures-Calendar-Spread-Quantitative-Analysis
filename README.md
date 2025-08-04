Python-Based Two-Factor SDE Commodity Futures Calendar Spread Analysis
This repository implements a modular Python pipeline designed to systematically ingest, cleanse, engineer features for, and model commodity futures calendar spreads using a two-factor stochastic differential equation (SDE) framework. The focus is on WTI-Brent cross-commodity analysis, automating the end-to-end workflow from raw market data through alpha generation.

Problem Statement
Commodity futures term structures exhibit rich dynamics driven by mean-reversion, seasonality, stochastic volatility, and evolving convenience yields. Capturing alpha in calendar spreads demands disentangling transient demand shocks from long-term structural trends.

At a senior quantitative level, we pose the following challenge:

We model the front- and back-month futures spread 
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

Key Features
Automated data ingestion from multiple vendor APIs with version control

Data cleansing modules handling missing values, outliers, and corporate actions

Two-factor SDE feature generation capturing convenience yield and trend dynamics

Time-series features: rolling moments, cointegration residuals, seasonality indices

Cross-commodity analysis leveraging both WTI and Brent curves

Flexible modeling: XGBoost, feed-forward and recurrent neural networks

Backtesting framework with transaction cost modeling and walk-forward optimization

Continuous integration with linting, unit tests, and reproducible Docker environment
