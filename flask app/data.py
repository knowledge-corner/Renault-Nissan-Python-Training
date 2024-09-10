# Read and clean data here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

# From SQLITE3 -----------
# from sqlalchemy import create_engine
# con = create_engine("sqlite:///coffee_data.sqlite3")
# df = pd.read_csv("coffee_sales.csv")
# con.dispose()

df = pd.read_csv("coffee_sales.csv")
df.Date = pd.to_datetime(df.Date, format = "mixed")
df.insert(1, "Year", df.Date.dt.year)
df.insert(2, "Month", df.Date.dt.month_name())

cities = list(df["City"].unique())
years = list(df["Year"].unique())
months = list(df["Month"].unique())
products = list(df["Product"].unique())

def fig_bar_sales(data) :
    # Sales by product bar
    fig = plt.figure(figsize=(10, 5))
    sns.barplot(x='Product', y='Sales', hue='Product', data=df, estimator="sum",
                    errorbar=None)
    plt.title("Sales by Product", loc = "left", fontdict={"fontsize" : 16}, pad = 10)
    plt.xticks(rotation = 20, size = 8)
    
    # Save the plot to a BytesIO object
    img = BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    # Close the figure to release memory
    plt.close(fig)

    return plot_url


def fig_bar_profit(data) :
    # profit by product bar
    fig = plt.figure(figsize=(10, 5))
    sns.barplot(x='Product', y='Profit', hue='Product', data=df, estimator="sum",
                    errorbar=None)
    plt.title("Profit by Product", loc = "left", fontdict={"fontsize" : 16}, pad = 10)
    plt.xticks(rotation = 20, size = 8)
    
    # Save the plot to a BytesIO object
    img = BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    # Close the figure to release memory
    plt.close(fig)

    return plot_url

def fig_line_sales(data) :
    # sales over months line
    fig = plt.figure(figsize=(10, 5))
    sns.lineplot(x='Date', y='Sales', data=df, estimator="sum", color="teal",
                    errorbar=None)
    plt.title("Sales over Months", loc = "left", fontdict={"fontsize" : 16}, pad = 10)
    plt.xticks(rotation = 20, size = 8)
    
    # Save the plot to a BytesIO object
    img = BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    # Close the figure to release memory
    plt.close(fig)

    return plot_url


def fig_line_profit(data) :
    # profit over months line
    fig = plt.figure(figsize=(10, 5))
    sns.lineplot(x='Date', y='Profit', data=df, estimator="sum", color="teal",
                    errorbar=None)
    plt.title("Profit over Months", loc = "left", fontdict={"fontsize" : 16}, pad = 10)
    plt.xticks(rotation = 20, size = 8)

    
    # Save the plot to a BytesIO object
    img = BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    # Close the figure to release memory
    plt.close(fig)

    return plot_url

