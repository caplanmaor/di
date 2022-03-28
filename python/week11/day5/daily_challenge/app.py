import requests
from flask import Flask, render_template, Markup, redirect

app = Flask(__name__)

@app.route("/pokemon/<id>")
def pokemon(id):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    data = response.json()
    name = data['forms'][0]['name']
    pic = data['sprites']['other']['official-artwork']['front_default']
    return render_template('pokemon.html', name=name, pic=pic)

@app.route("/pokemons/bytype/<type>")
def by_type(type):
    response = requests.get(f'https://pokeapi.co/api/v2/type/{type}')
    data = response.json()
    pokemons = data['pokemon']
    html_pokemons = ""
    # limit is set to 10 pokemons for faster testing
    for pokemon in pokemons[:10:]:
        name = pokemon['pokemon']['name']
        pic_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        data = pic_response.json()
        pic = data['sprites']['other']['official-artwork']['front_default']
        html_pokemons += Markup(f'<a href="http://127.0.0.1:5000/pokemon/{name}"><div class="pokemon"><h2>name: {name}</h2><br><img src={pic}></div></a>') 
    return render_template('bytype.html', pokemons=html_pokemons)

@app.route("/pokemons/all")
@app.route("/pokemons/all/<offset>")
def all(offset=0):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit=10&offset={offset}')
    data = response.json()
    pokemons = data['results']
    html_pokemons = ""
    for pokemon in pokemons:
        name = pokemon['name']
        pic_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        data = pic_response.json()
        pic = data['sprites']['other']['official-artwork']['front_default']
        html_pokemons += Markup(f'<a href="http://127.0.0.1:5000/pokemon/{name}"><div class="pokemon"><h2>name: {name}</h2><br><img src={pic}></div></a>') 
    html_pokemons += Markup(f'<br><a href="/move_forward/{offset}">Show the next 10 pokemons</a>')
    return render_template('all.html', pokemons=html_pokemons)

@app.route("/move_forward/<offset>")
def moveforward(offset):
    offset = int(offset)
    offset += 10
    return redirect(f'http://127.0.0.1:5000/pokemons/all/{offset}')

@app.route("/")
def Home():
    response = requests.get(f'https://pokeapi.co/api/v2/type')
    data = response.json()
    types = data['results']
    print(types)
    html_types = Markup("<h1>pokemon types:</h1>")
    for i,type in enumerate(types):
        name = type['name']
        # pic_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        # data = pic_response.json()
        # pic = data['sprites']['other']['official-artwork']['front_default']
        html_types += Markup(f'<a href="http://127.0.0.1:5000/pokemons/bytype/{name}"><div class="pokemon"><h2>{name}</h2></div></a>') 
    return render_template('all.html', pokemons=html_types)