# ICW_Repository_w2052149

## **Description**
This repository contains the full lifecycle of a data science project developed for the 5DATA004W – Data Science Project Lifecycle module. The project explores historical exchange rate trends of the Sri Lankan Rupee (LKR) from 1970 to 2022, using publicly available data from Humanitarian Data Exchange (HDX). The final product is an interactive dashboard built using Streamlit to support government policy analysis and decision-making.

## **Contents**

### 1. Dataset Files

#### **exchange-rates_lka.csv**
- The original raw dataset downloaded from HDX.
- Contains monthly exchange rates of the Sri Lankan Rupee (LKR) to USD from 1970 to 2022, along with additional metadata columns (e.g., ISO codes, flags, units).

#### **cleaned_exchange_rates.csv**
- The intermediate cleaned dataset, used for exploration and feature engineering.
- Applied preprocessing steps:
  - Removed unnecessary metadata columns
  - Renamed columns (e.g., StartDate → Date, Value → Exchange_Rate)
  - Removed duplicates and missing values
  - Converted date formats and extracted Year and Month
  - Sorted chronologically

#### **final_exchange_rates.csv**
- The final dataset used for dashboard visualizations. Includes:
  - Exchange_Rate_Winsorized – Outlier-handled exchange rates using winsorization
  - Exchange_Rate_Change – Daily percentage change
  - Rolling_Mean & Rolling_Std – 30-day rolling statistics for trend analysis

### 2. Application Code

#### **streamlit_app.py**
- The main Streamlit script for the dashboard.
- Implements multiple visualizations: trend lines, YoY change, rolling averages, correlation plots, and a focus on the 2022 crisis.
- Includes interactivity via year filtering, metric selection, and view toggling.

#### **dspl_icw_cleaning_w2052149.ipynb**
- Jupyter notebook used for data cleaning, EDA, and feature engineering.

### 3. Other Files
#### **requirements.txt**
- Lists all Python package dependencies for local deployment.

#### **.devcontainer/**
- Contains configuration for GitHub Codespaces.
  
#### **README.md**
- This documentation file.

