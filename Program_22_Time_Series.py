import plotly.express as px
import pandas as pd

# Load time series data (replace 'your_dataset.csv' with your actual dataset file)
time_series_data = pd.read_csv('your_dataset.csv')

# Create a time series plot using Plotly Express
# Specify the x-axis as the time-related column (e.g., 'date') and y-axis as the value column
fig = px.line(time_series_data, x='date', y='value', title='Time Series Plot')

# Display the time series plot
fig.show()
