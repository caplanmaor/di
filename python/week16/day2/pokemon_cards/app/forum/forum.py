from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required,current_user
from app.forms import CreatePost
from app import db
from app.models import Pokemons,Profiles, Users, Posts

forum_bp = Blueprint('forum_bp',__name__,
    template_folder='templates',
    static_folder='static', 
    static_url_path='assets')

@forum_bp.route('/posts', methods=['GET', 'POST'])
# @login_required
def posts():
    posts = Posts.query.all()
    posts_array = []
    for post in posts:
        post_title = post.title
        post_body = post.body
        post_creator = db.session.query(Users).join(Posts, Users.id == Posts.user_id).filter_by(id=post.user_id).first()
        post_object = {'title': post_title, 'body': post_body, 'user': post_creator.name}
        posts_array.append(post_object)
    create_post_formi = CreatePost()
    if create_post_formi.validate_on_submit():  
        title = create_post_formi.title.data
        body = create_post_formi.body.data  
        post = Posts(title,body)
        user = Users.query.filter_by(name=current_user.name).first()
        user.posts.append(post)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('forum_bp.posts'))
    return render_template('posts.html', form=create_post_formi, posts=posts_array)