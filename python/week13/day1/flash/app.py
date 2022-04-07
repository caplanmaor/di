from flask import Flask,flash, render_template


app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"

@app.route("/")
def home():
    flash("this is a message")
    flash("this is a SECOND message")
    return render_template("home.html")