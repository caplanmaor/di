from flask import Flask, render_template, jsonify, redirect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
import psycopg2
import os
from flask_cors import CORS, cross_origin
from forms import Add_film_form
from flask_wtf import Form

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"

def get_db_connection():
    conn = psycopg2.connect(
            host="localhost",
            database="imdb",
            user="postgres",
            password="postgres")
    return conn

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

add_film = {}

@app.route("/homepage")
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM film')
    response = cur.fetchall()
    films = []
    for film in response:
        film_object = {}
        film_object['title'] = film[1]
        film_object['release_date'] = film[2]
        film_object['created_in_country'] = film[3]
        film_object['avilable_in_countries'] = film[4]
        films.append(film_object)
    cur.close()
    conn.close()
    print(films)
    return render_template('homepage.html', films = films)


@app.route("/films/addFilm", methods=('GET', 'POST'))
def addFilm():
    form = Add_film_form()
    if form.validate_on_submit():
        add_film={'title': form.title.data,
                             'release_date': form.release_date.data,
                             'created_in_country': form.created_in_country.data,
                             'avilable_in_countries': form.avilable_in_countries.data,
                             'category': form.category.data,
                             'director': form.director.data,
                             }
        print(add_film)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO film (title, release_date, created_in_country, avilable_in_countries, category, director) VALUES (%(title)s, %(release_date)s, %(created_in_country)s, %(avilable_in_countries)s, %(category)s, %(director)s)", {'title': add_film["title"], 'release_date': add_film["release_date"], 'created_in_country': add_film["created_in_country"], 'avilable_in_countries': add_film["avilable_in_countries"], 'category': add_film["category"], 'director': add_film["director"]})
        conn.commit()
        cur.close()
        conn.close()
        return redirect("http://127.0.0.1:5000/homepage")
        
    return render_template('/film/addFilm.html', form=form)
    
@app.route("/films/addDirector")
def addDirector():
    return render_template('homepage.html')



# Base = declarative_base()
# 
# class Country(Base):
#     __tablename__ = 'country'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)

# class Category(Base):
#     __tablename__ = 'category'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)

# class Film(Base):
#     __tablename__ = 'film'
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     release_date = Column(String)
#     created_in_country = Column(Integer)
#     avilable_in_countries = Column(Integer)
#     category = Column(Integer)
#     director = Column(Integer)

# class Director(Base):
#     __tablename__ = 'director'
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
    
