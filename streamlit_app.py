
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('cleaned_exchange_rates 1.csv')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set up the Streamlit app
st.title('Sri Lankan Exchange Rates Dashboard')
st.markdown('This dashboard visualizes the exchange rates of the Sri Lankan Rupee (LKR) over time.')

# Sidebar for year range selection
st.sidebar.header('Filter by Year')
min_year = int(df['Year'].min())
max_year = int(df['Year'].max())
year_range = st.sidebar.slider('Select Year Range', min_year, max_year, (min_year, max_year))

# Filter data based on selected year range
filtered_df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

# Sidebar for monthly vs annual toggle
view_option = st.sidebar.radio('View by', ('Monthly', 'Annual'))

# Plotting the data
st.header('Exchange Rate Trends')
if view_option == 'Monthly':
    st.line_chart(filtered_df.set_index('Date')['Exchange_Rate'])
else:
    annual_df = filtered_df.groupby('Year').mean().reset_index()
    st.line_chart(annual_df.set_index('Year')['Exchange_Rate'])

# Highlighting the 2022 economic crisis
st.header('2022 Economic Crisis Highlight')
crisis_2022 = df[df['Year'] == 2022]
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Exchange_Rate'], label='Exchange Rate')
plt.axvline(pd.Timestamp('2022-01-01'), color='r', linestyle='--', label='2022 Crisis Start')
plt.axvline(pd.Timestamp('2022-12-31'), color='r', linestyle='--', label='2022 Crisis End')
plt.legend()
plt.title('Sri Lankan Exchange Rates with 2022 Crisis Highlight')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
st.pyplot(plt)

# Display the data table
st.header('Data Table')
st.dataframe(filtered_df)
    