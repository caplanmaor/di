from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required,current_user
from app.forms import CreateProfileForm
from app import db
from app.models import Pokemons,Profiles, Users

profiles_bp = Blueprint('profiles_bp',__name__,
    template_folder='templates',
    static_folder='static', 
    static_url_path='assets')

@profiles_bp.route('/create', methods=['GET', 'POST'])
def create():
    create_profile_formi = CreateProfileForm()
    if create_profile_formi.validate_on_submit():  
        pokemon_name = create_profile_formi.pokemon.data  
        profile = Profiles()
        user = Users.query.filter_by(name=current_user.name).first()
        user.user_profile.append(profile)
        pokemon = Pokemons.query.filter_by(name=pokemon_name[0]).first()
        pokemon.pokemon_profile.append(profile)
        db.session.add(profile)
        db.session.commit()
        return redirect(url_for('profiles_bp.display'))
    return render_template('create.html', form=create_profile_formi)


@profiles_bp.route('/display', methods=['GET', 'POST'])
def display():
    try:
        pokemon = db.session.query(Pokemons).join(Profiles, Pokemons.id == Profiles.pokemon_id).join(Users, Profiles.user_id == Users.id).filter_by(name=current_user.name).first()
        return render_template('display.html', pokemon_name=pokemon.name)
    except:
        return render_template('display.html')
