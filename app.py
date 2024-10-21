from flask import Flask
from flask import render_template, request
from dotenv import load_dotenv
from flask_mysqldb import MySQL

# import MySQLdb.cursors
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = "a_secret_key"
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")

mysql = MySQL(app)


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


@app.route("/contact")
def create_contact():
    if request.method == "POST":
        print(request.form)
        phoneNumber = request.form["phoneNumber"]
        city = request.form["city"]
        cursor = mysql.connection.cursor()
        cursor.execute(
            """INSERT INTO contact (phoneNumber,city) VALUES(%s,%s)""",
            (phoneNumber, city),
        )
        mysql.connection.commit()
        cursor.close()


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
