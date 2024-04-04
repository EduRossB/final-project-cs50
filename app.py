from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aboutus")
def aboutUs():
    return render_template("aboutUs.html")

@app.route("/iniciarSesion")
def iniciarSesion():
    return render_template("iniciarSesion.html")

@app.route("/order")
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
