from app import app, db
from app.models import Film, Country, Director, Film_Director_J, Film_Country_J, Category, Film_Category_J
from flask import redirect, render_template
from app.forms import AddFilmForm,AddDirectorForm

@app.route('/', methods=['GET', 'POST'])
def home():
    films_query = Film.query.all()
    films=[]
    for film in films_query:
        title = film.title
        country_made = film.country_made
        avilable_countries = Country.query.join(Film_Country_J, Country.id==Film_Country_J.country_id).filter_by(film_id=film.id).join(Film, Film_Country_J.film_id==Film.id).all()
        directors = Director.query.join(Film_Director_J, Director.id==Film_Director_J.director_id).join(Film, Film_Director_J.film_id==Film.id).filter_by(id=film.id).all()
        categories = Category.query.join(Film_Category_J, Category.id==Film_Category_J.category_id).join(Film, Film_Category_J.film_id==Film.id).filter_by(id=film.id).all()
        filmi = {'title': title, 'country_made': country_made, 'avilable_countries': avilable_countries, 'directors': directors, 'categories': categories}
        films.append(filmi)        
    return render_template('homepage.html', films=films)


@app.route('/add_film', methods=['GET', 'POST'])
def add_film():
    add_film_formi = AddFilmForm()
    if add_film_formi.validate_on_submit():
        title = add_film_formi.title.data
        created_in_country = add_film_formi.created_in_country.data
        avilable_in_countries = add_film_formi.avilable_in_countries.data
        directors = add_film_formi.directors.data
        categories = add_film_formi.categories.data
        Film.add_film(title,created_in_country,avilable_in_countries,directors,categories)
        return "film created"
    return render_template('/film/addFilm.html', form=add_film_formi)


@app.route('/add_director', methods=['GET', 'POST'])
def add_director():
    add_director_formi = AddDirectorForm()
    if add_director_formi.validate_on_submit():
        first_name = add_director_formi.first_name.data
        last_name = add_director_formi.last_name.data
        films_directed = add_director_formi.films_directed.data
        print(films_directed)
        Director.add_director(first_name,last_name,films_directed)
        return "director created"
    else:
        print('valid failed')
    return render_template('/director/addDirector.html', form=add_director_formi)


@app.route('/signup', methods=['GET', 'POST'])
def signup():

@app.route('/login', methods=['GET', 'POST'])
def login():

@app.route('/logout', methods=['GET', 'POST'])
def logout():

@app.route('/profile/<user_id>', methods=['GET', 'POST'])
def logout(user_id):