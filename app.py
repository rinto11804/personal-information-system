from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register")
def signup():
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.form)
        email = request.form["email"]
        password = request.form["password"]
        return render_template("dashboard.html")
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
