# ---------- All imports
from flask import Flask, render_template
from data import *

app = Flask(__name__)

@app.route("/")   # url pattern
def home_page():
    return render_template("homepage.html", cities = cities)


if __name__ == "__main__" :
    app.run()