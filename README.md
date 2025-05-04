# ICW_Repository_w2052149

Description:
This repository contains the full lifecycle of a data science project developed for the 5DATA004W module. The project explores historical exchange rate trends of the Sri Lankan Rupee (LKR) using a cleaned dataset from 1970 to 2022. 

It includes:

**exchange_rates.csv**

The original dataset obtained from HDX, containing the exchange rate data of the Sri Lankan Rupee (LKR) from 1970 to 2022. 

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


