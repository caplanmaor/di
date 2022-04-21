from app import app, db
from app.models import Film, Country, Director, Film_Director_J, Film_Country_J, Category, Film_Category_J, User
from flask import redirect, render_template
from app.forms import AddFilmForm,AddDirectorForm, SignUpForm, LogInForm
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

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
@login_required
def add_film():
    add_film_formi = AddFilmForm()
    if add_film_formi.validate_on_submit():
        title = add_film_formi.title.data
        created_in_country = add_film_formi.created_in_country.data
        avilable_in_countries = add_film_formi.avilable_in_countries.data
        directors = add_film_formi.directors.data
        categories = add_film_formi.categories.data
        Film.add_film(title,created_in_country,avilable_in_countries,directors,categories)
        return redirect('http://127.0.0.1:5000/')
    return render_template('/film/addFilm.html', form=add_film_formi)


@app.route('/add_director', methods=['GET', 'POST'])
@login_required
def add_director():
    add_director_formi = AddDirectorForm()
    if add_director_formi.validate_on_submit():
        first_name = add_director_formi.first_name.data
        last_name = add_director_formi.last_name.data
        films_directed = add_director_formi.films_directed.data
        print(films_directed)
        Director.add_director(first_name,last_name,films_directed)
        return redirect('http://127.0.0.1:5000/')
    else:
        print('valid failed')
    return render_template('/director/addDirector.html', form=add_director_formi)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_formi = SignUpForm()
    if signup_formi.validate_on_submit():
        username = signup_formi.username.data
        email = signup_formi.email.data
        password1 = signup_formi.password1.data
        password2 = signup_formi.password2.data

        # check if already exists
        temp_user = User.query.filter_by(email=email).first()
        if temp_user:
            return "a user already exists with this email"

        if password1 != password2:
            return "passwords dont match"

        # create user
        user = User(email=email, name=username, password=generate_password_hash(password1, method='sha256'))
        db.session.add(user)
        db.session.commit()
        return redirect('http://127.0.0.1:5000/login')

    return render_template('user/signup.html', form=signup_formi)

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_formi = LogInForm()
    if login_formi.validate_on_submit():
        username = login_formi.username.data
        password = login_formi.password.data
        user = User.query.filter_by(name=username).first()
        
        # check password
        if not user or not check_password_hash(user.password, password):
            return 'wrong password or username doesnt exist'

        # log in
        login_user(user, remember=True)
        return redirect('http://127.0.0.1:5000/profile')
    return render_template('/user/login.html', form=login_formi)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('http://127.0.0.1:5000/')

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('user/profile.html', name=current_user.name)