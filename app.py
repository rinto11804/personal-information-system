from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register")
def signup():
    return render_template("signup.html")


@app.route("/login")
def login():
    return render_template("login.html")
