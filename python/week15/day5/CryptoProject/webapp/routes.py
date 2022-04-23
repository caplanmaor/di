from webapp import app, db
from webapp.models import User, Currency, User_Currency_J
from flask import redirect, render_template
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from webapp.forms import LogInForm,SignUpForm
from webapp import mail
import flask_mail

@app.route('/', methods=['GET', 'POST'])
def home():
    coins = Currency.query.all()
    return render_template('home.html', coins=coins)

@app.route('/update_currencies', methods=['GET', 'POST'])
def update():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    parameters = {
    'start':'1',
    'limit':'20'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '15daef1e-3fcc-46e5-8dcb-694f950ab633',
    }

    session = Session()
    session.headers.update(headers)
    coins = []
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        coins = data['data']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("errors:")
        print(e)

    
    for coin in coins:
        name = coin['name']
        symbol = coin['symbol']
        first_historical_data = coin['first_historical_data']
        last_historical_data = coin['last_historical_data']
        is_active = coin['is_active']

        # check if already exists
        currency_temp = Currency.query.filter_by(name=name).first()
        if not currency_temp:
            currency = Currency(name,symbol,first_historical_data,last_historical_data,is_active)
            db.session.add(currency)
            db.session.commit()
            print(f'inserted coin {name}')
        else:
            print(f'coin {name} already exists')

    return str(coins)

@app.route('/specifics/<symbol>', methods=['GET', 'POST'])
def specifics(symbol):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info'
    parameters = {
    'symbol': symbol,
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '15daef1e-3fcc-46e5-8dcb-694f950ab633',
    }

    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        details = data['data']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("errors:")
        print(e)
    return render_template('details.html', details=details, symbol=symbol)    
    

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
        return redirect('http://127.0.0.1:5000/')
    return render_template('/user/login.html', form=login_formi)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('http://127.0.0.1:5000/')

@app.route('/save/<symbol>', methods=['GET', 'POST'])
@login_required
def save(symbol):
    user = User.query.filter_by(name=current_user.name).first()
    currency = Currency.query.filter_by(symbol=symbol).first()
    user_currency_j = User_Currency_J()
    user.coins.append(user_currency_j)
    currency.users.append(user_currency_j)
    db.session.commit()
    return 'the coin was saved to the user'

@app.route('/email/<symbol>', methods=['GET', 'POST'])
def email(symbol):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info'
    parameters = {
    'symbol': symbol,
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '15daef1e-3fcc-46e5-8dcb-694f950ab633',
    }

    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        details = data['data']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("errors:")
        print(e)

    msg = flask_mail.Message('Crypto Coin Info',
        sender='caplanmaor@gmail.com',
        recipients=['caplanmaor@gmail.com','tinyzohar@gmail.com'])
    msg.body = str(details)
    mail.send(msg)
    return 'email sent'
    
