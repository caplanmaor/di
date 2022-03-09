from flask import Flask, render_template
from flaskext.markdown import Markdown
app = Flask(__name__)
Markdown(app)

@app.route("/exercises")
def exercises():
    file = open("/home/maor/projects/di/python/week11/day2/daily_challenge/lesson1/exercises.md", "r")
    md_text = file.read()
    return render_template('index.html',md_text=md_text)

@app.route("/lesson")
def lesson():
    file = open("/home/maor/projects/di/python/week11/day2/daily_challenge/lesson1/in-this-chapter.md", "r")
    md_text = file.read()
    return render_template('index.html',md_text=md_text)