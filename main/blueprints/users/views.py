from flask import Blueprint, render_template,request,url_for,redirect,flash
from models.user import User
from forms import RegistrationForm
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,LoginManager,login_required,logout_user,login_user,current_user
from models.preference import Preference
from models.user_preference import User_Preference
from models.general import General
import json
from random import shuffle

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates/')



@users_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )
        new_user.save()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('signup.html', title='Register', form=form)

@users_blueprint.route("/<username>", methods=['GET'])
def show(username):
    insta = General.get(name='instagram')
    insta_tag = insta.contents
    twitter = General.get(name='twitter')
    twitter_tag = insta.contents
    p_list = User_Preference.get_or_none(User_Preference.user==current_user.id)
    if p_list:
        results = []
        p_id = User_Preference.select(User_Preference.preference).where(User_Preference.user==current_user.id)
        preferences = Preference.select().where(Preference.id.in_(p_id))
        for preference in preferences:
            for article in preference.articles:
                json_article = json.loads(article)
                json_article['category']=preference.categories
                results.append(json_article)
        shuffle(results)
        return render_template('show.html',results=results,insta_tag=insta_tag,twitter_tag=twitter_tag) 
    else:
        results = []
        p_id =[1,2,3,4]
        preferences = Preference.select().where(Preference.id.in_(p_id))
        for preference in preferences:
            for article in preference.articles:
                json_article = json.loads(article)
                json_article['category']=preference.categories
                results.append(json_article)
        shuffle(results)
        return render_template('show.html',results=results,insta_tag=insta_tag,twitter_tag=twitter_tag) 

@users_blueprint.route("/edit", methods=['GET'])
def edit():
    p_list = User_Preference.get_or_none(User_Preference.user==current_user.id)
    if p_list:
        p_id = User_Preference.select(User_Preference.preference).where(User_Preference.user==current_user.id)
        preferences = Preference.select().where(Preference.id.in_(p_id))
        not_preferences = Preference.select().where(Preference.id.not_in(p_id))
        return render_template('edit.html',not_preferences=not_preferences,preferences=preferences) 
    else:
        not_preferences = Preference.select()
        return render_template('edit.html',not_preferences=not_preferences) 

@users_blueprint.route("/carousel") 
def carousel():
    return render_template('carousel.html')
