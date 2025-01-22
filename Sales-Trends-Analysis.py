import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Load sales data
data = pd.read_csv('sales_data.csv', parse_dates=['Date'])
data['Month'] = data['Date'].dt.to_period('M')

# Aggregate sales by month
monthly_sales = data.groupby('Month')['Sales'].sum().reset_index()

# Plot with Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales['Month'].astype(str), monthly_sales['Sales'], marker='o', label='Monthly Sales')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

# Plot with Plotly
fig = px.line(monthly_sales, x='Month', y='Sales', title='Monthly Sales Trends', markers=True)
fig.update_layout(xaxis_title='Month', yaxis_title='Total Sales')
fig.show()
