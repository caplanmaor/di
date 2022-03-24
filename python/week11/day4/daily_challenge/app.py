from flask import Flask, render_template, url_for
import json
app = Flask(__name__)

@app.route("/Home")
def home():
    return render_template("index.html")

@app.route("/colors")
def colors():
    file = open("colors.json")
    text = file.read()
    parsed = json.loads(text)
    colors = []
    for item in parsed:
        colors.append(item)
    return str(colors)

@app.route("/color/<color_name>")
def color(color_name=None):
    with open("colors.json") as file:
        text = file.read()
        parsed = json.loads(text)
        colors = []
        for item in parsed:
            if item == color_name:
                bg_color = item
        # for color in colors:
        #     if color == color_name:
        #         bg_color = color
        
        return render_template('color.html', color=bg_color)
