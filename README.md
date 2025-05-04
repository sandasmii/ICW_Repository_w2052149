# ICW_Repository_w2052149

Description:
This repository contains the full lifecycle of a data science project developed for the 5DATA004W – Data Science Project Lifecycle module. The project explores historical exchange rate trends of the Sri Lankan Rupee (LKR) from 1970 to 2022, using publicly available data from Humanitarian Data Exchange (HDX). The final product is an interactive dashboard built using Streamlit to support government policy analysis and decision-making.

It includes:

_**1. Dataset Files**_

**exchange_rates.csv**

- The original dataset obtained from HDX.

- Contains raw exchange rate data of the Sri Lankan Rupee (LKR) to USD from 1970 to 2022.

- Includes multiple unused metadata columns.

**cleaned_exchange_rates.csv**

This file contains the cleaned version of the original HDX exchange rate dataset. The following preprocessing steps were applied:

- Dropped irrelevant columns (Flag, Currency, ISO Code, etc.)

- Removed duplicate rows and missing values

- Renamed and formatted columns (Date, Exchange_Rate)

- Extracted Year and Month for filtering

- Sorted the data chronologically

_This file was primarily used for exploration, EDA, and feature engineering._

**final_exchange_rates.csv**

This is the final version of the dataset used in the Streamlit dashboard. It includes:

- Exchange_Rate_Winsorized: Outlier-handled exchange rate

- Exchange_Rate_Change: Daily % change

- Rolling_Mean and Rolling_Std: 30-day rolling statistics

_This dataset is loaded by streamlit_app.py and powers the visualizations in the dashboard._


