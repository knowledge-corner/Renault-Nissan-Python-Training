# Read and clean data here

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

