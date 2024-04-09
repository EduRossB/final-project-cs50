from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session
from helpers import login_required

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aboutus")
def aboutUs():
    return render_template("aboutUs.html")

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(email, password)
    else:
        return render_template("index.html")

@app.route("/order")
@login_required
def order():
    return render_template("order.html")

@app.route("/workwithus")
def workwithus():
    return render_template("workwithus.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
