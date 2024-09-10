# ---------- All imports
from flask import Flask, render_template, Response
from data import *

app = Flask(__name__)



@app.route("/")   # url pattern
def home_page():
    total_sales = df.Sales.sum()
    total_profits = df.Profit.sum()
    chart = (fig_bar_sales(df), fig_bar_profit(df), fig_line_profit(df), fig_line_sales(df))
    return render_template("homepage.html", cities = cities, sales = total_sales,
                           profit = total_profits, selected_city = "Select City", chart = chart)

@app.route("/filter/<city>")   # url pattern
def filter_by_city(city):
    filter_df = df[df.City == city]
    total_sales = filter_df.Sales.sum()
    total_profits = filter_df.Profit.sum()
    chart = (fig_bar_sales(filter_df), fig_bar_profit(filter_df), 
             fig_line_profit(filter_df), fig_line_sales(filter_df))
    return render_template("homepage.html", cities = cities, sales = total_sales,
                           profit = total_profits, selected_city = city, chart = chart)

if __name__ == "__main__" :
    app.run()