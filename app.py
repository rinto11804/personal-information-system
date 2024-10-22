from flask import Flask
from flask import render_template, request, redirect, url_for
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


@app.route("/register", methods=["GET", "POST"])
def signup():
    context = {}
    cursor = mysql.connection.cursor()
    if request.method == "POST":
        print(request.form)
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        department = request.form["department"]
        role = request.form["role"]
        cursor.execute(
            """INSERT INTO employee (name,email,password,departmentId) VALUES(%s,%s,%s,%s)""",
            (name, email, password, department),
        )
        mysql.connection.commit()
        cursor.close()
        context["msg"] = "Your registed successfully"
        return render_template("signup.html", context=context)

    cursor.execute("SELECT id,name FROM department")
    context["departments"] = list(cursor.fetchall())
    print(context["departments"])
    cursor.close()
    return render_template("signup.html", context=context)


@app.route("/login", methods=["GET", "POST"])
def login():
    context = {}
    if request.method == "POST":
        print(request.form)
        email = request.form["email"]
        password = request.form["password"]
        cursor = mysql.connection.cursor()
        cursor.execute(
            """SELECT * FROM employee WHERE email=%s AND password=%s""",
            (email, password),
        )
        employee = cursor.fetchone()
        cursor.close()
        print(employee)
        context["employee"] = employee
        return redirect("dashboard")
    return render_template("login.html")


@app.route("/employee/contact")
def create_contact():
    cursor = mysql.connection.cursor()
    if request.method == "POST":
        print(request.form)
        phoneNumber = request.form["phoneNumber"]
        city = request.form["city"]
        cursor.execute(
            """INSERT INTO contact (phoneNumber,city) VALUES(%s,%s)""",
            (phoneNumber, city),
        )
        mysql.connection.commit()
    cursor.execute(
        "SELECT e.name,e.email,c.phoneNumber,c.city FROM contact c JOIN employee e ON c.id = e.contactId"
    )
    contacts = cursor.fetchall()
    cursor.close()
    return render_template("contact.html", contacts=contacts)


# @app.route("/employee/profile")
# def view_profile():
#     cursor = mysql.connection.cursor()
#     cursor.execute(
#         "SELECT e.name,e.email,c.phoneNumber,c.city FROM contact c JOIN employee e ON c.id = e.contactId"
#     )
#     contacts = cursor.fetchall()
#     cursor.close()
#     return render_template("profile.html", employee=employees[0])


@app.route("/departments", methods=["GET", "POST"])
def departments_page():
    cursor = mysql.connection.cursor()
    if request.method == "POST":
        name = (request.form.get("name"),)
        description = (request.form.get("description"),)
        cursor.execute(
            """INSERT INTO department (name,description) VALUES(%s,%s)""",
            (name, description),
        )
        mysql.connection.commit()
        cursor.execute("SELECT name,description FROM department")
        departments = cursor.fetchall()
        print(departments)
        return render_template("department.html", departments=departments)
    cursor.execute("SELECT name,description FROM department")
    departments = list(cursor.fetchall())
    print(departments)
    cursor.close()
    return render_template("department.html", departments=departments)


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    context = {}
    cursor = mysql.connection.cursor()
    if request.method == "POST":
        # Extract form data
        project_name = request.form.get("name")
        description = request.form.get("description")
        priority = request.form.get("priority")
        deadline = request.form.get("deadline")
        departmentId = request.form.get("department")

        insert_query = """
            INSERT INTO projects (name, description, priority, deadline, departmentId)
            VALUES (%s, %s, %s, %s, %s);
        """

        print(departmentId)
        cursor.execute(
            insert_query, (project_name, description, priority, deadline, departmentId)
        )
        mysql.connection.commit()
        return redirect(url_for("dashboard"))
    cursor.execute("SELECT id, name, description, priority, deadline FROM projects;")
    projects = list(cursor.fetchall())
    context["projects"] = projects
    cursor.execute("SELECT id,name FROM department")
    departments = list(cursor.fetchall())
    print(departments)
    context["departments"] = departments
    cursor.close()
    return render_template("dashboard.html", context=context)
