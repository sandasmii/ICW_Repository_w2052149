# ICW_Repository_w2052149

# Sri Lankan Exchange Rate Analysis Dashboard

**Repository Name:** `ICW_Repository_w2052149`  
**Module:** 5DATA004W – Data Science Project Lifecycle  
**Student ID:** w2052149

---

## Project Overview

This project explores historical exchange rate trends of the Sri Lankan Rupee (LKR) against the US Dollar from 1970 to 2022. It follows the complete data science lifecycle, from data acquisition and cleaning to visual analytics and deployment.
The goal is to present key insights into Sri Lanka’s monetary trends and economic crises (notably in 2022) through an interactive Streamlit dashboard.

---

## Files and Folders

| File | Description |
|------|-------------|
| `exchange-rates_lka.csv` | Raw dataset downloaded from HDX containing monthly exchange rate data and metadata |
| `cleaned_exchange_rates.csv` | Cleaned dataset with unnecessary columns removed, missing values handled, and date formatting applied |
| `final_exchange_rates.csv` | Final dataset used in the Streamlit app, including winsorized values, rolling statistics, and engineered features |
| `streamlit_app.py` | Main Python script for launching the Streamlit dashboard |
| `requirements.txt` | Contains the required packages for running the dashboard |
| `.devcontainer/` | Container configuration (if applicable for VS Code remote environments) |

---

## Live Dashboard Deployment

The Streamlit app has been deployed on **Streamlit Community Cloud** and is accessible here:  
https://icwrepositoryw2052149-mncqneravpr8mz8rnlphgg.streamlit.app/

---

## Dashboard Features

### Visualization 1: Exchange Rate Trend Over Time
A line chart that shows the LKR to USD exchange rate from 1970 to 2022. This helps to understand the long-term depreciation of the Sri Lankan Rupee.

### Visualization 2: Year-on-Year Change
Shows the annual percentage change in the exchange rate, indicating periods of significant currency volatility.

### Visualization 3: 12-Month Rolling Average
Visualizes smoothed exchange rate trends using a 12-month rolling average to eliminate short-term fluctuations.

### Visualization 4: 2022 Economic Crisis Highlight
A focused view highlighting the timeline of the 2022 crisis using vertical markers.

### Visualization 5: Correlation Analysis
An interactive scatterplot to compare variables like YoY Change, Exchange Rate, and Rolling Averages, including a calculated Pearson correlation coefficient.

### Filters & Interactivity
- Year range filter (slider)
- Monthly vs annual toggle
- Dropdowns for correlation plot axes
- Dataset preview table

---

## Technologies Used

- **Python**
- **Pandas**
- **Matplotlib**
- **Plotly**
- **Streamlit**
- **Git & GitHub**

---

## Key Insights

- The LKR has shown a steady depreciation over decades, with sharp spikes during economic instability.
- The 2022 crisis marked the most significant drop due to political unrest, global inflation, and currency reserve depletion.
- There is minimal linear correlation between short-term YoY changes and long-term rolling trends, suggesting that short-term events do not strongly influence overall trend patterns.

---

## References

- Koop, A. (2022). *Sri Lanka’s political and economic situation, visualized*. World Economic Forum.  
  [https://www.weforum.org/stories/2022/07/economic-politics-debt-protest-crisis-sri-lanka](https://www.weforum.org/stories/2022/07/economic-politics-debt-protest-crisis-sri-lanka)

- Larson, E. (2024). *Why do exchange rates fluctuate?* | Western Union.  
  [https://www.westernunion.com/blog/en/us/what-causes-exchange-rates-to-change](https://www.westernunion.com/blog/en/us/what-causes-exchange-rates-to-change)

---



