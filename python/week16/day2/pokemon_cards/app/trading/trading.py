from contextlib import nullcontext
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required,current_user
from app.forms import CreateTransactionForm
from app import db
from app.models import Pokemons,Profiles, Users, Transactions_a,Transactions_b, Decks

trading_bp = Blueprint('trading_bp',__name__,
    template_folder='templates',
    static_folder='static', 
    static_url_path='assets')


@trading_bp.route('/market', methods=['GET', 'POST'])
def market():
    if current_user.is_authenticated:
        transactions = Transactions_a.query.all()
        posts=[]
        for post in transactions:
            pokemon = Pokemons.query.filter_by(id=post.pokemons).first()
            posted_by = Users.query.join(Profiles, Users.id==Profiles.user_id).filter_by(id=post.profile).first()
            post_obj = {'currency': post.currency,'pokemons': pokemon.name, 'profile': posted_by.name, 'img': pokemon.img} 
            posts.append(post_obj)
        create_transaction_formi = CreateTransactionForm()
        if create_transaction_formi.validate_on_submit():  
            transaction_a = Transactions_a()
            profile = Profiles.query.join(Users, Profiles.user_id==Users.id).filter_by(name=current_user.name).first()
            profile.transactions_a.append(transaction_a)
            pokemon_name = create_transaction_formi.pokemon.data
            pokemon = Pokemons.query.filter_by(name=pokemon_name[0]).first()
            pokemon.transactions_a.append(transaction_a)
            transaction_a.currency=create_transaction_formi.currency.data
            db.session.add(transaction_a)
            db.session.commit()
            return redirect(url_for('trading_bp.market'))
    else:
        return redirect(url_for('users_bp.login'))
    return render_template('trading.html', form=create_transaction_formi, transactions=posts)
