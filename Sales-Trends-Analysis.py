import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import argparse
import os

# ---------------------------------------------------------
# Load data safely
# ---------------------------------------------------------

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    
    try:
        df = pd.read_csv(file_path, parse_dates=['Date'])
    except ValueError:
        raise ValueError("CSV must contain a valid 'Date' column in date format.")

    required_cols = {'Date', 'Sales'}
    if not required_cols.issubset(df.columns):
        raise KeyError(f"CSV must contain the columns: {required_cols}")

    return df

# ---------------------------------------------------------
# Prepare and transform data
# ---------------------------------------------------------
def prepare_data(df):
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
    monthly_sales['Month'] = monthly_sales['Month'].astype(str)
    return monthly_sales

# ---------------------------------------------------------
# Matplotlib Plot
# ---------------------------------------------------------
def plot_matplotlib(monthly_sales):
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_sales['Month'], monthly_sales['Sales'],
             marker='o', label='Monthly Sales')

    plt.title('Monthly Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()

# ---------------------------------------------------------
# Plotly Plot
# ---------------------------------------------------------
def plot_plotly(monthly_sales):
    fig = px.line(
        monthly_sales,
        x='Month',
        y='Sales',
        title='Monthly Sales Trends',
        markers=True
    )
    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Total Sales"
    )
    fig.show()


def main():
    # Orchestrate full workflow
