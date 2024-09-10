# ---------- All imports
from flask import Flask, render_template
from data import *

app = Flask(__name__)

@app.route("/")   # url pattern
def home_page():
    total_sales = df.Sales.sum()
    total_profits = df.Profit.sum()
    return render_template("homepage.html", cities = cities, sales = total_sales,
                           profit = total_profits, selected_city = "Select City")

@app.route("/filter/<city>")   # url pattern
def filter_by_city(city):
    filter_df = df[df.City == city]
    total_sales = filter_df.Sales.sum()
    total_profits = filter_df.Profit.sum()
    return render_template("homepage.html", cities = cities, sales = total_sales,
                           profit = total_profits, selected_city = city)


if __name__ == "__main__" :
    app.run()