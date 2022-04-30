from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required,current_user
from app.forms import CreateProfileForm
from app import db
from app.models import Pokemons,Profiles, Users, Transactions, Decks

profiles_bp = Blueprint('profiles_bp',__name__,
    template_folder='templates',
    static_folder='static', 
    static_url_path='assets')

@profiles_bp.route('/create', methods=['GET', 'POST'])
def create():