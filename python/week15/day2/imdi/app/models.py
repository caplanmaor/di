from app import db

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    country_made = db.Column(db.String(64), db.ForeignKey('country.name'))
    avilable_countries = db.relationship('Film_Country_J', backref='avilable_ref', lazy='dynamic')
    directed_by = db.relationship('Film_Director_J', backref='directed_ref', lazy='dynamic')
    in_categories = db.relationship('Film_Category_J', backref='category_ref', lazy='dynamic')
    
    def __init__(self,title,avilable_countries = tuple(),directed_by = tuple(),in_categories = tuple()):
        self.title = title

    def __repr__(self):
        return f'<Film: {self.title}>'
    try:
        def add_film(title,country_made,avilable_countries,directed_by,in_categories):
            country_madei = Country(name=country_made)
            film = Film(title)
            country_madei.films_made.append(film)
            db.session.add(country_madei)
            db.session.commit()

            db.session.add(film)
            db.session.commit()

            avilable_countries_list = avilable_countries.split()
            for country in avilable_countries_list:
                country_avilable = Country(name=country)
                film_country_j = Film_Country_J()
                country_avilable.films_avilable.append(film_country_j)
                db.session.add(country_avilable)
                db.session.commit()
                film.avilable_countries.append(film_country_j)
            
            categories_list = in_categories.split()
            for category in categories_list:
                categoryi = Category(name=category)
                film_category_j = Film_Category_J()
                categoryi.films_category.append(film_category_j)
                film.in_categories.append(film_category_j)
                db.session.add(categoryi)
                db.session.commit()

            directors = directed_by.split(', ')
            for director in directors:
                names = director.split()
                director = Director(first_name=names[0],last_name=names[1])
                film_director_j = Film_Director_J()
                director.films_directed.append(film_director_j)
                db.session.add(director)
                db.session.commit()
                film.directed_by.append(film_director_j)

            db.session.add(film)
            db.session.commit()
    except:
        print("cant add film")

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    films_made = db.relationship('Film', backref='nationality', lazy='dynamic')
    films_avilable = db.relationship('Film_Country_J', backref='film_ref', lazy='dynamic')

    def __init__(self,name,films_made = tuple(),films_avilable = tuple()):
        self.name = name
        self.films_made = films_made
        self.films_avilable = films_avilable

    def __repr__(self):
        return f'<Country: {self.name}>'

class Film_Country_J(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))

class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    films_directed = db.relationship('Film_Director_J', backref='director_ref', lazy='dynamic')

    def __init__(self,first_name,last_name,films_directed = tuple()):
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self):
        return f'<Director: {self.first_name}>'

    def add_director(first_name,last_name,films_directed):
        director = Director(first_name,last_name)
        film_director_j = Film_Director_J()
        print(films_directed)
        director.films_directed.append(film_director_j)
        for film in films_directed:  
            filmi = Film.query.filter_by(title=film).first()   
            filmi.directed_by.append(film_director_j)
            db.session.commit()
        db.session.add(director)
        db.session.commit()

class Film_Director_J(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    films_category = db.relationship('Film_Category_J', backref='director_ref', lazy='dynamic')

    def __init__(self,name,films_category = tuple()):
        self.name = name
    
    def __repr__(self):
        return f'<Category: {self.name}>'

class Film_Category_J(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))